# Heading

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full"></div>
</div>

`<rx:Heading>` is a component in the Reflex library, which is used for creating headings or titles in web applications. It's part of the reactive and declarative programming model that Reflex offers to build dynamic user interfaces.

Here are some key points about `<rx:Heading>` based on the provided information:

1. **Customization**: You can customize various aspects of a heading such as size, weight, alignment, trimming, color scheme, etc.
2. **Size and Weight**: The component allows you to specify different sizes (like `light`, `regular`) and weights (like `thin`, `normal`, `bold`).
3. **Alignment**: You can align the text within the heading to the left, center, or right.
4. **Trimming**: Controls how extra spaces are handled in the text.
5. **Color Scheme**: Allows setting a color for the heading from predefined color schemes or custom colors.
6. **High Contrast Mode**: An option to switch to high contrast mode for better readability.

The provided example demonstrates using `<rx:Heading>` with different parameters:

```jsx
<rx:Heading weight="bold" size="3">Hello World</rx:Heading>
```

This creates a bold and large heading saying "Hello World".

For more detailed usage, you can refer to the official Reflex documentation or the specific component's API reference.

# As another element

Use the `as_` prop to change the heading level. This prop is purely semantic and does not change the visual appearance.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
    </div>
</div>

# Level 1

# Level 2

```python
rx.flex(
    rx.heading("Level 1", as_="h1"),
    rx.heading("Level 2", as_="h2"),
    rx.heading("Level 3", as_="h3"),
    direction="column",
    spacing="3"
)
```

- Level 1
- Level 2
- Level 3

# Size

Use the `size` prop to control the size of the heading. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
  </div>
</div>

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", size="1"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="2"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="3"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="4"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="5"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="6"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="7"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="8"),
    rx.heading("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    spacing="3",
)
```

[View Documentation](https://reflex.dev/docs/library/typography/heading/#weight)

# Weight

Use the `weight` prop to set the text weight.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
  </div>
</div>

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="light"),
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="regular"),
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="medium"),
    rx.heading("The quick brown fox jumps over the lazy dog.", weight="bold"),
    direction="column",
    spacing="3",
)
```

# Align

Use the `align` prop to set text alignment.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-gap-3 css-8atqhb"></div>
  </div>
</div>

# Left-aligned

# Center-aligned

```python
rx.flex(
    rx.heading("Left-aligned", align="left"),
    rx.heading("Center-aligned", align="center"),
    rx.heading("Right-aligned", align="right"),
    direction="column",
    spacing="3",
    width="100%",
)
```

[![Copy](https://reflex.dev/docs/library/typography/heading/assets/copy.svg)](https://reflex.dev/docs/library/typography/heading/#trim)

# Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the text.

<div>
<div>

# Without Trim

# With Trim

Without Trim
```
rx.heading(
    "Without Trim",
    trim="normal",
    style={
        "background": "var(--gray-a2)",
        "border_top": "1px dashed var(--gray-a7)",
        "border_bottom": "1px dashed var(--gray-a7)",
    },
)
rx.heading(
    "With Trim",
    trim="both",
    style={
        "background": "var(--gray-a2)",
        "border_top": "1px dashed var(--gray-a7)",
        "border_bottom": "1px dashed var(--gray-a7)",
    },
)
direction="column",
spacing="3",
)
```

With Trim
```
rx.heading(
    "Without Trim",
    trim="normal",
    style={
        "background": "var(--gray-a2)",
        "border_top": "1px dashed var(--gray-a7)",
        "border_bottom": "1px dashed var(--gray-a7)",
    },
)
rx.heading(
    "With Trim",
    trim="both",
    style={
        "background": "var(--gray-a2)",
        "border_top": "1px dashed var(--gray-a7)",
        "border_bottom": "1px dashed var(--gray-a7)",
    },
)
direction="column",
spacing="3",
)
```

Trimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.

# Without trim
The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant.

# Without trim
The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant.

# With trim
The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant.

# Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column"></div>
  </div>
</div>

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column"
)
```

[High Contrast](https://reflex.dev/docs/library/typography/heading/#high-contrast)

# High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python
high_contrast
```

<div>
  <div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <!-- Content within this div will be listed here -->
  </div>
</div>

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

# The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="indigo", high_contrast=True),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="cyan", high_contrast=True),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="crimson", high_contrast=True),
    rx.heading("The quick brown fox jumps over the lazy dog.", color_scheme="orange", high_contrast=True),
    direction="column"
)
```

[Link to API reference](https://reflex.dev/docs/library/typography/heading/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/typography/heading/#rx.heading)

# rx.heading
A foundational text primitive based on the element.

<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
</div>
</div>

# Test

## Prop | Type | Default | Interactive
- `as_child` | bool |
- `as_` | str |
- `size` | "1" | "2" | ... | 1
- `weight` | "light" | "regular" | ... | light
- `align` | "left" | "center" | ... | left
- `trim` | "normal" | "start" | ... | normal
- `color_scheme` | "tomato" | "red" | ... | tomato
- `high_contrast` | bool | false

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)