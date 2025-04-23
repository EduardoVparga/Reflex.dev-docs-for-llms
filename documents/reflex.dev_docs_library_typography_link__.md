# Link

Links are accessible elements used primarily for navigation. Use the `href` prop to specify the location for the link to navigate to.

- **Reflex Home Page.**
  [Reflex Home Page.](https://reflex.dev/)

```python
rx.link("Reflex Home Page.", href="https://reflex.dev/")
```

You can also provide local links to other pages in your project without writing the full URL.

- Example
  [Example](/docs/library/)

```python
rx.link(
    "Example",
    href="/docs/library"
)
```

The `link` component can be used to wrap other components to make them link to other pages.

- **Example**
  [Example](https://reflex.dev/)

```python
rx.link(rx.button("Example"), href="https://reflex.dev/")
```

You can also create anchors to link to specific parts of a page using the `id` prop.

- Example

```python
rx.box("Example", id="example")
```

To reference an anchor, you can use the `href` prop of the `link` component. The `href` should be in the format of the page you want to link to followed by a # and the id of the anchor.

- Example

[Example](/docs/library/typography/link/#example)

```python
rx.link(
    "Example",
    href="/docs/library/typography/link#example"
)
```

```html
<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
  <div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed"></div>
</div>
```

# Redirecting the user using State

## Description

This section describes how to redirect a user using state in Reflex. The content is currently hidden and can be expanded by clicking on the header.

- Clicking on the header will expand or collapse this section.
- The icon changes from a downward arrow to an upward arrow when expanded.

# Style

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/typography/link/#size"></a>

# Size

Use the `size` prop to control the size of the link. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

- **Size 1**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 2**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 3**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 4**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 5**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 6**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 7**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 8**
  - [The quick brown fox jumps over the lazy dog.](#)
- **Size 9**
  - [The quick brown fox jumps over the lazy dog.](#)

```python
rx.flex(
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="1",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="2",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="3",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="4",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="5",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="6",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="7",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="8",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        size="9",
    ),
    direction="column",
    spacing="3",
)
```

# Weight

Use the `weight` prop to set the text weight.

## Examples

The quick brown fox jumps over the lazy dog. (light)

The quick brown fox jumps over the lazy dog. (regular)

The quick brown fox jumps over the lazy dog. (medium)

The quick brown fox jumps over the lazy dog. (bold)

```python
rx.flex(
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        weight="light",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        weight="regular",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        weight="medium",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        weight="bold",
    ),
    direction="column",
    spacing="3",
)
```

# Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the rendered text.

[Without Trim](#)
[With Trim](#)

```python
rx.flex(
    rx.link(
        "Without Trim",
        trim="normal",
        style={
            "background": "var(--gray-a2)",
            "border_top": "1px dashed var(--gray-a7)",
            "border_bottom": "1px dashed var(--gray-a7)"
        }
    ),
    rx.link(
        "With Trim",
        trim="both",
        style={
            "background": "var(--gray-a2)",
            "border_top": "1px dashed var(--gray-a7)",
            "border_bottom": "1px dashed var(--gray-a7)"
        }
    ),
    direction="column",
    spacing="3"
)
```

# Underline

Use the `underline` prop to manage the visibility of the underline affordance. It defaults to `auto`.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        underline="auto",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        underline="hover",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        underline="always",
    ),
    direction="column",
    spacing="3",
)
```

[Link to documentation](https://reflex.dev/docs/library/typography/link/#color)

# Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="indigo",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="cyan",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="crimson",
    ),
    rx.link(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="orange",
    ),
    direction="column"
)
```

[More information](https://reflex.dev/docs/library/typography/link/#high-contrast)

# High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.link("The quick brown fox jumps over the lazy dog"),
    rx.link(
        "The quick brown fox jumps over the lazy dog",
        high_contrast=True,
    ),
    direction="column",
)
```

[![Copy Code](https://via.placeholder.com/32x32)](javascript:void(0))

# API Reference

[API Reference](https://reflex.dev/docs/library/typography/link/#rx.link)

# rx.link

A semantic element for navigation between pages.

## Example Link
[Test](#)

## Properties

- **as_child**: `bool` - 
- **size**: `"1" | "2" | ...` - 
- **weight**: `"light" | "regular" | ...` - Default: `light`
- **trim**: `"normal" | "start" | ...` - Default: `normal`
- **underline**: `"auto" | "hover" | ...` - Default: `auto`
- **color_scheme**: `"tomato" | "red" | ..."` - Default: `tomato`

### High Contrast
Default: `false`

### Is External
Default: `false`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)