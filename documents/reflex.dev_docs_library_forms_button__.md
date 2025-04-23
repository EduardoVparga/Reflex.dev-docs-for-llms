# Button
Buttons are essential elements in your application's user interface that users can click to trigger events.

[Learn more](https://reflex.dev/docs/library/forms/button/#basic-example)

# Basic Example

The `on_click` trigger is called when the button is clicked.

- Decrement

# 0

**Increment**

```python
class CountState(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1


def counter():
    return rx.flex(
        rx.button("Decrement", color_scheme="red", on_click=CountState.decrement),
        rx.heading(CountState.count),
        rx.button("Increment", color_scheme="grass", on_click=CountState.increment, spacing="3"),
    )
```

**Decrement**

**0**

**Increment**

# Loading and Disabled

The `loading` prop is used to indicate that the action triggered by the button is currently in progress. When set to `True`, the button displays a loading spinner, providing visual feedback to the user that the action is being processed. This also prevents multiple clicks while the button is in the loading state. By default, `loading` is set to `False`.

The `disabled` prop also prevents the button from being but does not provide a spinner.

Regular
Loading
Disabled

```python
rx.flex(
    rx.button("Regular"),
    rx.button("Loading", loading=True),
    rx.button("Disabled", disabled=True),
    spacing="2",
)
```

For more information, see [Reflex.dev documentation](https://reflex.dev/docs/library/forms/button/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/button/#rx.button)

# rx.button

Trigger an action or event, such as submitting a form or displaying a dialog.

## Basic Button Example

```html
<button class="rt-reset rt-BaseButton rt-r-size-1 rt-variant-classic rt-Button" data-accent-color="tomato" data-radius="none" type="submit">Basic Button</button>
```

### Props

| Prop             | Type | Values                | Default | Interactive |
|------------------|------|-----------------------|---------|-------------|
| as_child         | bool |                       |         |             |
| size             | str  | "1" | "2" | ...        |           |
| variant          | str  | "classic" | "solid" | ...        |           |
| color_scheme     | str  | "tomato" | "red" | ...        |           |
| high_contrast    | bool |                       | false   |             |
| radius           | str  | "none" | "small" | ...        |           |
| auto_focus       | bool |                       | false   |             |
| disabled         | bool |                       | false   |             |
| form             | str  |                       |         |             |
| form_action      | str  |                       |         |             |
| form_enc_type    | str  |                       |         |             |
| form_method      | str  |                       |         |             |
| form_no_validate | bool |                       | false   |             |
| form_target      | str  |                       |         |             |
| name             | str  |                       |         |             |
| type             | str  | "submit" | "reset" | ...        |           |
| value            | Union[str, int, float] |               |         |             |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)