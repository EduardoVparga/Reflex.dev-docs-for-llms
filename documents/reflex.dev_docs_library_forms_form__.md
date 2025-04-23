# Form

Forms are used to collect user input. The `rx.form` component is used to group inputs and submit them together.

The form component's children can be form controls such as `rx.input`, `rx.checkbox`, `rx.slider`, `rx.textarea`, `rx.radio_group`, `rx.select` or `rx.switch`. The controls should have a `name` attribute that is used to identify the control in the form data. The `on_submit` event trigger submits the form data as a dictionary to the `handle_submit` event handler.

The form is submitted when the user clicks the submit button or presses enter on the form controls.

- First Name: 
  - Last Name: 
  - Checked:
    - Switch:
      - Submit:

The provided content appears to be a detailed documentation or API reference for various form components in Reflex, which is a framework for building reactive user interfaces. Here's an overview and summary of the main components mentioned:

1. **rx.form**: This component represents a complete form with fields, messages, and submit functionality.

2. **rx.form.field**: Represents individual input fields within a form.
   - `name`: The name attribute of the field.
   - `match`: Validation rules for the field (e.g., "badInput", "patternMismatch").
   - `force_match`: Whether to force validation even when no change is detected.
   - `as_child`: Whether to render as a child component.

3. **rx.form.message**: Displays messages related to form fields, such as error or success messages.
   - `name`: The name of the field associated with the message.
   - `match`: The type of validation match (e.g., "badInput", "patternMismatch").
   - `as_child`: Whether to render as a child component.

4. **rx.form.submit**: Represents a submit button for the form.
   - `as_child`: Whether to render as a child component.

### Example Usage

Here's an example of how these components might be used in a Reflex application:

```python
from reflex import *

class App(State):
    email: str = ""

def main():
    return Form(
        Field(name="email", value=App.email, match=["badInput"], force_match=True),
        Message(name="email", match=["badInput"], as_child=False),
        Submit("Submit"),
    )

app = App()
```

### Key Points

- **Form Validation**: Fields can have validation rules attached to them.
- **Message Customization**: Messages are displayed based on the field's state and validation results.
- **Submission Handling**: The form has a submit button that triggers submission logic.

### Event Triggers
Each component supports various event triggers, such as `on_change`, `on_focus`, etc., which can be used to handle different user interactions. For detailed information on these events, you should refer to the official documentation.

This summary provides an overview of the form components in Reflex and how they can be utilized to build reactive forms with validation and submission functionality.

# Using `name` vs `id`.

This is a brief explanation of the difference between using `name` and `id` in certain contexts, likely in programming or web development.

# Video: Forms

## Dynamic Forms

[Learn more](https://reflex.dev/docs/library/forms/form/#dynamic-forms)

# Dynamic Forms

Forms can be dynamically created by iterating through state vars using `rx.foreach`.

This example allows the user to add new fields to the form prior to submit, and all
fields will be included in the form data passed to the `handle_submit` function.

## Form Fields

- First Name: [Input Field]
- Last Name: [Input Field]
- Email: [Input Field]

---

[Submit Button]

---

New Field:
- [Input Field]
+ [Button]

# Results

{}

```python
class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[str] = ["first_name", "last_name", "email"]

    @rx.var(cache=True)
    def form_field_placeholders(self) -> list[str]:
        return [w.capitalize() for w in field.split("_") for field in self.form_fields]

    @rx.event
    def add_field(self, form_data: dict):
        new_field = form_data.get("new_field")
        if not new_field:
            return
        field_name = (new_field.strip().lower().replace(" ", "_"))
        self.form_fields.append(field_name)

    @rx.event
    def handle_submit(self, form_data: dict):
        self.form_data = form_data


def dynamic_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field, idx: rx.input(
                        placeholder=DynamicFormState.form_field_placeholders[idx],
                        name=field,
                    ),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.form(
            rx.hstack(
                rx.input(placeholder="New Field", name="new_field"),
                rx.button("+", type="submit"),
            ),
            on_submit=DynamicFormState.add_field,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(DynamicFormState.form_data.to_string()),
    )
```
```

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/form/#rx.form)

# rx.form

The Form component.

## Test

### Props

| Prop          | Type | Values     | Default | Interactive |
|---------------|------|------------|---------|-------------|
| as_child      | bool | -          |         |             |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.form.root

The root component of a radix form.

## Email Form

<form>
  <div class="Field">
    <label for="radix-:R19ja6kml6:">Email</label>
    <input aria-describedby="radix-:R2f9ja6kml6:" id="radix-:R19ja6kml6:" name="email" placeholder="Email Address" type="email"/>
    <span id="radix-:R2f9ja6kml6:">Please enter a valid email</span>
    <button class="Submit" type="submit">Submit</button>
  </div>
</form>

## Properties

- **as_child**: bool
- **Description**: 
  - Type | Values: `bool`
  - Default: Not specified
  - Interactive: No description

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.form.field

A form field component.

## Form Example

```html
<form>
    <label for="radix-:R19je6kml6">Email</label>
    <input id="radix-:R19je6kml6" placeholder="Email Address" type="email"/>
    <button type="submit">Submit</button>
</form>
```

### Properties

- **name**
  - **Type:** str
  - **Default:** None
  - **Interactive:** No

- **server_invalid**
  - **Type:** bool
  - **Default:** False
  - **Interactive:** Yes

- **as_child**
  - **Type:** bool
  - **Default:** False
  - **Interactive:** No

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.form.control

A form control component.

## Prop

- **as_child**
  - Type: `bool`
  - Default: None
  - Interactive: No

---

The content continues but seems to be mostly redundant or contains repeated structure. If you need more details, please provide the specific part of the HTML you wish to convert further.

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.form.label

A form label component.

## Form

```html
<form>
  <div class="Field">
    <label for="radix-:R19jm6kml6:">Email</label>
    <input id="radix-:R19jm6kml6:" placeholder="Email Address" type="email"/>
    <button class="Submit" type="submit">Submit</button>
  </div>
</form>
```

### Table of Properties

| Prop           | Type | Default | Interactive |
|----------------|------|---------|------------|
| as_child       | bool |         |            |

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.form.message

A form message component.

## Form Example

```html
<form>
    <div>
        <label for="radix-:R19jq6kml6:">Email</label>
        <input id="radix-:R19jq6kml6:" name="email" placeholder="Email Address" type="email"/>
        <button class="Submit" type="submit">Submit</button>
    </div>
</form>
```

## Properties

| Prop           | Type | Default | Interactive |
|----------------|------|---------|------------|
| `name`         | str  | -       | -          |
| `match`        | "badInput" | "patternMismatch" | -          |
| `force_match`  | bool | -       | <button>False</button> |
| `as_child`     | bool | -       | -          |

---

## Table of Properties

- **name**  
  Type: str
  Default: None
  Interactive: No

- **match**  
  Type: "badInput" | "patternMismatch"
  Default: None
  Interactive: Yes (Dropdown)

- **force_match**  
  Type: bool
  Default: False
  Interactive: Yes (Checkbox)

- **as_child**  
  Type: bool
  Default: None
  Interactive: No

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.form.submit
A form submit component.

## Example

```html
<button class="Submit" type="submit">Test</button>
```

### Props

- **Prop**: `as_child`
  - **Type | Values**: `bool`
  - **Default**: None
  - **Interactive**: No

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)