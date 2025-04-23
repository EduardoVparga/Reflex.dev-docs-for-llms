# Select

Displays a list of options for the user to pick from—triggered by a button.

## Example 1

<button aria-autocomplete="none" aria-controls="radix-:R1ih6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface" data-state="closed" dir="ltr" role="combobox" type="button">
<span class="rt-SelectTriggerInner"><span style="pointer-events:none">apple</span></span><svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9" xmlns="http://www.w3.org/2000/svg"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg>
</button>
<span class="rt-reset rt-Badge rt-r-size-1 rt-variant-soft" data-accent-color="">apple</span>

```python
class SelectState(rx.State):
    value: str = "apple"

    @rx.event
    def change_value(self, value: str):
        """Change the select value var."""
        self.value = value

def select_intro():
    return rx.center(
        rx.select(["apple", "grape", "pear"], value=SelectState.value, on_change=SelectState.change_value),
        rx.badge(SelectState.value)
    )
```

## Example 2

<button aria-autocomplete="none" aria-controls="radix-:R1il6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface" data-state="closed" dir="ltr" role="combobox" type="button">
<span class="rt-SelectTriggerInner"><span style="pointer-events:none">apple</span></span><svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9" xmlns="http://www.w3.org/2000/svg"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg>
</button>
<button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="">Change Value</button>

```python
class SelectState3(rx.State):
    values: list[str] = ["apple", "grape", "pear"]
    value: str = "apple"

    @rx.event
    def change_value(self):
        """Change the select value var."""
        self.value = random.choice(self.values)

def select_example3():
    return rx.vstack(
        rx.select(SelectState3.values, value=SelectState3.value, on_change=SelectState3.set_value),
        rx.button("Change Value", on_click=SelectState3.change_value)
    )
```

## Event Handlers

The `on_open_change` event handler acts in a similar way to the `on_change` and is called when the open state of the select changes.

```python
rx.select(
    ["apple", "grape", "pear"],
    on_change=rx.window_alert("on_change event handler called")
)
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/forms/select/#submitting-a-form-using-select">Learn More</a>

Submitting a form using select
The `name` prop is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must select a value before the owning form can be submitted.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-reset rt-BaseCard rt-Card rt-r-size-1 rt-variant-surface css-11ze7cv">
            <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1lni6sm"></div>
        </div>
    </div>
</div>

# Example Form

<form>
  <button>apple</button>
  <select required>
    <option selected value="apple">apple</option>
    <option value="grape">grape</option>
    <option value="pear">pear</option>
  </select>
  <button type="submit">Submit</button>
</form>

---
<div>

# Results:
Example Form

```
class FormSelectState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def select_form_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.flex(
                    rx.select(["apple", "grape", "pear"], default_value="apple", name="select", required=True),
                    rx.button("Submit", flex="1", type="submit"), width="100%", spacing="3",
                    on_submit=FormSelectState.handle_submit, reset_on_submit=True
                ),
                rx.divider(),
                rx.hstack(
                    rx.heading("Results:"), 
                    rx.badge(FormSelectState.form_data.to_string())
                ),
                align_items="left", width="100%"
            ),
            width="50%"
        )
    )
```

Results: apple

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/select/#rx.select)

# rx.select

High level wrapper for the Select component.

## Props

| Prop         | Type          | Default | Interactive |
|--------------|---------------|---------|-------------|
| items        | Sequence      | -       | -           |
| placeholder  | str           | -       | -           |
| label        | str           | -       | -           |
| color_scheme | "tomato" | "red" | ...         | — |
| high_contrast | bool          | -       | -           |
| variant      | "classic" | "surface" | ...         | — |
| radius       | "none" | "small" | ...         | — |
| width        | str           | -       | -           |
| position     | "item-aligned" | "popper" |            | — |
| size         | "1" | "2" | ...         | — |
| default_value| str           | -       | -           |
| value        | str           | -       | -           |
| default_open | bool          | -       | -           |
| open         | bool          | -       | -           |
| name         | str           | -       | -           |
| disabled     | bool          | -       | -           |
| required     | bool          | -       | -           |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.root

Displays a list of options for the user to pick from, triggered by a button.

## Example Usage

```html
<button aria-autocomplete="none" aria-controls="radix-:R36a6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-1 rt-variant-surface" data-state="closed" dir="ltr" role="combobox" type="button">
  <span class="rt-SelectTriggerInner"><span style="pointer-events:none">pear</span></span>
  <svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9">
    <path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path>
  </svg>
</button>
```

### Properties

- **size**
  - Type: `"1" | "2" | ...`
  - Default: Not specified
  - Interactive: Dropdown to select size

- **default_value**
  - Type: `str`
  - Default: Not specified

- **value**
  - Type: `str`
  - Default: Not specified

- **default_open**
  - Type: `bool`
  - Default: Not specified

- **open**
  - Type: `bool`
  - Default: Not specified

- **name**
  - Type: `str`
  - Default: Not specified

- **disabled**
  - Type: `bool`
  - Default: `false`

- **required**
  - Type: `bool`
  - Default: `false`

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.trigger

The button that toggles the select.

## Properties

- **Prop**: Type | Values | Default | Interactive
- **variant**
  - "classic" | "surface" | ...
  - 
  - 
  - <button>classic</button>
- **color_scheme**
  - "tomato" | "red" | ...
  - 
  - 
  - <button>tomato</button>
- **radius**
  - "none" | "small" | ...
  - 
  - 
  - <button>none</button>
- **placeholder**
  - str
  -

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.content

The component that pops out when the select is open.

## Properties

- **variant**
  - Type | Values: `"solid" | "soft"`
  - Default: Not provided
  - Interactive: Yes

- **color_scheme**
  - Type | Values: `"tomato" | "red" | ...`
  - Default: Not provided
  - Interactive: Yes

- **high_contrast**
  - Type | Values: `bool`
  - Default: Not provided
  - Interactive: No

- **position**
  - Type | Values: `"item-aligned" | "popper"`
  - Default: Not provided
  - Interactive: Yes

- **side**
  - Type | Values: `"top" | "right" | ...`
  - Default: Not provided
  - Interactive: Yes

- **side_offset**
  - Type | Values: `int`
  - Default: Not provided
  - Interactive: No

- **align**
  - Type | Values: `"start" | "center" | ...`
  - Default: Not provided
  - Interactive: Yes

- **align_offset**
  - Type | Values: `int`
  - Default: Not provided
  - Interactive: No

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.group

Used to group multiple items.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.item

The component that contains the select items.

## Button Example

<button aria-autocomplete="none" aria-controls="radix-:R36q6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface" data-state="closed" dir="ltr" role="combobox" type="button">
  <span class="rt-SelectTriggerInner"><span style="pointer-events:none">pear</span></span>
</button>

## Select Items

- **Prop**: value
  - **Type | Values**: `str`
  - **Default**: Not specified
- **Prop**: disabled
  - **Type | Values**: `bool`
  - **Default**: Not specified

### Interactive Example

<label class="rt-Text rt-r-size-2">
  <div class="rt-Flex rt-r-gap-2">
    <button aria-checked="false" class="rt-reset rt-BaseCheckboxRoot rt-CheckboxRoot rt-r-size-2 rt-variant-surface" data-state="unchecked" role="checkbox" type="button" value="on"></button>
    false
  </div>
</label>

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.label

Used to render the label of a group, it isn't focusable using arrow keys.

---

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.select.separator

Used to visually separate items in the Select. 

<div class="rt-Box pb-2"><p class="rt-Text font-normal text-slate-12 mb-4 leading-7">Used to visually separate items in the Select.</p></div>

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)