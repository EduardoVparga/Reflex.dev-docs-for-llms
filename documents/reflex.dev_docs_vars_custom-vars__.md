# Custom Vars

As mentioned in the [vars page](/docs/vars/base-vars), Reflex vars must be JSON serializable.

This means we can support any Python primitive types, as well as lists, dicts, and tuples. However, you can also create more complex var types by inheriting from `rx.Base` or decorating them as dataclasses with `@dataclasses.dataclass`.

[Defining a Type](/docs/vars/custom-vars/#defining-a-type)

# Defining a Type

In this example, we will create a custom var type for storing translations.

Once defined, we can use it as a state var, and reference it from within a component.

```python
import googletrans

class Translation(rx.Base):
    original_text: str
    translated_text: str

class TranslationState(rx.State):
    input_text: str = "Hola Mundo"
    current_translation: Translation = Translation(
        original_text="",
        translated_text=""
    )

    @rx.event
    def translate(self):
        self.current_translation.original_text = (self.input_text)
        self.current_translation.translated_text = (
            googletrans.Translator()\
            .translate(self.input_text, dest="en").text
        )
```

```python
def translation_example():
    return rx.vstack(
        rx.input(
            on_blur=TranslationState.setvar("input_text"),
            default_value=TranslationState.input_text,
            placeholder="Text to translate...",
        ),
        rx.button(
            "Translate", on_click=TranslationState.translate
        ),
        rx.text(TranslationState.current_translation.translated_text),
    )
```

- Input: Text to translate...
- Button: Translate
- Output: Translated text