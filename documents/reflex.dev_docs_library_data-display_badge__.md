# Badge

Badges are used to highlight an item's status for quick recognition.

[Basic Example](https://reflex.dev/docs/library/data-display/badge/)

# Basic Example

To create a badge component with only text inside, pass the text as an argument.

- **New**

```python
rx.badge("New")
```

[View Code]

# Styling

- **solid**
- **soft**
- **surface**
- **outline**
- **Accent**
  - England!
  - England!
  - England!
  - England!

- **Gray**
  - England!
  - England!
  - England!
  - England!

  - England!
  - England!
  - England!
  - England!

## tomato

- England!

<button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-surface rt-Button justify-between w-32">
  <p class="rt-Text font-small">tomato</p>
  <svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9">
    <path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path>
  </svg>
</button>

[Link to Reflex.dev](https://reflex.dev/docs/library/data-display/badge/#size)

# Size

The `size` prop controls the size and padding of a badge. It can take values of `"1" | "2"`, with default being `"1"`.

## Examples

- New
- New
- New

```python
rx.flex(
    rx.badge("New"),
    rx.badge("New", size="1"),
    rx.badge("New", size="2"),
    align="center",
    spacing="2",
)
```

Learn more about badge variants on the [Reflex.dev documentation](https://reflex.dev/docs/library/data-display/badge/#variant)

# Variant

The `variant` prop controls the visual style of the badge. The supported variant types are `"solid" | "soft" | "surface" | "outline"`. The variant default is `"soft"`.

## Examples

- Solid: New
- Soft: New
- Soft: New
- Surface: New
- Outline: New

```python
rx.flex(
    rx.badge("New", variant="solid"),
    rx.badge("New", variant="soft"),
    rx.badge("New"),
    rx.badge("New", variant="surface"),
    rx.badge("New", variant="outline"),
    spacing="2",
)
```

For more details, see the [color scheme documentation](https://reflex.dev/docs/library/data-display/badge/#color-scheme).

# Color Scheme

The `color_scheme` prop sets a specific color, ignoring the global theme.

## Badges

New | New | New | New

```python
rx.flex(
    rx.badge("New", color_scheme="indigo"),
    rx.badge("New", color_scheme="cyan"),
    rx.badge("New", color_scheme="orange"),
    rx.badge("New", color_scheme="crimson"),
    spacing="2",
)
```

[View Documentation](https://reflex.dev/docs/library/data-display/badge/#high-contrast)

# High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python
rx.flex(
    rx.flex(
        rx.badge("New", variant="solid"),
        rx.badge("New", variant="soft"),
        rx.badge("New", variant="surface"),
        rx.badge("New", variant="outline"), 
        spacing="2",
    ),
    rx.flex(
        rx.badge("New", variant="solid", high_contrast=True),
        rx.badge("New", variant="soft", high_contrast=True),
        rx.badge("New", variant="surface", high_contrast=True),
        rx.badge("New", variant="outline", high_contrast=True), 
        spacing="2",
    ),
    direction="column",
    spacing="2",
)
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/data-display/badge/#radius">

# Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none" | "small" | "medium" | "large" | "full"`.

- New (radius: none)
- New (radius: small)
- New (radius: medium)
- New (radius: large)
- New (radius: full)

```python
rx.flex(
    rx.badge("New", radius="none"),
    rx.badge("New", radius="small"),
    rx.badge("New", radius="medium"),
    rx.badge("New", radius="large"),
    rx.badge("New", radius="full"),
    spacing="3",
)
```

# Final Example

A badge may contain more complex elements within it. This example uses a `flex` component to align an icon and the text correctly, using the `gap` prop to ensure a comfortable spacing between the two.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <span class="rt-reset rt-Badge rt-r-size-1 rt-variant-soft" data-accent-color="grass">
            <div class="rt-Flex rt-r-gap-1">
                <svg class="lucide lucide-arrow-up css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24">
                    <path d="m5 12 7-7 7 7"></path>
                    <path d="M12 19V5"></path>
                </svg>
                <p class="rt-Text">8.8%</p>
            </div>
        </span>
    </div>
    <div class="rt-Box relative mb-4">
        <div class="rt-Box code-block css-1islnds">
            <pre class="shiki one-dark-pro" style="background-color:#282c34;color:#abb2bf" tabindex="0"><code>rx.badge(
    rx.flex(
        rx.icon(tag="arrow_up"),
        rx.text("8.8%"),
        spacing="1",
    ),
    color_scheme="grass",
)</code></pre>
            <button class="css-kobh7h">
                <svg class="lucide lucide-copy css-cqk0y8" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16">
                    <rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect>
                    <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>
                </svg>
            </button>
        </div>
    </div>
</div>

[Link to API Reference](https://reflex.dev/docs/library/data-display/badge/#api-reference)

# API Reference

[![Link](https://example.com/link)](https://reflex.dev/docs/library/data-display/badge/#rx.badge)

# rx.badge

A stylized badge element.

## Basic Badge

```html
<span class="rt-reset rt-Badge rt-r-size-1 rt-variant-solid" data-accent-color="tomato" data-radius="none">Basic Badge</span>
```

### Properties

| Prop       | Type | Values          | Default | Interactive |
|------------|------|-----------------|---------|------------|
| variant    |      | "solid" | "soft" | ...        | -           |
| size       |      | "1"   | "2"   | ...        | 1           |
| color_scheme|       | "tomato" | "red" | ...        | tomato      |
| high_contrast|    | bool            |         | false      |
| radius     |      | "none" | "small"| ...        | none        |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)