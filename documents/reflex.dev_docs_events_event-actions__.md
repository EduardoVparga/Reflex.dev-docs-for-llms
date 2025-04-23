# Event Actions

In Reflex, an event action is a special behavior that occurs during or after processing an event on the frontend.

Event actions can modify how the browser handles DOM events or throttle and debounce events before they are processed by the backend.

An event action is specified by accessing attributes and methods present on all EventHandlers and EventSpecs.

[Learn more about DOM event propagation](https://reflex.dev/docs/events/event-actions/#dom-event-propagation)

# DOM Event Propagation

*Added in v0.3.2*

[Learn more](https://reflex.dev/docs/events/event-actions/#prevent_default)

# prevent_default

The `.prevent_default` action prevents the default behavior of the browser for the action. This action can be added to any existing event, or it can be used on its own by specifying `rx.prevent_default` as an event handler.

A common use case for this is to prevent navigation when clicking a link.

This Link Does Nothing
https://reflex.dev/

```python
rx.link(
    "This Link Does Nothing",
    href="https://reflex.dev/",
    on_click=rx.prevent_default,
)
```

## Output

This Link Does Nothing

# The value is false

[Toggle Value](https://reflex.dev/)

```python
class LinkPreventDefaultState(rx.State):
    status: bool = False

    @rx.event
    def toggle_status(self):
        self.status = not self.status


def prevent_default_example():
    return rx.vstack(
        rx.heading(f"The value is {LinkPreventDefaultState.status}"),
        rx.link(
            "Toggle Value",
            href="https://reflex.dev/",
            on_click=LinkPreventDefaultState.toggle_status.prevent_default,
        ),
    )
```

# stop_propagation

The `.stop_propagation` action stops the event from propagating to parent elements. This action is often used when a clickable element contains nested buttons that should not trigger the parent element's click event.

In the following example, the first button uses `.stop_propagation` to prevent the click event from propagating to the outer vstack. The second button does not use `.stop_propagation`, so the click event will also be handled by the on_click attached to the outer vstack.

```
class StopPropagationState(rx.State):
    where_clicked: list[str] = []

    @rx.event
    def handle_click(self, where: str):
        self.where_clicked.append(where)

    @rx.event
    def handle_reset(self):
        self.where_clicked = []

def stop_propagation_example():
    return rx.vstack(
        rx.button(
            "btn1 - Stop Propagation",
            on_click=StopPropagationState.handle_click("btn1").stop_propagation,
        ),
        rx.button(
            "btn2 - Normal Propagation",
            on_click=StopPropagationState.handle_click("btn2"),
        ),
        rx.foreach(StopPropagationState.where_clicked, rx.text),
        rx.button(
            "Reset",
            on_click=StopPropagationState.handle_reset.stop_propagation,
        ),
        padding="2em",
        border=f"1px dashed {rx.color('accent', 5)}",
        on_click=StopPropagationState.handle_click("outer"),
    )
```

The following buttons are displayed:

- btn1 - Stop Propagation
- btn2 - Normal Propagation
- Reset

These buttons and the reset button are part of a vstack with some styling applied.

# Throttling and Debounce

For events that are fired frequently, it can be useful to throttle or debounce them to avoid network latency and improve performance. These actions both take a single argument which specifies the delay time in milliseconds.

[Throttle](https://reflex.dev/docs/events/event-actions/#throttle)

# throttle

The `.throttle` action limits the number of times an event is processed within a given time period. It is useful for `on_scroll` and `on_mouse_move` events which are fired very frequently, causing lag when handling them in the backend.

In the following example, the `on_scroll` event is throttled to only fire every half second.

<div>
  <div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <style>
      [data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}
    </style>
    <div class="overflow-x-auto" style="min-width:100%;display:table">
      <!-- Content will be here -->
    </div>
  </div>
</div>

# Scroll Me

- Item 0
- Item 1
- Item 2
- Item 3
- Item 4
- Item 5
- Item 6
- Item 7
- Item 8
- Item 9
- Item 10
- Item 11
- Item 12
- Item 13
- Item 14
- Item 15
- Item 16
- Item 17
- Item 18
- Item 19
- Item 20
- Item 21
- Item 22
- Item 23
- Item 24
- Item 25
- Item 26
- Item 27
- Item 28
- Item 29
- Item 30
- Item 31
- Item 32
- Item 33
- Item 34
- Item 35
- Item 36
- Item 37
- Item 38
- Item 39
- Item 40
- Item 41
- Item 42
- Item 43
- Item 44
- Item 45
- Item 46
- Item 47
- Item 48
- Item 49
- Item 50
- Item 51
- Item 52
- Item 53
- Item 54
- Item 55
- Item 56
- Item 57
- Item 58
- Item 59
- Item 60
- Item 61
- Item 62
- Item 63
- Item 64
- Item 65
- Item 66
- Item 67
- Item 68
- Item 69
- Item 70
- Item 71
- Item 72
- Item 73
- Item 74
- Item 75
- Item 76
- Item 77
- Item 78
- Item 79
- Item 80
- Item 81
- Item 82
- Item 83
- Item 84
- Item 85
- Item 86
- Item 87
- Item 88
- Item 89
- Item 90
- Item 91
- Item 92
- Item 93
- Item 94
- Item 95
- Item 96
- Item 97
- Item 98
- Item 99

Last Scroll Event: Invalid date

```python
class ThrottleState(rx.State):
    last_scroll: datetime.datetime | None
    
    @rx.event
    def handle_scroll(self):
        self.last_scroll = datetime.datetime.now(timezone.utc)

def scroll_box():
    return rx.scroll_area(
        rx.heading("Scroll Me"),
        [rx.text(f"Item {i}") for i in range(100)],
        height="75px",
        width="50%",
        border=f"1px solid {rx.color('accent', 5)}",
        on_scroll=ThrottleState.handle_scroll.throttle(500),
    )

def throttle_example():
    return (
        scroll_box(),
        rx.text(f"Last Scroll Event: ", rx.moment(ThrottleState.last_scroll, format="HH:mm:ss.SSS")),
    )
```

# Event Actions are Chainable

Event actions are chainable.

# debounce

The `.debounce` action delays the processing of an event until the specified timeout occurs. If another event is triggered during the timeout, the timer is reset and the original event is discarded.

Debounce is useful for handling the final result of a series of events, such as moving a slider.

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-18dvnhc" data-orientation="vertical" data-state="closed"></div>
</div>

### Debounced events are discarded.

In the following example, the slider's `on_change` handler, `update_value`, is only triggered on the backend when the slider value has not changed for half a second.

Settled Value: 50

```python
class DebounceState(rx.State):
    settled_value: int = 50

    @rx.event
    def update_value(self, value: list[int]):
        self.settled_value = value[0]

def debounced_slider():
    return rx.slider(
        key=rx.State.router.session.session_id,
        default_value=[DebounceState.settled_value],
        on_change=DebounceState.update_value.debounce(500),
        width="100%",
    )

def debounce_example():
    return rx.vstack(
        debounced_slider(),
        rx.text(f"Settled Value: {DebounceState.settled_value}")
    )
```

# Why set key on the slider?