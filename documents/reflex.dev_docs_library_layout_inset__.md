# Inset

Applies a negative margin to allow content to bleed into the surrounding container.

[Basic Example](https://reflex.dev/docs/library/layout/inset/#basic-example)

# Basic Example

Nesting an Inset component inside a Card will render the content from edge to edge of the card.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Inset rt-r-side-top rt-r-clip-border-box rt-r-pb-inset">
      <img class="css-ducv57" src="/reflex_banner.png"/>
    </div>
    <p class="rt-Text">Reflex is a web framework that allows developers to build their app in pure Python.</p>
  </div>
</div>

```python
rx.card(
    rx.inset(
        rx.image(
            src="/reflex_banner.png",
            width="100%",
            height="auto"
        ),
        side="top",
        pb="current"
    ),
    rx.text(
        "Reflex is a web framework that allows developers to build their app in pure Python."
    ),
    width="25vw"
)
```

[Link](https://reflex.dev/docs/library/layout/inset/#other-directions)

# Other Directions

The `side` prop controls which side the negative margin is applied to. When using a specific side, it is helpful to set the padding for the opposite side to `current` to retain the same padding the content would have had if it went to the edge of the parent component.

## Inset with Bottom Side
The inset below uses a bottom side.
```python
rx.card(
    rx.text("The inset below uses a bottom side."),
    rx.inset(
        rx.image(src="/reflex_banner.png"),
        side="bottom",
        pt="current"
    ),
    width="25vw"
)
```

## Inset with Right Side
This inset uses a right side, which requires a flex with direction row.
```python
rx.card(
    rx.flex(
        rx.text("This inset uses a right side, which requires a flex with direction row."),
        rx.inset(
            rx.box(background="center/cover url('/reflex_banner.png')", height="100%"),
            width="100%",
            side="right",
            pl="current"
        ),
        direction="row",
        width="100%"
    ),
    width="25vw"
)
```

## Inset with Left Side
This inset uses a left side, which also requires a flex with direction row.
```python
rx.card(
    rx.flex(
        rx.inset(
            rx.box(background="center/cover url('/reflex_banner.png')", height="100%"),
            width="100%",
            side="left",
            pr="current"
        ),
        rx.text("This inset uses a left side, which also requires a flex with direction row."),
        direction="row",
        width="100%"
    ),
    width="25vw"
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/inset/#rx.inset)

# rx.inset

Applies a negative margin to allow content to bleed into the surrounding container.

## Properties

Prop | Type | Values | Default | Interactive
--- | --- | --- | --- | ---
side | `"x" | "y" | ...` |  |  |
clip | `"border-box" | "padding-box"` |  |  |
p | `Union[int, str]` |  | 
px | `Union[int, str]` |  | 
py | `Union[int, str]` |  | 
pt | `Union[int, str]` |  | 
pr | `Union[int, str]` |  | 
pb | `Union[int, str]` |  | 
pl | `Union[int, str]` |  |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)