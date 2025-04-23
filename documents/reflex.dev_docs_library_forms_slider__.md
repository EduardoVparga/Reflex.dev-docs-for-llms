# Slider
Provides user selection from a range of values. The

[Basic Example](https://reflex.dev/docs/library/forms/slider/#basic-example)

# Basic Example

The slider can be controlled by a single value or a range of values. Slider can be hooked to state to control its value. Passing a list of two values creates a range slider.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1tehhj4"></div>
    </div>
</div>

### `reactive_slider` Component Reference

The `reactive_slider` component in Reflex allows you to create interactive sliders that can be used to select a range of values. Below is the detailed reference for this component, including its props and event triggers.

#### Props

- **name**: `str`
  - The name attribute of the slider.
  
- **value**: `Sequence`
  - The current value of the slider (as a list or tuple).
  
- **min** & **max**: `Union[int, float]`
  - The minimum and maximum values that can be selected on the slider.

- **step**: `Union[int, float]`
  - The step size for each tick on the slider.
  
- **default_value**: `Union[Sequence, float, int]`
  - The initial value of the slider when it is first rendered (if not provided by `value` prop).
  
- **width**: `Union[str, NoneType]`
  - The width of the slider. Defaults to "100%".
  
- **disabled**: `bool`
  - Whether the slider should be disabled or not.

- **orientation**: `"horizontal" | "vertical"`
  - The orientation of the slider (either horizontal or vertical).

- **radius**: `"none" | "small" | ...`
  - The border radius for the slider thumb and track.
  
- **highlights**: `Sequence[dict]` (optional)
  - A list of dictionaries representing highlight points on the slider. Each dictionary should contain a `value` key.

- **on_change**: Event Trigger
  - Fired when the value of the slider changes.
  
- **on_value_commit**: Event Trigger
  - Fired when a thumb is released after being dragged, effectively committing the new value to the component's state.

#### Example Usage

```python
from reflex import App, StateVar, command, var
from reflex.components import slider

state = StateVar(value=[50], min=0, max=100)

def on_change(new_value):
    print("Slider value changed:", new_value)
    # You can update the state or perform other actions here.

app = App(state=state)

@app.component
def MyComponent():
    return slider(
        id="my_slider",
        name="slider_name",
        value=state.value,
        min=state.min,
        max=state.max,
        on_change=on_change,
        orientation="horizontal"
    )

if __name__ == "__main__":
    app.compile()
```

#### Event Triggers

- **on_change**: This event is triggered whenever the slider's value changes. You can pass a function to this prop to handle the change.
  
  ```python
  def on_change(new_value):
      print("Slider value changed:", new_value)
  ```

- **on_value_commit**: This event is triggered when a thumb is released after being dragged, effectively committing the new value to the component's state.

#### Customizing the Slider

You can customize various aspects of the slider using props like `min`, `max`, `step`, and `orientation`. Here’s an example with some customizations:

```python
@app.component
def MyComponent():
    return slider(
        id="my_slider",
        name="slider_name",
        value=[30, 70],
        min=10,
        max=90,
        step=5,
        width="400px",
        disabled=False,
        orientation="horizontal",
        on_change=lambda new_value: print("Slider value changed:", new_value),
        on_value_commit=lambda new_value: print("Value committed:", new_value)
    )
```

This example sets the slider to a range between 10 and 90, with steps of 5. It also handles both `on_change` and `on_value_commit` events.

Feel free to explore more props like `highlights` to add additional features such as highlight points on the slider track!

# Range Slider

Range slider is created by passing a list of two values to the `default_value` prop. The list should contain two values that are in the range of the slider.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1tehhj4">
            <div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
                <!-- Content will be here -->
            </div>
        </div>
    </div>
</div>

# 25

# 75

## 25 ## 75 

```python
class RangeSliderState(rx.State):
    value_start: int = 25
    value_end: int = 75
    
    @rx.event
    def set_end(self, value: list[int]):
        self.value_start = value[0]
        self.value_end = value[1]

def range_slider_intro():
    return rx.vstack(
        rx.hstack(
            rx.heading(RangeSliderState.value_start),
            rx.heading(RangeSliderState.value_end),
        ),
        rx.slider(
            default_value=[25, 75],
            min_=0,
            max=100,
            size="1",
            on_value_commit=RangeSliderState.set_end,
        ),
        width="100%",
    )
```

[Live Updating Slider](https://reflex.dev/docs/library/forms/slider/#live-updating-slider)

# Live Updating Slider

You can use the `on_change` prop to update the slider value as you interact with it. The `on_change` prop takes a function that will be called with the new value of the slider.

Here we use the `throttle` method to limit the rate at which the function is called, which is useful to prevent excessive updates. In this example, the slider value is updated every 100ms.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1tehhj4"></div>
    </div>
</div>

# 50

```python
class LiveSliderState(rx.State):
    value: int = 50

    @rx.event
    def set_end(self, value: list[int]):
        self.value = value[0]

def live_slider_intro():
    return rx.vstack(
        rx.heading(LiveSliderState.value),
        rx.slider(
            default_value=50,
            min_=0,
            max=100,
            on_change=LiveSliderState.set_end.throttle(100),
        ),
        width="100%",
    )
```

<button>
<svg class="lucide lucide-copy css-cqk0y8" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg">
<rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect>
<path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>
</svg>
</button>

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/forms/slider/#slider-in-forms">...</a>

# Slider in forms

Here we show how to use a slider in a form. We use the `name` prop to identify the slider in the form data. The form data is then passed to the `handle_submit` method to be processed.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-reset rt-BaseCard rt-Card rt-r-size-1 rt-variant-surface css-11ze7cv">
      <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-1lni6sm"></div>
    </div>
  </div>
</div>

# Example Form

<form>
  <div>
    <span>
      <span>
        <button type="submit">Submit</button>
      </span>
    </span>
  </div>
</form>

<span class="rt-Separator rt-r-orientation-horizontal rt-r-size-4 css-1ezhfzu" data-accent-color="gray"></span>

# Results:
Example Form

```
class FormSliderState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def slider_form_example():
    return rx.card(
        rx.vstack(
            rx.heading("Example Form"),
            rx.form.root(
                rx.hstack(
                    rx.slider(default_value=40, name="slider"),
                    rx.button("Submit", type="submit"),
                    width="100%",
                ),
                on_submit=FormSliderState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results:"), 
                rx.badge(FormSliderState.form_data.to_string())
            ),
            align_items="left",
            width="100%",
        ),
        width="50%",
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/forms/slider/#rx.slider)

# rx.slider

Provides user selection from a range of values.

## Properties

- **as_child**: `bool`
- **size**: `"1" | "2" | ...` (Interactive: [Select](#))
- **variant**: `"classic" | "surface" | ..." (Interactive: [Select](#))
- **color_scheme**: `"tomato" | "red" | ..." (Interactive: [Select](#))
- **high_contrast**: `bool`
- **radius**: `"none" | "small" | ...` (Interactive: [Select](#))
- **default_value**: `Union[Sequence, float, int]`
- **value**: `Sequence`
- **name**: `str`
- **width**: `Union[str, NoneType]` (Default: `Var.create("100%")`)
- **min**: `Union[int, float]`
- **max**: `Union[int, float]`
- **step**: `Union[int, float]`
- **disabled**: `bool`
- **orientation**: `"vertical" | "horizontal"` (Interactive: [Select](#))

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_change`
  - Description: Props to rename Fired when the value of the slider changes.
  
- **Trigger:** `on_value_commit`
  - Description: Fired when a thumb is released after being dragged.