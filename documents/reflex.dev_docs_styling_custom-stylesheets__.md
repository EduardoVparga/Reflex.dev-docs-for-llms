# Custom Stylesheets

Reflex allows you to add custom stylesheets. Simply pass the URLs of the stylesheets to `rx.App`:

```python
app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)
```

[Learn More](https://reflex.dev/docs/styling/custom-stylesheets/#local-stylesheets)

# Local Stylesheets

You can also add local stylesheets. Just put the stylesheet under `assets/` and pass the path to the stylesheet to `rx.App`:

```python
app = rx.App(
    stylesheets=[
        "/styles.css",  # This path is relative to assets/
    ],
)
```

<div data-orientation="vertical" data-variant="classic">
<div class="AccordionItem" data-orientation="vertical" data-state="closed"></div>
</div>

Always use a leading slash (/) when referencing files in the assets directory.

# Styling with CSS

You can use CSS variables directly in your Reflex app by passing them alongside the appropriate props. Create a `style.css` file inside the `assets` folder with the following lines:

```python
:root {
    --primary-color: blue;
    --accent-color: green;
}
```

Then, after referencing the CSS file within the `stylesheets` props of `rx.App`, you can access the CSS props directly like this

```python
app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["/style.css"],
)
app.add_page(
    rx.center(
        rx.text("CSS Variables!"),
        width="100%",
        height="100vh",
        bg="var(--primary-color)",
    ),
    "/"
)
```

[Learn more about custom stylesheets](https://reflex.dev/docs/styling/custom-stylesheets/#fonts)

# Fonts

You can take advantage of Reflex's support for custom stylesheets to add custom fonts to your app.

In this example, we will use the [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) font from Google Fonts. First, add the stylesheet with the font to your app. You can get this link from the "Get embed code" section of the Google font page.

```python
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)
```

Then you can use the font in your component by setting the `font_family` prop.

Check out my font

```python
rx.text(
    "Check out my font",
    font_family="IBM Plex Mono",
    font_size="1.5em",
)
```

[Learn more about local fonts in Reflex](https://reflex.dev/docs/styling/custom-stylesheets/#local-fonts)

# Local Fonts

By making use of the two previous points, we can also make a stylesheet that allows you to use a font hosted on your server.

If your font is called `MyFont.otf`, copy it in `assets/fonts`.

Now we have the font ready, let's create the stylesheet `myfont.css`.

```css
@font-face {
    font-family: MyFont;
    src: url("/fonts/MyFont.otf") format("opentype");
}

@font-face {
    font-family: MyFont;
    font-weight: bold;
    src: url("/fonts/MyFont.otf") format("opentype");
}
```

Add the reference to your new Stylesheet in your App.

```python
app = rx.App(
    stylesheets=[
        "/fonts/myfont.css",  # This path is relative to assets/
    ],
)
```

And that's it! You can now use `MyFont` like any other FontFamily to style your components.