# Blockquote

Perfect typography is certainly the most elusive of all arts.

```python
rx.blockquote("Perfect typography is certainly the most elusive of all arts.")
```

[![Copy Code](https://user-images.githubusercontent.com/76249183/210528275-d1cfe8a1-2e22-4dcd-bb4f-e10e8ce47f24.svg)](https://reflex.dev/docs/library/typography/blockquote/#size)

# Size

Use the `size` prop to control the size of the blockquote. The prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.

```python
rx.flex(
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="1"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="2"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="3"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="4"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="5"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="6"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="7"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="8"),
    rx.blockquote("Perfect typography is certainly the most elusive of all arts.", size="9"),
)
```

# Weight

Use the `weight` prop to set the blockquote weight.

## Examples

```python
rx.flex(
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        weight="light",
    ),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        weight="regular",
    ),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        weight="medium",
    ),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        weight="bold",
    ),
)
```

For more details, see [Reflex.dev documentation](https://reflex.dev/docs/library/typography/blockquote/#color)

# Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

*Perfect typography is certainly the most elusive of all arts.*

- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts.
- Perfect typography is certainly the most elusive of all arts

```python
rx.flex(
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        color_scheme="indigo",
    ),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        color_scheme="cyan",
    ),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        color_scheme="crimson",
    ),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        color_scheme="orange",
    ),
    direction="column",
    spacing="3",
)
```

# High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

<div class="py-4 gap-4 flex flex-col w-full">
    <div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <blockquote>Perfect typography is certainly the most elusive of all arts.</blockquote>
        <blockquote class="rt-high-contrast">Perfect typography is certainly the most elusive of all arts.</blockquote>
    </div>
</div>

<div class="relative mb-4">
    <pre class="shiki one-dark-pro" style="background-color:#282c34;color:#abb2bf" tabindex="0">
```python
rx.flex(
    rx.blockquote("Perfect typography is certainly the most elusive of all arts."),
    rx.blockquote(
        "Perfect typography is certainly the most elusive of all arts.",
        high_contrast=True,
    ),
    direction="column",
    spacing="3",
)
```
</pre>
<button><svg class="lucide lucide-copy" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg></button>
</div>

<a class="rt-reset rt-link flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors" href="https://reflex.dev/docs/library/typography/blockquote/#api-reference">Link</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/typography/blockquote/#rx.blockquote)

# rx.blockquote

A block level extended quotation.

## Test

```python
size: "1" | "2"
weight: "light" | "regular"
color_scheme: "tomato" | "red"
high_contrast: bool
cite: str
```

- size: Can be one of the values `"1"`, `"2"`, etc.
- weight: Can be one of the values `"light"`, `"regular"`, etc.
- color_scheme: Can be one of the values `"tomato"`, `"red"`, etc.
- high_contrast: A boolean value.
- cite: A string.

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)