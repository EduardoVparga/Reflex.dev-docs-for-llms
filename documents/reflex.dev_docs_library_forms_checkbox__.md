# Checkbox

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/forms/checkbox/#basic-example">

# Basic Example

The `on_change` trigger is called when the `checkbox` is clicked.

```python
```

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
    </div>
</div>

# false

- [ ] 

The `input` prop is used to set the `checkbox` as a controlled component.

```python
class CheckboxState(rx.State):
    checked: bool = False


def checkbox_example():
    return rx.vstack(
        rx.heading(CheckboxState.checked),
        rx.checkbox(on_change=CheckboxState.set_checked),
    )
```

The `input` prop is used to set the `checkbox` as a controlled component.

# Example Form

- [ ] 
- Submit

---

# Results:
Example Form

- Accept terms and conditions: 
  - Submit

Results: {}
```python
class FormCheckboxState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data


def form_checkbox_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.hstack(
                    rx.checkbox(name="checkbox", label="Accept terms and conditions"),
                    rx.button("Submit", type="submit"),
                    width="100%",
                    on_submit=FormCheckboxState.handle_submit,
                    reset_on_submit=True,
                ),
                align_items="left",
                width="50%",
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"), 
                rx.badge(FormCheckboxState.form_data.to_string())
            ),
            align_items="left",
            width="100%",
        ),
        width="50%"
    )
```
![Copy Code](http://reflex.dev/docs/library/forms/checkbox/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/checkbox/#rx.checkbox)

# rx.checkbox

A checkbox component with a label.

## Basic Checkbox Example

```html
<label>
  <button aria-checked="false" aria-required="false" class="rt-reset rt-BaseCheckboxRoot rt-CheckboxRoot rt-r-size-1 rt-variant-classic" data-accent-color="tomato" data-state="unchecked" role="checkbox" type="button" value="on"></button>Basic Checkbox
</label>
```

## Properties

| Prop               | Type | Default | Interactive |
|--------------------|------|---------|------------|
| text               | str  |         |            |
| spacing            | "0" | "1" | ...       |        | bool          |
| size               | "1" | "2" | ...       |        | bool          |
| as_child           | bool |         |            |
| variant            | "classic" | "surface" | ...      |        | bool          |
| color_scheme       | "tomato" | "red" | ...       |        | bool          |
| high_contrast      | bool | false   |           |
| default_checked    | bool |         |           |
| checked            | bool |         |           |
| disabled           | bool | false   |           |
| required           | bool | false   |           |
| name               | str  |         |           |
| value              | str  |         |           |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_change`
  - **Description**: Props to rename Fired when the checkbox is checked or unchecked.