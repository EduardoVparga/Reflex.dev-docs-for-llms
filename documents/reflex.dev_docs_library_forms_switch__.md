# Switch

A toggle switch alternative to the checkbox.

[Learn more](https://reflex.dev/docs/library/forms/switch/#basic-example)

# Basic Example

Here is a basic example of a switch. We use the `on_change` trigger to toggle the value in the state.

<button aria-checked="false" class="rt-SwitchRoot rt-r-size-2 rt-variant-surface" data-state="unchecked" role="switch" type="button" value="on">
  <span class="rt-SwitchThumb" data-state="unchecked"></span>
</button>
<span class="rt-Badge rt-r-size-1 rt-variant-soft" data-accent-color="">false</span>

```python
class SwitchState(rx.State):
    value: bool = False

    @rx.event
    def set_end(self, value: bool):
        self.value = value

def switch_intro():
    return rx.center(
        rx.switch(on_change=SwitchState.set_end),
        rx.badge(SwitchState.value),
    )
```

# Control the value

The `checked` prop is used to control the state of the switch. The event `on_change` is called when the state of the switch changes, when the `change_checked` event handler is called.

The `disabled` prop when `True`, prevents the user from interacting with the switch. In our example below, even though the second switch is disabled we are still able to change whether it is checked or not using the `checked` prop.

<button aria-checked="true" class="rt-reset rt-SwitchRoot rt-r-size-2 rt-variant-surface" data-state="checked" role="switch" type="button" value="on"><span class="rt-SwitchThumb" data-state="checked"></span></button>
<button aria-checked="true" class="rt-reset rt-SwitchRoot rt-r-size-2 rt-variant-surface" data-disabled="" data-state="checked" disabled="" role="switch" type="button" value="on"><span class="rt-SwitchThumb" data-disabled="" data-state="checked"></span></button>

```python
class ControlSwitchState(rx.State):
    checked = True

    @rx.event
    def change_checked(self, checked: bool):
        """Change the switch checked var."""
        self.checked = checked


def control_switch_example():
    return rx.hstack(
        rx.switch(
            checked=ControlSwitchState.checked,
            on_change=ControlSwitchState.change_checked,
        ),
        rx.switch(
            checked=ControlSwitchState.checked,
            on_change=ControlSwitchState.change_checked,
            disabled=True,
        ),
    )
```

[Link to reflex.dev/docs/library/forms/switch/#switch-in-forms](https://reflex.dev/docs/library/forms/switch/#switch-in-forms)

# Switch in forms

The `name` of the switch is needed to submit with its owning form as part of a name/value pair. When the `required` prop is `True`, it indicates that the user must check the switch before the owning form can be submitted.

The `value` prop is only used for form submission, use the `checked` prop to control state of the `switch`.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-reset rt-BaseCard rt-Card rt-r-size-1 rt-variant-surface css-11ze7cv">
            <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1lni6sm"></div>
        </div>
    </div>
</div>

# Example Form

- [ ] 
- Submit

---

# Results:

Example Form

```python
class FormSwitchState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def switch_form_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.hstack(
                    rx.switch(name="switch"),
                    rx.button("Submit", type="submit"),
                    width="100%",
                ),
                on_submit=FormSwitchState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(FormSwitchState.form_data.to_string()),
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/switch/#rx.switch)

# rx.switch

A toggle switch alternative to the checkbox.

## Example

```html
<button aria-checked="false" aria-required="false" class="rt-reset rt-SwitchRoot rt-r-size-1 rt-variant-classic" data-accent-color="tomato" data-radius="none" data-state="unchecked" role="switch" type="button" value="on">
    <span class="rt-SwitchThumb" data-state="unchecked"></span>
</button>
```

## Properties

- **as_child**: `bool`  
  - Default: None
- **default_checked**: `bool`  
  - Default: None
- **checked**: `bool`  
  - Default: None
- **disabled**: `bool`  
  - Default: false (False)
- **required**: `bool`  
  - Default: false (False)
- **name**: `str`  
  - Default: None
- **value**: `str`  
  - Default: None
- **size**: `"1" | "2" | ...`  
  - Default: "1"
- **variant**: `"classic" | "surface" | ...`  
  - Default: "classic"
- **color_scheme**: `"tomato" | "red" | ...`  
  - Default: "tomato"
- **high_contrast**: `bool`  
  - Default: false (False)
- **radius**: `"none" | "small" | ...`  
  - Default: "none"

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_change`
  - **Description:** Props to rename Fired when the value of the switch changes