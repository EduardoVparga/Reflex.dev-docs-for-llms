# Box

Box is a generic container component that can be used to group other components.

By default, the Box component is based on the `<code>div</code>` and rendered as a block element. It's primary use is for applying styles.

[View Basic Example](https://reflex.dev/docs/library/layout/box/#basic-example)

# Basic Example

![Link](https://example.com/link_icon.svg)

```python
rx.box(
    rx.box(
        "CSS color",
        background_color="yellow",
        border_radius="2px",
        width="20%",
        margin="4px",
        padding="4px",
    ),
    rx.box(
        "CSS color",
        background_color="orange",
        border_radius="5px",
        width="40%",
        margin="8px",
        padding="8px",
    ),
    rx.box(
        "Radix Color",
        background_color="var(--tomato-3)",
        border_radius="5px",
        width="60%",
        margin="12px",
        padding="12px",
    ),
    rx.box(
        "Radix Color",
        background_color="var(--plum-3)",
        border_radius="10px",
        width="80%",
        margin="16px",
        padding="16px",
    ),
    rx.box(
        "Radix Theme Color",
        background_color="var(--accent-2)",
        radius="full",
        width="100%",
        margin="24px",
        padding="25px",
    ),
    flex_grow="1",
    text_align="center",
)
```

[Learn more about the `rx.box` component](https://reflex.dev/docs/library/layout/box/#background)

# Background

To set a background image or gradient, use the `background` CSS prop.

```python
rx.flex(
    rx.box(
        background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))",
        width="20%",
        height="100%",
    ),
    rx.box(
        background="linear-gradient(red, yellow, blue, orange)",
        width="20%",
        height="100%",
    ),
    rx.box(
        background="radial-gradient(at 0% 30%, red 10px, yellow 30%, #1e90ff 50%)",
        width="20%",
        height="100%",
    ),
    rx.box(
        background="center/cover url('/reflex_banner.png')",
        width="20%",
        height="100%",
    ),
    spacing="2",
    width="100%",
    height="10vh",
)
```

For more details, see the [documentation](https://reflex.dev/docs/library/layout/box/#api-reference).

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/box/#rx.box)

# rx.box

A fundamental layout building block, based on `div` element.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)