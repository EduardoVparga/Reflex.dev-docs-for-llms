# Tooltip
A `tooltip` displays informative information when users hover over or focus on an element.
It takes a `content` prop, which is the content associated with the tooltip.

## Example

Hover over me

This is the tooltip content.

```python
rx.tooltip(
    rx.button("Hover over me"),
    content="This is the tooltip content.",
)
```

For more details, see [Events When the Tooltip Opens or Closes](/docs/library/overlay/tooltip/#events-when-the-tooltip-opens-or-closes)

# Events when the Tooltip opens or closes

The `on_open_change` event is called when the `open` state of the tooltip changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
    </div>
</div>

# Number of times tooltip opened or closed: 0

# Tooltip open: False

Hover over the button to see the tooltip.
[Hover over me](#)

```python
class TooltipState(rx.State):
    num_opens: int = 0
    opened: bool = False

    @rx.event
    def count_opens(self, value: bool):
        self.opened = value
        self.num_opens += 1


def index():
    return rx.flex(
        rx.heading(f"Number of times tooltip opened or closed: {TooltipState.num_opens}"),
        rx.heading(f"Tooltip open: {TooltipState.opened}"),
        rx.text("Hover over the button to see the tooltip.",
                rx.tooltip(rx.button("Hover over me"), content="This is the tooltip content.", on_open_change=TooltipState.count_opens)),
        direction="column",
        spacing="3",
    )
```

[![Copy](https://raw.githubusercontent.com/llSourcell/images/master/copy_button.png)](#)

# API Reference

[API Reference](/docs/library/overlay/tooltip/#rx.tooltip)

# rx.tooltip

Floating element that provides a control with contextual information via pointer or focus.

## Button Example
Hover over me
<button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed">Hover over me</button>

## Properties

- **content**
  - Type: `str`
  
- **default_open**
  - Type: `bool`
  
- **open**
  - Type: `bool`
  
- **side**
  - Values: `"top" | "right" | ...`
  - Default: `"top"`
  - Interactive: Dropdown

- **side_offset**
  - Type: `Union[int, float]`
  
- **align**
  - Values: `"start" | "center" | ...`
  - Default: `"start"`
  - Interactive: Dropdown

- **align_offset**
  - Type: `Union[int, float]`
  
- **avoid_collisions**
  - Type: `bool`
  - Default: `false`

- **collision_padding**
  - Type: `Union[float, int, dict]`
  
- **arrow_padding**
  - Type: `Union[int, float]`
  
- **sticky**
  - Values: `"partial" | "always"`
  - Default: `"partial"`
  - Interactive: Dropdown

- **hide_when_detached**
  - Type: `bool`
  - Default: `false`

- **delay_duration**
  - Type: `Union[int, float]`
  
- **disable_hoverable_content**
  - Type: `bool`
  - Default: `false`

- **force_mount**
  - Type: `bool`
  - Default: `false`

- **aria_label**
  - Type: `str`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- `on_open_change`: Fired when the open state changes.
- `on_escape_key_down`: Fired when the escape key is pressed.
- `on_pointer_down_outside`: Fired when the pointer is down outside the tooltip.