# Hovercard

The `hover_card.root` contains all the parts of a hover card.

The `hover_card.trigger` wraps the link that will open the hover card.

The `hover_card.content` contains the content of the open hover card.

Hover over the text to see the tooltip. [Hover over me](#)

```python
rx.text(
    "Hover over the text to see the tooltip.",
    rx.hover_card.root(
        rx.hover_card.trigger(
            rx.link("Hover over me", color_scheme="blue", underline="always"),
        ),
        rx.hover_card.content(rx.text("This is the hovercard content.")),
    ),
)
```

---

Hover over the text to see the tooltip. [Hover over me](#)

```python
rx.text(
    "Hover over the text to see the tooltip.",
    rx.hover_card.root(
        rx.hover_card.trigger(
            rx.link("Hover over me", color_scheme="blue", underline="always"),
        ),
        rx.hover_card.content(
            rx.grid(
                rx.inset(
                    side="left",
                    pr="current",
                    background="url('https://images.unsplash.com/5/unsplash-kitsune-4.jpg') center/cover",
                    height="full",
                ),
                rx.box(
                    rx.text_area(placeholder="Write a comment…", style={"height": 80}),
                    rx.flex(
                        rx.checkbox("Send to group"),
                        spacing="3",
                        margin_top="12px",
                        justify="between",
                    ),
                    padding_left="12px",
                ),
                columns="120px 1fr",
            ),
            style={"width": 360},
        ),
    ),
)
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/overlay/hover-card/#events-when-the-hovercard-opens-or-closes">

# Events when the Hovercard opens or closes

The `on_open_change` event is called when the `open` state of the hovercard changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
  </div>
</div>

# Number of times hovercard opened or closed: 0

# Hovercard open: false

Hover over the text to see the hover card. [Hover over me](#)

## Number of times hovercard opened or closed: 0

## Hovercard open: False

This is the tooltip content.

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/hover-card/#rx.hover_card.root)

# rx.hover_card.root

For sighted users to preview content available behind a link.

Hover over me

## Props

- **Prop** | **Type | Values** | **Default** | **Interactive**
  - `default_open` | bool |  |
  - `open` | bool |  |
  - `open_delay` | int |  |
  - `close_delay` | int |  |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.hover_card.content

Hover over me

## Properties

- **side**
  - Type: `"top" | "right" | ...`
  - Default: None
  - Interactive: Yes

- **side_offset**
  - Type: `int`
  - Default: None
  - Interactive: No

- **align**
  - Type: `"start" | "center" | ...`
  - Default: None
  - Interactive: Yes

- **align_offset**
  - Type: `int`
  - Default: None
  - Interactive: No

- **avoid_collisions**
  - Type: `bool`
  - Default: False
  - Interactive: No

- **collision_padding**
  - Type: `Union[float, int, dict]`
  - Default: None
  - Interactive: No

- **sticky**
  - Type: `"partial" | "always"`
  - Default: "partial"
  - Interactive: Yes

- **hide_when_detached**
  - Type: `bool`
  - Default: False
  - Interactive: No

- **size**
  - Type: `"1" | "2" | ...`
  - Default: "1"
  - Interactive: Yes

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.hover_card.trigger

Wraps the link that will open the hover card.

<div class="rt-Box pb-2"><p class="rt-Text font-normal text-slate-12 mb-4 leading-7">Wraps the link that will open the hover card.</p></div>

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)