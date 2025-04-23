# Component State

New in version 0.4.6.

Defining a subclass of `rx.ComponentState` creates a special type of state that is tied to an instance of a component, rather than existing globally in the app. A Component State combines UI code with state Vars and Event Handlers, and is useful for creating reusable components which operate independently of each other.

[Using ComponentState](https://reflex.dev/docs/substates/component-state/#using-componentstate)

# Using ComponentState

## Using `ReusableCounter`

```python
class ReusableCounter(rx.ComponentState):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

    @rx.event
    def decrement(self):
        self.count -= 1

    @classmethod
    def get_component(cls, **props):
        return rx.hstack(
            rx.button("Decrement", on_click=cls.decrement),
            rx.text(cls.count),
            rx.button("Increment", on_click=cls.increment),
            **props,
        )
```

```python
reusable_counter = ReusableCounter.create()
```

```python
def multiple_counters():
    return rx.vstack(
        reusable_counter(),
        reusable_counter(),
        reusable_counter(),
    )
```

### Explanation

- The variables and event handlers defined on the `ReusableCounter` class are scoped to the component instance.
- Each time a `reusable_counter` is created, a new state class for that instance of the component is also created.
- The `get_component` classmethod is used to define the UI for the component and link it up to the State.

### Notes

- The `cls` argument in the `get_component` method refers to the unique instance of `ComponentState` for the component being returned.
- Other states may also be referenced by the returned component, but `cls` will always refer to the specific instance of `ComponentState`.

# Passing Props

Similar to a normal Component, the `ComponentState.create` classmethod accepts the arbitrary
`*children` and `**props` arguments, and by default passes them to your `get_component` classmethod.
These arguments may be used to customize the component, either by applying defaults or
passing props to certain subcomponents.

In the following example, we implement an editable text component that allows the user to click on
the text to turn it into an input field. If the user does not provide their own `value` or `on_change`
props, then the defaults defined in the `EditableText` class will be used.

Click to edit  
Edit me!  
Reflex is fun

```python
class EditableText(rx.ComponentState):
    text: str = "Click to edit"
    original_text: str
    editing: bool = False

    @rx.event
    def start_editing(self, original_text: str):
        self.original_text = original_text
        self.editing = True

    @rx.event
    def stop_editing(self):
        self.editing = False
        self.original_text = ""

    @classmethod
    def get_component(cls, **props):
        # Pop component-specific props with defaults before passing **props
        value = props.pop("value", cls.text)
        on_change = props.pop("on_change", cls.set_text)
        cursor = props.pop("cursor", "pointer")

        # Set the initial value of the State var.
        initial_value = props.pop("initial_value", None)
        if initial_value is not None:
            # Update the pydantic model to use the initial value as default.
            cls.__fields__["text"].default = initial_value

        # Form elements for editing, saving and reverting the text.
        edit_controls = rx.hstack(
            rx.input(
                value=value,
                on_change=on_change,
                **props,
            ),
            rx.icon_button(
                rx.icon("x"),
                on_click=[
                    on_change(cls.original_text),
                    cls.stop_editing,
                ],
                type="button",
                color_scheme="red",
            ),
            rx.icon_button(rx.icon("check"), align="center", width="100%"),
        )

        # Return the text or the form based on the editing Var.
        return rx.cond(
            cls.editing,
            rx.form(
                edit_controls,
                on_submit=lambda _: cls.stop_editing(),
            ),
            rx.text(
                value,
                on_click=cls.start_editing,
                cursor=cursor,
                **props,
            ),
        )

editable_text = EditableText.create

def editable_text_example():
    return rx.vstack(
        editable_text(),
        editable_text(initial_value="Edit me!", color="blue"),
        editable_text(initial_value="Reflex is fun", font_family="monospace", width="100%"),
    )
```

Because this `EditableText` component is designed to be reusable, it can handle the case
where the `value` and `on_change` are linked to a normal global state.

Global state text  
GLOBAL STATE TEXT

```python
class EditableTextDemoState(rx.State):
    value: str = "Global state text"

def editable_text_with_global_state():
    return rx.vstack(
        editable_text(
            value=EditableTextDemoState.value,
            on_change=EditableTextDemoState.set_value,
        ),
        rx.text(EditableTextDemoState.value.upper()),
    )
```

[Accessing the State](https://reflex.dev/docs/substates/component-state/#accessing-the-state)

# Accessing the State

The underlying state class of a `ComponentState` is accessible via the `.State` attribute. To use it, assign an instance of the component to a local variable, then include that instance in the page.

Total: 0  
[Decrement](#) | 0 | [Increment](#)  
[Decrement](#) | 0 | [Increment](#)

```python
def counter_sum():
    counter1 = reusable_counter()
    counter2 = reusable_counter()
    return rx.vstack(
        rx.text(f"Total: {counter1.State.count + counter2.State.count}"),
        counter1,
        counter2,
    )
```

Other components can also affect a `ComponentState` by referencing its event handlers or vars via the `.State` attribute.

[Decrement](#) | 0 | [Increment](#)  
[<svg class="lucide lucide-step-back css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><line x1="18" x2="18" y1="20" y2="4"></line><polygon points="14,20 4,12 14,4"></polygon></svg>](#) | [Plus](#) | [Double](#) | [Triple](#)

```python
def extended_counter():
    counter1 = reusable_counter()
    return rx.vstack(
        counter1,
        rx.hstack(
            rx.icon_button(rx.icon("step_back"), on_click=counter1.State.set_count(0)),
            rx.icon_button(rx.icon("plus"), on_click=counter1.State.increment),
            rx.button("Double", on_click=lambda: counter1.State.set_count(counter1.State.count * 2)),
            rx.button("Triple", on_click=lambda: counter1.State.set_count(counter1.State.count * 3)),
        ),
    )
```