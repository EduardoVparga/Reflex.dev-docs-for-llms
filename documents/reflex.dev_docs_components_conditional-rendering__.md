# Conditional Rendering

Recall from the [basics](/docs/getting-started/basics/) that we cannot use Python `if/else` statements when referencing state vars in Reflex. Instead, use the `rx.cond` component to conditionally render components or set props based on the value of a state var.

# Video: Conditional Rendering

Check out the API reference for [cond docs](/docs/library/dynamic-rendering/cond/).

Below is a simple example showing how to toggle between two text components by checking the value of the state var `show`.

Toggle
------

Text 1

```python
class CondSimpleState(rx.State):
    show: bool = True

@rx.event
def change(self):
    self.show = not (self.show)

def cond_simple_example():
    return rx.vstack(
        rx.button("Toggle", on_click=CondSimpleState.change),
        rx.cond(
            CondSimpleState.show,
            rx.text("Text 1", color="blue"),
            rx.text("Text 2", color="red"),
        ),
    )
```

If `show` is `True`, then the first component is rendered (in this case the blue text). Otherwise the second component is rendered (in this case the red text).

[Conditional Props](https://reflex.dev/docs/components/conditional-rendering/#conditional-props)

# Conditional Props

You can also set props conditionally using `rx.cond`. In this example, we set the `color` prop of a text component based on the value of the state var `show`.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <!-- Slider component is represented as a placeholder -->
    </div>
</div>

```python
class PropCondState(rx.State):
    value: int

    @rx.event
    def set_end(self, value: list[int]):
        self.value = value[0]

def cond_prop():
    return rx.slider(
        default_value=[50],
        on_value_commit=PropCondState.set_end,
        color_scheme=rx.cond(PropCondState.value > 50, "green", "pink"),
        width="100%",
    )
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/components/conditional-rendering/#var-operations">Learn more</a>

# Var Operations

You can use [var operations](/docs/vars/var-operations/) with the `cond` component for more complex conditions. See the full [cond reference](/docs/library/dynamic-rendering/cond/) for more details.

# Multiple Conditional Statements

The `rx.match` component in Reflex provides a powerful alternative to `rx.cond` for handling multiple conditional statements and structural pattern matching. This component allows you to handle multiple conditions and their associated components in a cleaner and more readable way compared to nested `rx.cond` structures.

Unknown cat breed selected.
<button aria-autocomplete="none" aria-controls="radix-:Rkomkml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface" data-placeholder="" data-state="closed" dir="ltr" role="combobox" type="button">
<span class="rt-SelectTriggerInner"><span style="pointer-events:none"></span></span>
<svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9" xmlns="http://www.w3.org/2000/svg">
<path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path>
</svg>
</button>

```python
from typing import List

import reflex as rx

class MatchState(rx.State):
    cat_breed: str = ""
    animal_options: List[str] = [
        "persian",
        "siamese",
        "maine coon",
        "ragdoll",
        "pug",
        "corgi"
    ]

def match_demo():
    return rx.flex(
        rx.match(
            MatchState.cat_breed,
            ("persian", rx.text("Persian cat selected.")),
            ("siamese", rx.text("Siamese cat selected.")),
            (
                "maine coon",
                rx.text("Maine Coon cat selected.")
            ),
            ("ragdoll", rx.text("Ragdoll cat selected.")),
            rx.text("Unknown cat breed selected."),
        ),
        rx.select(
            [
                "persian",
                "siamese",
                "maine coon",
                "ragdoll",
                "pug",
                "corgi"
            ],
            value=MatchState.cat_breed,
            on_change=MatchState.set_cat_breed,
            direction="column",
            gap="2"
        ),
    )
```