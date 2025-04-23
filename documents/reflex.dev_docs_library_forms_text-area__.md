# Text Area
A text area is a multi-line text input field.

[Basic Example](https://reflex.dev/docs/library/forms/text-area/#basic-example)

# Basic Example

The text area component can be controlled by a single value. The `on_blur` prop can be used to update the value when the text area loses focus.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
    </div>
</div>

# Hello World!

## TextAreaBlur Example

```python
class TextAreaBlur(rx.State):
    text: str = "Hello World!"

def blur_example():
    return rx.vstack(
        rx.heading(TextAreaBlur.text),
        rx.text_area(
            placeholder="Type here...",
            on_blur=TextAreaBlur.set_text,
        ),
    )
```

[Link to Reflex.dev](https://reflex.dev/docs/library/forms/text-area/#text-area-in-forms)

# Text Area in forms

Here we show how to use a text area in a form. We use the `name` prop to identify the text area in the form data. The form data is then passed to the `submit_feedback` method to be processed.

Are you enjoying Reflex?

Write your feedback…

Send

```python
class TextAreaFeedbackState(rx.State):
    feedback: str = ""
    submitted: bool = False

    @rx.event
    def submit_feedback(self, form_data: dict):
        self.submitted = True

    @rx.event
    def reset_form(self):
        self.feedback = ""
        self.submitted = False


def feedback_form():
    return rx.cond(
        TextAreaFeedbackState.submitted,
        rx.card(
            rx.vstack(
                rx.text("Thank you for your feedback!"),
                rx.button(
                    "Submit another response",
                    on_click=TextAreaFeedbackState.reset_form,
                ),
            )
        ),
        rx.card(
            rx.form(
                rx.flex(
                    rx.text("Are you enjoying Reflex?"),
                    rx.text_area(
                        placeholder="Write your feedback…",
                        value=TextAreaFeedbackState.feedback,
                        on_change=TextAreaFeedbackState.set_feedback,
                        resize="vertical",
                    ),
                    rx.button("Send", type="submit"),
                    direction="column",
                    spacing="3",
                ),
                on_submit=TextAreaFeedbackState.submit_feedback,
            )
        ),
    )
```

[API Reference](https://reflex.dev/docs/library/forms/text-area/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/text-area/#rx.text_area)

It appears you have a detailed list of configuration options for some kind of input component, likely from a Python library like `streamlit` or `dash`. Here's an organized breakdown of the properties and their descriptions:

### Properties Overview

1. **General Properties:**
   - **auto_complete**: A boolean indicating whether auto-complete should be enabled.
   - **auto_focus**: A boolean indicating whether the input should automatically receive focus.
   - **default_value**: The default value of the input, typically a string (`str`).
   - **dirname**: The directory name for file input components (string `str`).
   - **disabled**: A boolean indicating whether the input is disabled or not.
   - **form**: Name of the form to which this input belongs (string `str`).
   - **max_length**: Maximum length of the string value (`int`).
   - **min_length**: Minimum length of the string value (`int`).
   - **name**: The name of the input field (string `str`).
   - **placeholder**: Placeholder text for the input (string `str`).
   - **read_only**: A boolean indicating whether the input is read-only.
   - **required**: A boolean indicating if the input is required.
   - **rows**: Number of rows for multi-line inputs, typically a string (`str`).
   - **value**: The current value of the input (string `str`).
   - **wrap**: Whether to wrap text in a multi-line input (string `str`).

2. **Boolean Properties:**
   - These properties are toggles that can be set to `True` or `False`.
     - auto_complete
     - auto_focus
     - disabled
     - read_only
     - required

3. **String Properties:**
   - These properties take string values.
     - default_value
     - dirname
     - form
     - name
     - placeholder
     - rows
     - value
     - wrap

4. **Integer Properties:**
   - These properties take integer values.
     - max_length
     - min_length

5. **Special Properties:**
   - **dirname**: Used for file input components to specify the directory path.
   - **form**: For grouping related inputs into a form.

### Example Usage (Pseudo-code)

```python
input_config = {
    "auto_complete": False,
    "auto_focus": True,
    "default_value": "Default Value",
    "dirname": "/path/to/directory",
    "disabled": False,
    "form": "my_form",
    "max_length": 100,
    "min_length": 5,
    "name": "user_input",
    "placeholder": "Enter your name here",
    "read_only": True,
    "required": True,
    "rows": "4",
    "value": "",
    "wrap": "soft"
}
```

### Notes:
- **auto_complete**: If `True`, the input will show suggestions as you type.
- **auto_focus**: If `True`, the input field will automatically receive focus when the page loads.
- **default_value**: The initial value shown in the input box.
- **dirname**: Used for file input to specify a directory path.
- **disabled**: If `True`, the user cannot interact with the input.
- **form**: Group inputs under a form name.
- **max_length** and **min_length**: Limits on the length of the input value.
- **name**: The name attribute used in forms.
- **placeholder**: Placeholder text to guide users.
- **read_only**: If `True`, the user can view but not edit the input.
- **required**: If `True`, the field must be filled out before submitting a form.
- **rows**: Number of rows for multi-line inputs.
- **value**: Current value of the input, updated as the user types.
- **wrap**: How text is wrapped in a multi-line input.

This structure ensures that you can configure your input component precisely according to your needs. If you have any specific questions or need further assistance with these properties, feel free to ask!

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

## Trigger | Description
- `on_focus` | Function or event handler called when the element (or some element inside of it) receives focus. For example, it is called when the user clicks on a text input.
- `on_blur` | Function or event handler called when focus has left the element (or left some element inside of it). For example, it is called when the user clicks outside of a focused text input.
- `on_change` | Function or event handler called when the value of an element has changed. For example, it is called when the user types into a text input each keystroke triggers the on change.
- `on_key_down` | The on_key_down event handler is called when the user presses a key.
- `on_key_up` | The on_key_up event handler is called when the user releases a key.