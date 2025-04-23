# Pages

Pages map components to different URLs in your app. This section covers creating pages, handling URL arguments, accessing query parameters, managing page metadata, and handling page load events.

[Adding a Page](https://reflex.dev/docs/pages/overview/#adding-a-page)

# Adding a Page

You can create a page by defining a function that returns a component.
By default, the function name will be used as the route, but you can also specify a route.

```python
def index():
    return rx.text("Root Page")

def about():
    return rx.text("About Page")

def custom():
    return rx.text("Custom Route")

app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
```

In this example we create three pages:

- `index` - The root route, available at `/`
- `about` - available at `/about`
- `custom` - available at `/custom-route`

Index is a special exception where it is available at both `/` and `/index`. All other pages are only available at their specified route.

# Video: Pages and URL Routes

[Video Link](https://reflex.dev/docs/pages/overview/#page-decorator)

# Page Decorator

You can also use the `@rx.page` decorator to add a page.

```python
@rx.page(route="/", title="My Beautiful App")
def index():
    return rx.text("A Beautiful App")
```

This is equivalent to calling `app.add_page` with the same arguments.

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-18dvnhc" data-orientation="vertical" data-state="closed">
```

Remember to import the modules defining your decorated pages.

# Navigating Between Pages

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/pages/overview/#links">

# Links

Links are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

[Reflex Home Page.](https://reflex.dev/)

```python
rx.link("Reflex Home Page.", href="https://reflex.dev/")
```

You can also provide local links to other pages in your project without writing the full url.

[Example](/docs/library/)

```python
rx.link("Example", href="/docs/library")
```

To open the link in a new tab, set the `is_external` prop to `True`.

[Open in new tab](https://reflex.dev/ target="_blank")

```python
rx.link(
    "Open in new tab",
    href="https://reflex.dev/",
    is_external=True,
)
```

Check out the [link docs](/docs/library/typography/link/) to learn more.

# Video: Link-based Navigation

## Redirect Documentation

[Read More](https://reflex.dev/docs/pages/overview/#redirect)

# Redirect

Redirect the user to a new path within the application using `rx.redirect()`.

- **path**: The destination path or URL to which the user should be redirected.
- **external**: If set to True, the redirection will open in a new tab. Defaults to `False`.

## Examples

### Buttons for Redirecting

```python
rx.vstack(
    rx.button("open in tab", on_click=rx.redirect("/docs/api-reference/special_events")),
    rx.button("open in new tab", on_click=rx.redirect("https://github.com/reflex-dev/reflex/", is_external=True)),
)
```

### State-Based Redirect

```python
class Redirect2ExampleState(rx.State):
    redirect_to_org: bool = False

    @rx.event
    def change_redirect(self):
        self.redirect_to_org = not self.redirect_to_org

    @rx.var
    def url(self) -> str:
        return (
            "https://github.com/reflex-dev/"
            if self.redirect_to_org
            else "https://github.com/reflex-dev/reflex/"
        )

    @rx.event
    def change_page(self):
        return rx.redirect(self.url, is_external=True)

def redirect_example():
    return rx.vstack(
        rx.text(f"{Redirect2ExampleState.url}"),
        rx.button("Change redirect location", on_click=Redirect2ExampleState.change_redirect),
        rx.button("Redirect to new page in State", on_click=Redirect2ExampleState.change_page),
    )
```

https://github.com/reflex-dev/reflex/

- **Change redirect location**
- **Redirect to new page in State**

# Video: Redirecting to a New Page

[Redirecting to a New Page](https://reflex.dev/docs/pages/overview/#nested-routes)

# Nested Routes

Pages can also have nested routes.

```python
def nested_page():
    return rx.text("Nested Page")

app = rx.App()
app.add_page(nested_page, route="/nested/page")
```

This component will be available at `/nested/page`.

[Link](https://reflex.dev/docs/pages/overview/#page-metadata)

# Page Metadata

You can add page metadata such as:

* The title to be shown in the browser tab
* The description as shown in search results
* The preview image to be shown when the page is shared on social media
* Any additional metadata

```python
@rx.page(
    title="My Beautiful App",
    description="A beautiful app built with Reflex",
    image="/splash.png",
    meta=meta,
)
def index():
    return rx.text("A Beautiful App")

@rx.page(title="About Page")
def about():
    return rx.text("About Page")

meta = [
    {"name": "theme_color", "content": "#FFFFFF"},
    {"char_set": "UTF-8"},
    {"property": "og:url", "content": "url"}
]

app = rx.App()
```

[Learn more](https://reflex.dev/docs/pages/overview/#getting-the-current-page)

# Getting the Current Page

You can access the current page from the `router` attribute in any state. See the [router docs](/docs/utility-methods/router-attributes/) for all available attributes.

```python
class State(rx.State):
    def some_method(self):
        current_page_route = self.router.page.path
        current_page_url = self.router.page.raw_path  # ... Your logic here ...
```

The `router.page.path` attribute allows you to obtain the path of the current page from the router data, for dynamic pages this will contain the slug rather than the actual value used to load the page.

To get the actual URL displayed in the browser, use `router.page.raw_path`. This will contain all query parameters and dynamic path segments.

In the above example, `current_page_route` will contain the route pattern (e.g., `/posts/[id]`), while `current_page_url` will contain the actual URL (e.g., `/posts/123`).

To get the full URL, access the same attributes with `full_` prefix.

Example:

```python
class State(rx.State):
    @rx.var
    def current_url(self) -> str:
        return self.router.page.full_raw_path

def index():
    return rx.text(State.current_url)

app = rx.App()
app.add_page(index, route="/posts/[id]")
```

In this example, running on `localhost` should display `http://localhost:3000/posts/123/`