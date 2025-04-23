# Card
A Card component is used for grouping related components. It is similar to the Box, except it has a border, uses the theme colors and border radius, and provides a `size` prop to control spacing and margin according to the Radix "1" - "5" scale.

The Card requires less styling than a Box to achieve consistent visual results when used with themes.

[Basic Example](https://reflex.dev/docs/library/layout/card/#basic-example)

# Basic Example

Card 1
Card 2
Card 3
Card 4
Card 5

```python
rx.flex(
    rx.card("Card 1", size="1"),
    rx.card("Card 2", size="2"),
    rx.card("Card 3", size="3"),
    rx.card("Card 4", size="4"),
    rx.card("Card 5", size="5"),
    spacing="2",
    align_items="flex-start",
    flex_wrap="wrap",
)
```

# Rendering as a Different Element

The `as_child` prop may be used to render the Card as a different element. Link and Button are commonly used to make a Card clickable.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <a class="rt-Text rt-reset rt-Link rt-underline-auto rt-reset rt-BaseCard rt-Card rt-r-size-1 rt-variant-surface css-1macts" href="#">
            <div class="rt-Flex rt-r-gap-2">
                <span class="rt-reset rt-AvatarRoot rt-r-size-3 rt-variant-soft">
                    <img class="rt-AvatarImage" src="/reflex_banner.png"/>
                </span>
                <div class="rt-Box"></div>
            </div>
        </a>
    </div>
</div>

# Quick Start

Get started with Reflex in 5 minutes.

```python
rx.card(
    rx.link(
        rx.flex(
            rx.avatar(src="/reflex_banner.png"),
            rx.box(
                rx.heading("Quick Start"),
                rx.text("Get started with Reflex in 5 minutes.")
            ),
            spacing="2"
        ),
        as_child=True,
    )
)
```

# Using Inset Content

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/layout/card/#api-reference">

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/card/#rx.card)

# rx.card

Container that groups related content and actions.

## Basic Card

```python
Basic Card 
```

### Props

| Prop          | Type | Default | Interactive |
|---------------|------|---------|------------|
| as_child      | bool |         |            |
| size          | "1" | "2" | ...       | 1        |
| variant       | "surface" | "classic" | ...     | surface |

---

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)