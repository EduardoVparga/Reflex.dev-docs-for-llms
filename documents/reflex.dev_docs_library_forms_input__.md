# Input

The `input` component is an input field that users can type into. 

```python
class Input:
    pass
```

<div data-orientation="vertical" data-variant="classic">
<div data-orientation="vertical" data-state="closed">
</div>
</div>

### Video: Input

# Basic Example

The `on_blur` event handler is called when focus has left the `input`, for example, it’s called when the user clicks outside of a focused text input.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
    </div>
</div>

# Heading 1
This is a paragraph.

## Heading 2
- Item 1
- Item 2

### Heading 3
This is another paragraph.

Some *italic* and **bold** text.

Here is a code block:
```python
def hello_world():
    print("Hello, world!")
```

This is a link: [Visit Website](https://example.com)

This is an image reference: ![](image.jpg)

# Hello World!

```
class TextfieldControlled(rx.State):
    text: str = "Hello World!"
    
def controlled_example():
    return rx.vstack(
        rx.heading(TextfieldControlled.text),
        rx.input(
            placeholder="Search here...",
            value=TextfieldControlled.text,
            on_change=TextfieldControlled.set_text,
        ),
    )
```

Behind the scenes, the input component is implemented as a debounced input to avoid sending individual state updates per character to the backend while the user is still typing. This allows a state variable to directly control the `value` prop from the backend without the user experiencing input lag.

[Learn More](https://reflex.dev/docs/library/forms/input/#submitting-a-form-using-input)

# Submitting a form using input

The `name` prop is needed to submit with its owning form as part of a name/value pair.

When the `required` prop is `True`, it indicates that the user must input text before the owning form can be submitted.

The `type` is set here to `password`. The element is presented as a one-line plain text editor control in which the text is obscured so that it cannot be read. The `type` prop can take any value of `email`, `file`, `password`, `text` and several others. Learn more [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

```html
<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-reset rt-BaseCard rt-Card rt-r-size-1 rt-variant-surface css-11ze7cv">
            <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1lni6sm"></div>
        </div>
    </div>
</div>
```

# Example Form

Enter text...
Submit

---

# Results:
{}`

```python
class FormInputState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_input1():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.hstack(
                    rx.input(name="input", placeholder="Enter text...", type="text", required=True),
                    rx.button("Submit", type="submit"),
                    width="100%",
                ),
                on_submit=FormInputState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"), 
                rx.badge(FormInputState.form_data.to_string())
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )
```

To learn more about how to use forms in the [Form](/docs/library/forms/form/) docs.

[Learn More →](https://reflex.dev/docs/library/forms/input/#setting-a-value-without-using-a-state-var)

# Setting a value without using a State var

Set the value of the specified reference element, without needing to link it up to a State var. This is an alternate way to modify the value of the `input`.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
      <input id="input1" spellcheck="false"/>
      <button data-accent-color="">Erase</button>
    </div>
  </div>
  <div class="rt-Box relative mb-4">
    <pre>
rx.hstack(
    rx.input(id="input1"),
    rx.button("Erase", on_click=rx.set_value("input1", ""))
)
    </pre>
  </div>
</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/input/#rx.input)

It looks like you're dealing with a detailed table of properties and their types for some kind of form or input component, possibly from a library like Radix UI. Here's a summary of the main properties listed in your snippet:

### Properties Summary

#### General Properties
- **checked**: A boolean to indicate if an element is checked.
- **default_checked**: The default value for the `checked` property.

#### Form Properties
- **form**: Specifies the form associated with the input.
- **form_action**: The URL of the form to be submitted.
- **form_enc_type**: The encoding type used when submitting a form (e.g., "application/x-www-form-urlencoded", "multipart/form-data").
- **form_method**: The HTTP method for submitting the form (GET, POST).
- **form_no_validate**: A boolean indicating whether the form should not validate on submission.
- **form_target**: Specifies where to display the response after submitting a form.

#### Input Properties
- **multiple**: A boolean that allows multiple selections in input types like `<select>` or `<input type="file">`.
- **pattern**: A regular expression used for client-side validation of an input field.
- **min**, **max**: Specify minimum and maximum values for numeric inputs (e.g., `<input type="number">`).
- **step**: The step size that a user can increment the value by.
- **src**: Specifies the URL of an image to be used in certain elements like `<img>` or `<picture>`.

#### Button Properties
- **checked**: Boolean indicating if a checkbox or radio button is checked.
- **default_checked**: Default boolean for the `checked` property of checkboxes/radio buttons.
- **form**: The form associated with the input/button.
- **form_action**, **form_enc_type**, **form_method**, **form_no_validate**, **form_target**: Similar to general form properties but specific to a button.

#### Select Properties
- **multiple**: Allows multiple selections in `<select>` elements.
- **checked**: Boolean indicating if an option is checked.
- **default_checked**: Default boolean for the `checked` property of options.

#### Date Input Properties
- **min**, **max**: Specify minimum and maximum dates.
- **step**: The step size for date increments.
- **pattern**: A regular expression used for validation (though not typically used for `<input type="date">`).

### Additional Controls
- **Select Trigger**:
  - Allows users to trigger a dropdown menu with options. It includes an icon and can be expanded or collapsed.

#### Validation and Form Handling
- Several properties like `form_no_validate`, `form_method`, etc., are used for form handling and validation.
  
### Notes
1. The table is quite extensive, covering various aspects of form controls, including input types (text, number, date), buttons, and select elements.
2. Properties like `pattern` and `min/max` are specific to certain input types and can be used for client-side validation.

If you need more detailed information on any specific property or how they work together in a real-world scenario, feel free to ask!

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.input.slot

Contains icons or buttons associated with an Input.

## Search the Docs

```html
<input class="rt-reset rt-TextFieldInput" placeholder="Search the docs" spellcheck="false"/>
```

### Properties

| Prop          | Type | Default | Interactive |
|---------------|------|---------|------------|
| color_scheme  | "tomato" | -      | <button>tomato</button> |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)