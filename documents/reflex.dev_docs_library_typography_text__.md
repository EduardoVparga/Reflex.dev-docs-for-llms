# Text

The quick brown fox jumps over the lazy dog.

rx.text("The quick brown fox jumps over the lazy dog")

![](link_to_image)

[Read more about text as another element](https://reflex.dev/docs/library/typography/text/#as-another-element)

# As another element

Use the `as_` prop to render text as a `p`, `label`, `div` or `span`. This prop is purely semantic and does not alter visual appearance.

This is a **paragraph** element.
This is a **label** element.
This is a **div** element.
This is a **span** element.

```python
rx.flex(
    rx.text(
        "This is a ",
        rx.text.strong("paragraph"),
        " element.",
        as_="p",
    ),
    rx.text(
        "This is a ",
        rx.text.strong("label"),
        " element.",
        as_="label",
    ),
    rx.text(
        "This is a ",
        rx.text.strong("div"),
        " element.",
        as_="div",
    ),
    rx.text(
        "This is a ",
        rx.text.strong("span"),
        " element.",
        as_="span",
    ),
    direction="column",
    spacing="3",
)
```

# Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.text("The quick brown fox jumps over the lazy dog.", size="1"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="2"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="3"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="4"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="5"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="6"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="7"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="8"),
    rx.text("The quick brown fox jumps over the lazy dog.", size="9"),
    direction="column",
    spacing="3",
)
```

Sizes 2–4 are designed to work well for long-form content. Sizes 1–3 are designed to work well for UI labels.

Learn more about text weight [here](https://reflex.dev/docs/library/typography/text/#weight).

# Weight

Use the `weight` prop to set the text weight.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        weight="light",
        as_="div",
    ),
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        weight="regular",
        as_="div",
    ),
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        weight="medium",
        as_="div",
    ),
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        weight="bold",
        as_="div",
    ),
    direction="column",
    spacing="3",
)
```

# Align

Use the `align` prop to set text alignment.

- Left-aligned: rx.flex(rx.text("Left-aligned", align="left", as_="div"))
- Center-aligned: rx.text("Center-aligned", align="center", as_="div")
- Right-aligned: rx.text("Right-aligned", align="right", as_="div")

```python
rx.flex(
    rx.text("Left-aligned", align="left", as_="div"),
    rx.text("Center-aligned", align="center", as_="div"),
    rx.text("Right-aligned", align="right", as_="div"),
    direction="column",
    spacing="3",
    width="100%",
)
```

# Trim

Use the `trim` prop to trim the leading space at the start, end, or both sides of the text box.

Without Trim
With Trim

```python
rx.flex(
    rx.text(
        "Without Trim",
        trim="normal",
        style={
            "background": "var(--gray-a2)",
            "border_top": "1px dashed var(--gray-a7)",
            "border_bottom": "1px dashed var(--gray-a7)",
        },
    ),
    rx.text(
        "With Trim",
        trim="both",
        style={
            "background": "var(--gray-a2)",
            "border_top": "1px dashed var(--gray-a7)",
            "border_bottom": "1px dashed var(--gray-a7)",
        },
    ),
    direction="column",
    spacing="3",
)
```

Trimming the leading is useful when dialing in vertical spacing in cards or other “boxy” components. Otherwise, padding looks larger on top and bottom than on the sides.

# Without trim

The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant.

# Without trim

The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant.

---

# With trim

The goal of typography is to relate font size, line height, and line width in a proportional way that maximizes beauty and makes reading easier and more pleasant.

# Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="indigo"),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="cyan"),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="crimson"),
    rx.text("The quick brown fox jumps over the lazy dog.", color_scheme="orange"),
    direction="column",
)
```

For more information, see [High Contrast Text](https://reflex.dev/docs/library/typography/text/#high-contrast) in the documentation.

# High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

```python
rx.flex(
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="indigo",
        high_contrast=True,
    ),
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="cyan",
        high_contrast=True,
    ),
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="crimson",
        high_contrast=True,
    ),
    rx.text(
        "The quick brown fox jumps over the lazy dog.",
        color_scheme="orange",
        high_contrast=True,
    ),
    direction="column"
)
```

![Copy](https://reflex.dev/docs/library/typography/text/#with-formatting)

# With formatting

Compose `Text` with formatting components to add emphasis and structure to content.

Look, such a helpful [link](/docs/library/typography/text/#), an *italic emphasis* a piece of computer `code`, and even a hotkey combination **⇧⌘A** within the text.

rx.text(
    "Look, such a helpful ",
    rx.link("link", href="#"),
    ", an ",
    rx.text.em("italic emphasis"),
    " a piece of computer ",
    rx.code("code"),
    ", and even a hotkey combination ",
    rx.text.kbd("⇧⌘A"),
    " within the text.",
    size="5",
)

[More details](https://reflex.dev/docs/library/typography/text/#preformmatting)

# Preformmatting

By Default, the browser renders multiple white spaces into one. To preserve whitespace, use the `white_space = "pre"` css prop.

This is not pre     formatted
This is pre     formatted

```python
rx.hstack(
    rx.text("This is not pre     formatted"),
    rx.text("This is pre     formatted", white_space="pre"),
)
```

For more information, see [Text with Form Controls](https://reflex.dev/docs/library/typography/text/#with-form-controls)

# With form controls

Composing `text` with a form control like `checkbox`, `radiogroup`, or `switch` automatically centers the control with the first line of text, even when the text is multi-line.

## Text Input Example

- **Checkbox:**
  - I understand that these documents are confidential and cannot be shared with a third party.

```python
rx.box(
    rx.text(
        rx.flex(
            rx.checkbox(default_checked=True),
            "I understand that these documents are confidential and cannot be shared with a third party.",
        ),
        as_="label",
        size="3",
    ),
    style={"max_width": 300},
)
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/typography/text/#api-reference">Learn more</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/typography/text/#rx.text)

# rx.text

A foundational text primitive based on the `<span>` element.

## Properties

- **as_child**: `bool`
- **as_**: `"p" | "label" | ...` (Default: `Var.create("p")`)
- **size**: `"1" | "2" | ..." `
- **weight**: `"light" | "regular" | ..." `
- **align**: `"left" | "center" | ..." `
- **trim**: `"normal" | "start" | ..." `
- **color_scheme**: `"tomato" | "red" | ..." `

  Default: `tomato`

- **high_contrast**: `bool` (Default: `false`)

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.text.em
Marks text to stress emphasis.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)