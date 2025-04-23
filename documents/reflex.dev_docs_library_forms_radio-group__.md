# Radio Group

A set of interactive radio buttons where only one can be selected at a time.

[Basic Example](/docs/library/forms/radio-group/#basic-example)

# Basic Example

No Selection

1. 1
2. 2
3. 3

```python
class RadioGroupState(rx.State):
    item: str = "No Selection"

    @rx.event
    def set_item(self, item: str):
        self.item = item


def radio_group_state_example():
    return rx.vstack(
        rx.badge(RadioGroupState.item, color_scheme="green"),
        rx.radio(["1", "2", "3"], on_change=RadioGroupState.set_item, direction="row"),
    )
```

[Link](/docs/library/forms/radio-group/#submitting-a-form-using-radio-group)

# Submitting a form using Radio Group

The `name` prop is used to name the group. It is submitted with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must check a radio item before the owning form can be submitted.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-reset rt-BaseCard rt-Card rt-r-size-1 rt-variant-surface css-11ze7cv">
            <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-4 rx-Stack css-1lni6sm"></div>
        </div>
    </div>
</div>

# Example Form

- Option 1
- Option 2
- Option 3

Submit

# Results:

Example Form

- Option 1
- Option 2
- Option 3

Submit

Results: {}

```python
class FormRadioState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def radio_form_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.vstack(
                    rx.radio_group([
                        "Option 1",
                        "Option 2",
                        "Option 3"
                    ], name="radio_choice", direction="row"),
                    rx.button("Submit", type="submit"),
                    width="100%",
                    spacing="4"
                ),
                on_submit=FormRadioState.handle_submit,
                reset_on_submit=True
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"),
                rx.badge(FormRadioState.form_data.to_string())
            ),
            align_items="left",
            width="100%",
            spacing="4"
        ),
        width="50%"
    )
```

# API Reference

[API Reference](/docs/library/forms/radio-group/#rx.radio_group)

# rx.radio_group

High level wrapper for the RadioGroup component.

## Example Usage

```python
<div class="rt-RadioGroupRoot" dir="ltr" role="radiogroup" style="outline:none" tabindex="0">
  <div class="rt-Flex rt-r-fd-row rt-r-gap-0">
    <label>
      <div class="rt-Flex rt-r-gap-2">
        <button aria-checked="false" value="1">1</button>
      </div>
    </label>
    <label>
      <div class="rt-Flex rt-r-gap-2">
        <button aria-checked="false" value="2">2</button>
      </div>
    </label>
    <label>
      <div class="rt-Flex rt-r-gap-2">
        <button aria-checked="false" value="3">3</button>
      </div>
    </label>
    <label>
      <div class="rt-Flex rt-r-gap-2">
        <button aria-checked="false" value="4">4</button>
      </div>
    </label>
    <label>
      <div class="rt-Flex rt-r-gap-2">
        <button aria-checked="false" value="5">5</button>
      </div>
    </label>
  </div>
</div>
```

## Props

| Prop         | Type                | Default | Interactive |
|--------------|---------------------|---------|-------------|
| `items`      | Sequence            | -       | -           |
| `direction`  | "row" | "column" | ...        | LiteralVar.create("row")   | Yes          |
| `spacing`    | "0" | "1" | ...        | LiteralVar.create("2")     | Yes          |
| `size`       | "1" | "2" | ...        | LiteralVar.create("2")     | Yes          |
| `variant`    | "classic" | "surface" | ...        | LiteralVar.create("classic")  | Yes          |
| `color_scheme` | "tomato" | "red" | ...        | -           | No            |
| `high_contrast` | bool                | -       | -           |
| `value`      | str                 | -       | -           |
| `default_value` | str                | -       | -           |
| `disabled`   | bool                | -       | -           |
| `name`       | str                 | -       | -           |
| `required`   | bool                | -       | -           |

## Notes

- The `color_scheme` prop has a palette icon which is not fully converted to Markdown.
- Some interactive components (like dropdowns and checkboxes) are represented as placeholders in the example usage.

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.radio_group.root

A set of interactive radio buttons where only one can be selected at a time.

## Properties

- **size**
  - Type | Values: "1" | "2" | ...
  - Default: LiteralVar.create("2")
  - Interactive: [Dropdown Menu]

- **variant**
  - Type | Values: "classic" | "surface" | ...
  - Default: LiteralVar.create("classic")
  - Interactive: [Dropdown Menu]

- **color_scheme**
  - Type | Values: "tomato" | "red" | ...
  - Default: 
  - Interactive: [Color Picker]

- **high_contrast**
  - Type: bool
  - Default: false
  - Interactive: [Checkbox]

- **value**
  - Type: str

- **default_value**
  - Type: str

- **disabled**
  - Type: bool
  - Default: false
  - Interactive: [Checkbox]

- **name**
  - Type: str

- **required**
  - Type: bool
  - Default: false
  - Interactive: [Checkbox]

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.radio_group.item

An item in the group that can be checked.

## Properties

- **Prop** | **Type | Values** | **Default** | **Interactive**
  - `value` | `str` | — | —
  - `disabled` | `bool` | — | <label><button>false</button></label>
  - `required` | `bool` | — | <label><button>false</button></label>

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)