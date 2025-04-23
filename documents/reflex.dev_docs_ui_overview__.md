# UI Overview

Components are the building blocks for your app's user interface (UI). They are the visual elements that make up your app, like buttons, text, and images.

[Learn about component basics](/docs/ui/overview/#component-basics)

# Component Basics

Components are made up of children and props.

# Children
Text or other Reflex components nested inside a component. Passed as positional arguments.

# Props

Attributes that affect the behavior and appearance of a component.
Passed as **keyword arguments**.

Let's take a look at the `rx.text` component.

Hello World!

```python
rx.text("Hello World!", color="blue", font_size="1.5em")
```

"Hello World!" is the child text to display, while `color` and `font_size` are props that modify the appearance of the text.

Regular Python data types can be passed in as children to components. This is useful for passing in text, numbers, and other simple data types.

Now let's take a look at a more complex component, which has other components nested inside it. The `rx.vstack` component is a container that arranges its children vertically with space between them.

Sample Form
- Name

Subscribe to Newsletter

```python
rx.vstack(
    rx.heading("Sample Form"),
    rx.input(placeholder="Name"),
    rx.checkbox("Subscribe to Newsletter"),
)
```

Some props are specific to a component. For example, the `header` and `content` props of the `rx.accordion.item` component show the heading and accordion content details of the accordion respectively.

Styling props like `color` are shared across many components.

You can find all the props for a component by checking its documentation page in the [component library](/docs/library/).

Reflex apps are organized into pages, each of which maps to a different URL.

Pages are defined as functions that return a component. By default, the function name will be used as the path, but you can also specify a route explicitly.

```python
def index():
    return rx.text("Root Page")

def about():
    return rx.text("About Page")

app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
```

In this example we add a page called `index` at the root route.
If you `reflex run` the app, you will see the `index` page at `http://localhost:3000`.
Similarly, the `about` page will be available at `http://localhost:3000/about`.

# Children
Text or other Reflex components nested inside a component. Passed as positional arguments.

# Props

Attributes that affect the behavior and appearance of a component.
Passed as keyword arguments.

Let's take a look at the `rx.text` component.

Hello World!

```python
rx.text("Hello World!", color="blue", font_size="1.5em")
```

Here `"Hello World!"` is the child text to display, while `color` and `font_size` are props that modify the appearance of the text.

Regular Python data types can be passed in as children to components. This is useful for passing in text, numbers, and other simple data types.

# Another Example

Now let's take a look at a more complex component, which has other components nested inside it. The `rx.vstack` component is a container that arranges its children vertically with space between them.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
  </div>
</div>

# Sample Form

Name: [Input Field]

Subscribe to Newsletter: [Checkbox]

```python
rx.vstack(
    rx.heading("Sample Form"),
    rx.input(placeholder="Name"),
    rx.checkbox("Subscribe to Newsletter"),
)
```

Some props are specific to a component. For example, the `header` and `content` props of the `rx.accordion.item` component show the heading and accordion content details of the accordion respectively.

Styling props like `color` are shared across many components.

You can find all the props for a component by checking its documentation page in the [component library](/docs/library/).

# Pages

Pages are organized into functions that return a component. By default, the function name will be used as the path, but you can also specify a route explicitly.

```python
def index():
    return rx.text("Root Page")

def about():
    return rx.text("About Page")

app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
```

In this example we add a page called `index` at the root route. If you `reflex run` the app, you will see the `index` page at `http://localhost:3000`. Similarly, the `about` page will be available at `http://localhost:3000/about`.