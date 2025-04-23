# Icon

The Icon component is used to display an icon from a library of icons. This implementation is based on the [Lucide Icons](https://lucide.dev/icons) where you can find a list of all available icons.

[View Icons List](https://reflex.dev/docs/library/data-display/icon/#icons-list)

# Icons List

![Link](/path/to/link.svg)

## Search icons...
Search icons...

<button>Show all (0)</button>

<a href="https://reflex.dev/docs/library/data-display/icon/#basic-example">More</a>

# Basic Example

To display an icon, specify the `tag` prop from the list of available icons.
Passing the tag as the first children is also supported and will be assigned to the `tag` prop.

The `tag` is expected to be in `snake_case` format, but `kebab-case` is also supported to allow copy-paste from [https://lucide.dev/icons](https://lucide.dev/icons).

```
rx.flex(
    rx.icon("calendar"),
    rx.icon(tag="calendar", gap="2"),
)
```

For more details, see the documentation on dynamic icons: [Dynamic Icons](https://reflex.dev/docs/library/data-display/icon/#dynamic-icons)

# Dynamic Icons

It is not possible to use dynamic values as the `tag` prop, because it is used to import the icon from the Lucide library. If you have a specific subset of icons you want to use dynamically, define an rx.match with them:

```python
def dynamic_icon(icon_name):
    return rx.match(
        icon_name,
        ("plus", rx.icon("plus")),
        ("minus", rx.icon("minus")),
        ("equal", rx.icon("equal")),
    )
```

You can then use the `dynamic_icon` function to display the icons dynamically.

<svg class="lucide lucide-plus css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg>
<svg class="lucide lucide-minus css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg>
<svg class="lucide lucide-equal css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg>

```python
rx.foreach(["plus", "minus", "equal"], dynamic_icon)
```

For more information, visit [Styling Icons](https://reflex.dev/docs/library/data-display/icon/#styling).

# Styling

Icon from Lucide can be customized with the following props `stroke_width`, `size` and `color`.

[View Documentation](https://reflex.dev/docs/library/data-display/icon/#stroke-width)

# Stroke Width

![](moon_icon.svg)

```python
rx.flex(
    rx.icon("moon", stroke_width=1),
    rx.icon("moon", stroke_width=1.5),
    rx.icon("moon", stroke_width=2),
    rx.icon("moon", stroke_width=2.5),
    gap="2",
)
```

[Link to Reflex Icon Documentation](https://reflex.dev/docs/library/data-display/icon/#size)

# Size

![zoom_in](/path/to/svg/zoom_in_15.svg)
![zoom_in](/path/to/svg/zoom_in_20.svg)
![zoom_in](/path/to/svg/zoom_in_25.svg)
![zoom_in](/path/to/svg/zoom_in_30.svg)

```python
rx.flex(
    rx.icon("zoom_in", size=15),
    rx.icon("zoom_in", size=20),
    rx.icon("zoom_in", size=25),
    rx.icon("zoom_in", size=30),
    align="center",
    gap="2",
)
```

[Copy Code](#)

It looks like you're working with examples of using the `rx.icon` function in Reflex to create a series of icons, each with different colors from a color palette. Here's a summary and explanation of what your code is doing:

### First Example: Using a Custom Color Palette

```python
rx.flex(
    rx.icon("zoom_in", size=18, color=rx.color("custom_color1")),
    rx.icon("zoom_in", size=18, color=rx.color("custom_color2")),
    # ... and so on for custom_color3 to custom_color12
)
```

- **`rx.flex`**: This function is used to arrange elements horizontally.
- **`rx.icon`**: This function creates an icon. The first argument is the name of the icon (e.g., "zoom_in").
- **`size=18`**: Sets the size of the icons to 18px.
- **`color=rx.color("custom_color1")`**: Uses a custom color from your color palette, specified by `"custom_color1"`.
- **`gap="2"`**: Adds space (2 units) between each icon.

### Second Example: Using the "accent" Color Palette

```python
rx.flex(
    rx.icon("zoom_in", size=18, color=rx.color("accent", 1)),
    rx.icon("zoom_in", size=18, color=rx.color("accent", 2)),
    # ... and so on for accent colors 3 to 12
)
```

- **`rx.flex`**: Arranges elements horizontally.
- **`rx.icon`**: Creates an icon with the specified icon name (`"zoom_in"`).
- **`size=18`**: Sets the size of the icons to 18px.
- **`color=rx.color("accent", n)`**: Uses colors from the "accent" color palette. The second argument (e.g., `1`, `2`, etc.) specifies which shade or tone of the accent color to use.

### Key Points

1. **Custom Colors vs. Palette Colors**:
   - In the first example, you're using a custom-defined color palette.
   - In the second example, you're using predefined "accent" colors from Reflex's built-in color scheme.

2. **Color Shading**:
   - The `rx.color` function allows you to specify different shades of a color by providing an additional argument (e.g., `1`, `2`, etc.). This can be useful for creating a gradient effect or simply varying the intensity of the colors.

3. **Flex Layout**:
   - `rx.flex` is used to arrange icons horizontally with a specified gap between them, ensuring they are neatly aligned and spaced out.

### Example Use Case

These examples could be used in various UI components where you need a series of consistent but slightly varied icons, such as in a navigation bar or a set of action buttons. The use of color palettes ensures that your design remains cohesive while still providing visual distinction between elements.

If you have any specific questions about the code or need further customization options, feel free to ask!

# Final Example

Icons can be used as child components of many other components. For example, adding a magnifying glass icon to a search bar.

```python
rx.badge(
    rx.flex(
        rx.icon("search", size=18),
        rx.text(
            "Search documentation...",
            size="3",
            weight="medium",
        ),
        direction="row",
        gap="1",
        align="center",
    ),
    size="2",
    radius="full",
    color_scheme="gray",
)
```

For more details, you can view the [API reference](https://reflex.dev/docs/library/data-display/icon/#api-reference).

# API Reference

[![Link](https://reflex.dev/docs/library/data-display/icon/#rx.lucide.icon)](https://reflex.dev/docs/library/data-display/icon/#rx.lucide.icon)

# rx.lucide.Icon

An Icon component.

## Prop

- **Prop**: `size`
- **Type | Values**: `int`
- **Default**: None

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)