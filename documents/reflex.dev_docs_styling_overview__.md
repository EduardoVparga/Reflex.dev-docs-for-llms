# Styling
Reflex components can be styled using the full power of CSS.

There are three main ways to add style to your app and they take precedence in the following order:

- Inline: Styles applied to a single component instance.
- Component: Styles applied to components of a specific type.
- Global: Styles applied to all components.

# Style keys can be any valid CSS property name.

Style keys can be any valid CSS property name.

# Global Styles

You can pass a style dictionary to your app to apply base styles to all components.

For example, you can set the default font family and font size for your app here just once rather than having to set it on every component.

```python
style = {
    "font_family": "Comic Sans MS",
    "font_size": "16px",
}

app = rx.App(style=style)
```

[Copy Code](#)

# Component Styles

In your style dictionary, you can also specify default styles for specific component types or arbitrary CSS classes and IDs.

```python
style = {
    # Set the selection highlight color globally.
    "::selection": {
        "background_color": accent_color,
    },
    # Apply global css class styles.
    ".some-css-class": {
        "text_decoration": "underline",
    },
    # Apply global css id styles.
    "#special-input": {"width": "20vw"},
    # Apply styles to specific components.
    rx.text: {
        "font_family": "Comic Sans MS",
    },
    rx.divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.heading: {
        "font_weight": "500",
    },
    rx.code: {
        "color": "green",
    },
}

app = rx.App(style=style)
```

Using style dictionaries like this, you can easily create a consistent theme for your app.

<div class="AccordionItem" data-orientation="vertical" data-state="closed"></div>

# Watch out for underscores in class names and IDs

## Note
Watch out for underscores in class names and IDs

# Inline Styles

Inline styles apply to a single component instance. They are passed in as regular props to the component.

Hello World

```python
rx.text(
    "Hello World",
    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
    background_clip="text",
    font_weight="bold",
    font_size="2em",
)
```

Children components inherit inline styles unless they are overridden by their own inline styles.

Default Button
Red Button

```python
rx.box(
    rx.hstack(
        rx.button("Default Button"),
        rx.button("Red Button", color="red"),
    ),
    color="blue",
)
```

# Style Prop

Inline styles can also be set with a `style` prop. This is useful for reusing styles between multiple components.

```python
text_style = {
    "color": "green",
    "font_family": "Comic Sans MS",
    "font_size": "1.2em",
    "font_weight": "bold",
    "box_shadow": "rgba(240, 46, 170, 0.4) 5px 5px, rgba(240, 46, 170, 0.3) 10px 10px"
}
```

```python
rx.vstack(
    rx.text("Hello", style=text_style),
    rx.text("World", style=text_style)
)
```

---

```python
style1 = {
    "color": "green",
    "font_family": "Comic Sans MS",
    "border_radius": "10px",
    "background_color": "rgb(107,99,246)"
}
style2 = {
    "color": "white",
    "border": "5px solid #EE756A",
    "padding": "10px"
}
```

```python
rx.box(
    "Multiple Styles",
    style=[style1, style2]
)
```

The style dictionaries are applied in the order they are passed in. This means that styles defined later will override styles defined earlier.

[Reflex.dev Docs: Theming](https://reflex.dev/docs/styling/overview/#theming)

# Theming

As of Reflex 'v0.4.0', you can now theme your Reflex web apps. To learn more checkout the [Theme docs](/docs/styling/theming/).

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in your rx.App.

```python
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
```

Additionally you can modify the theme of your app through using the `Theme Panel` component which can be found in the [Theme Panel docs](/docs/library/other/theme/).

# Special Styles

We support all of Chakra UI's [pseudo styles](https://v2.chakra-ui.com/docs/styled-system/style-props#pseudo).

Below is an example of text that changes color when you hover over it.

Hover Me

```python
rx.box(
    rx.text("Hover Me", _hover={"color": "red"}),
)
```

![](data:image/svg+xml;utf8,<svg class="lucide lucide-copy css-cqk0y8" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg>)