# Progress

Progress is used to display the progress status for a task that takes a long time or consists of several steps.

[Basic Example](https://reflex.dev/docs/library/data-display/progress/#basic-example)

# Basic Example

_rx.progress_ expects the _value_ prop to set the progress value. _width_ is default to 100%, the width of its parent component.

- Progress: 0%
- Progress: 50%
- Progress: 100%

```python
rx.vstack(
    rx.progress(value=0),
    rx.progress(value=50),
    rx.progress(value=100),
)
```

For a dynamic progress, you can assign a state variable to the _value_ prop instead of a constant value.

- Progress: 0%
- [Start]

```python
import asyncio

class ProgressState(rx.State):
    value: int = 0

    @rx.event(background=True)
    async def start_progress(self):
        async with self:
            self.value = 0
        while self.value < 100:
            await asyncio.sleep(0.1)
            async with self:
                self.value += 1

def live_progress():
    return rx.hstack(
        rx.progress(value=ProgressState.value),
        rx.button("Start", on_click=ProgressState.start_progress),
        width="50%",
    )
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/data-display/progress/#api-reference">Learn More</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/progress/#rx.progress)

# rx.progress
A progress bar component.

## Progress Bar Example

```html
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
  <div aria-valuemax="100" aria-valuemin="0" aria-valuenow="50" aria-valuetext="50%" class="rt-ProgressRoot rt-r-size-1 rt-variant-classic css-8atqhb" data-accent-color="tomato" data-max="100" data-radius="none" data-state="loading" data-value="50" role="progressbar" style="--progress-value:50">
    <div class="rt-ProgressIndicator" data-max="100" data-state="loading" data-value="50"></div>
  </div>
</div>
```

## Properties

| Prop         | Type | Values            | Default | Interactive |
| ------------ | ---- | ----------------- | ------- | ---------- |
| `value`      | int  | -                 | -       | -          |
| `max`        | int  | -                 | -       | -          |
| `size`       | "1" | "2" | ...             | 1       | -          |
| `variant`    | "classic" | "surface" | ...     | classic   | -          |
| `color_scheme` | "tomato" | "red" | ...      | tomato    | -          |
| `high_contrast` | bool  | -                 | False   | -          |
| `radius`     | "none" | "small" | ...       | none     | -          |
| `duration`   | str  | -                 | -       | -          |
| `fill_color` | str  | -                 | -       | -          |

Note: The values and descriptions are based on the provided metadata.

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)