# Popover

A popover displays content, triggered by a button.

The `popover.root` contains all the parts of a popover.
The `popover.trigger` contains the button that toggles the popover.
The `popover.content` is the component that pops out when the popover is open.
The `popover.close` is the button that closes an open popover.

[Basic Example](https://reflex.dev/docs/library/overlay/popover/#basic-example)

# Basic Example

[![Basic Example](https://via.placeholder.com/18x18)](https://reflex.dev/docs/library/overlay/popover/#examples-in-context)

<div class="py-4 gap-4 flex flex-col w-full">
    <div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <button aria-controls="radix-:R556kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Popover</button>
    </div>
    <div class="relative mb-4">
        <pre>
rx.popover.root(
    rx.popover.trigger(
        rx.button("Popover"),
    ),
    rx.popover.content(
        rx.flex(
            rx.text("Simple Example"),
            rx.popover.close(
                rx.button("Close"),
            ),
            direction="column",
            spacing="3",
        ),
    ),
)
        </pre>
    </div>
</div>

# Examples in Context

## Comment

<button aria-controls="radix-:R5d6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-soft rt-Button" data-accent-color="" data-state="closed" type="button">Comment</button>

<div class="relative mb-4">
    <div class="code-block">
        ```python
rx.popover.root(
    rx.popover.trigger(
        rx.button("Comment", variant="soft"),
    ),
    rx.popover.content(
        rx.flex(
            rx.avatar("2", fallback="RX", radius="full"),
            rx.box(
                rx.text_area(placeholder="Write a comment…", style={"height": 80}),
                rx.flex(
                    rx.checkbox("Send to group"),
                    rx.popover.close(rx.button("Comment", size=1)),
                    spacing=3,
                    margin_top="12px",
                    justify="between"
                ),
                flex_grow=1,
            ),
            spacing=3,
        ),
        style={"width": 360},
    ),
)
```
</div>
<button class="css-kobh7h">
    <svg class="lucide lucide-copy css-cqk0y8" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg">
        <rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect>
        <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>
    </svg>
</button>
</div>

## Feedback

<button aria-controls="radix-:R5h6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-classic rt-Button" data-accent-color="" data-state="closed" type="button">Feedback</button>

<div class="relative mb-4">
    <div class="code-block">
        ```python
rx.popover.root(
    rx.popover.trigger(
        rx.button("Feedback", variant="classic"),
    ),
    rx.popover.content(
        rx.inset(side="top", background="url('https://images.unsplash.com/5/unsplash-kitsune-4.jpg') center/cover", height="100px"),
        rx.box(
            rx.text_area(placeholder="Write a comment…", style={"height": 80}),
            rx.flex(
                rx.checkbox("Send to group"),
                rx.popover.close(rx.button("Comment", size=1)),
                spacing=3,
                margin_top="12px",
                justify="between"
            ),
            padding_top="12px",
        ),
        style={"width": 360},
    ),
)
```
</div>
<button class="css-kobh7h">
    <svg class="lucide lucide-copy css-cqk0y8" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg">
        <rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect>
        <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>
    </svg>
</button>
</div>

# Popover with dynamic title

Code like below will not work as expected and it is necessary to place the dynamic title (`Index2State.language`) inside of an `rx.text` component.

```python
class Index2State(rx.State):
    language: str = "EN"

def index() -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(rx.button(Index2State.language)),
        rx.popover.content(rx.text("Success")),
    )
```

This code will work:

```python
class Index2State(rx.State):
    language: str = "EN"

def index() -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(rx.button(rx.text(Index2State.language))),
        rx.popover.content(rx.text("Success")),
    )
```

[![Copy](https://raw.githubusercontent.com/radix-ui/icons/main/svg/copy.svg)](https://reflex.dev/docs/library/overlay/popover/#events-when-the-popover-opens-or-closes)

# Events when the Popover opens or closes

The `on_open_change` event is called when the `open` state of the popover changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
  </div>
</div>

# Number of times popover opened or closed: 0

# Popover open: false

**Popover**

## Number of times popover opened or closed: 0
## Popover open: False

Simple Example  
Close  

---

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/popover/#rx.popover.root)

# rx.popover.root

Floating element for displaying rich content, triggered by a button.

<button aria-controls="radix-:R1j66kml6:" aria-expanded="false" aria-haspopup="dialog">Popover</button>

## Props

| Prop      | Type | Values | Default | Interactive |
|-----------|------|--------|---------|------------|
| open      | bool |        |         |            |
| modal     | bool |        |         | <label><div><button aria-checked="false" role="checkbox" type="button"></button>false</div></label> |
| default_open | bool |        |         |            |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.popover.content

Contains content to be rendered in the open popover.

## Button Example
- **Button:** Popover
  - Type: `button`

## Properties
- **size**
  - Type | Values: `"1" | "2" | ...`
  - Default: None
  - Interactive: No

- **side**
  - Type | Values: `"top" | "right" | ...`
  - Default: None
  - Interactive: No

- **side_offset**
  - Type | Values: `int`
  - Default: None
  - Interactive: No

- **align**
  - Type | Values: `"start" | "center" | ...`
  - Default: None
  - Interactive: No

- **align_offset**
  - Type | Values: `int`
  - Default: None
  - Interactive: No

- **avoid_collisions**
  - Type | Values: `bool`
  - Default: False
  - Interactive: No

- **collision_padding**
  - Type | Values: `Union[float, int, dict]`
  - Default: None
  - Interactive: No

- **sticky**
  - Type | Values: `"partial" | "always"`
  - Default: partial
  - Interactive: No

- **hide_when_detached**
  - Type | Values: `bool`
  - Default: False
  - Interactive: No

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.popover.trigger

Wraps the control that will open the popover.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props

No component specific props

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.popover.close

Wraps the control that will close the popover.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)