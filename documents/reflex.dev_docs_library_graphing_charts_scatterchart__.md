# Scatter Chart

A scatter chart always has two value axes to show one set of numerical data along a horizontal (value) axis and another set of numerical values along a vertical (value) axis. The chart displays points at the intersection of an x and y numerical value, combining these values into single data points.

[Simple Example](https://reflex.dev/docs/library/graphing/charts/scatterchart/#simple-example)

# Simple Example

For a scatter chart we must define an `rx.recharts.scatter()` component for each set of values we wish to plot. Each `rx.recharts.scatter()` component has a `data` prop which clearly states which data source we plot. We also must define `rx.recharts.x_axis()` and `rx.recharts.y_axis()` so that the graph knows what data to plot on each axis.

```python
def scatter_simple():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data01,
            fill="#8884d8",
        ),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        width="100%",
        height=300,
    )
```

[Code](https://reflex.dev/docs/library/graphing/charts/scatterchart/#multiple-scatters)

# Multiple Scatters

We can also add two scatters on one chart by using two `rx.recharts.scatter()` components, and we can define an `rx.recharts.z_axis()` which represents a third column of data and is represented by the size of the dots in the scatter plot.

To learn how to use the `x_axis_id` and `y_axis_id` props, check out the Multiple Axis section of the area chart [documentation](/docs/library/graphing/charts/areachart/).

```python
def scatter_double():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data01, fill="#8884d8", name="A"
        ),
        rx.recharts.scatter(
            data=data02, fill="#82ca9d", name="B"
        ),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        rx.recharts.z_axis(
            data_key="z", range=[60, 400], name="score"
        ),
        rx.recharts.legend(),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=300,
    )
```

To see the dynamic data for this scatter chart, you can check out the [documentation](https://reflex.dev/docs/library/graphing/charts/scatterchart/#dynamic-data).

# Dynamic Data

Chart data tied to a State var causes the chart to automatically update when the state changes, providing a nice way to visualize data in response to user interface elements. View the "Data" tab to see the substate driving this calculation of iterations in the Collatz Conjecture for a given starting number. Enter a starting number in the box below the chart to recalculate.

<form>
  <div class="rt-TextFieldRoot rt-r-size-2 rt-variant-surface">
    <input id="start" placeholder="Enter a number" spellcheck="false"/>
  </div>
  <button type="submit">Compute</button>
</form>

```python
class ScatterChartState(rx.State):
    data: list[dict[str, int]] = []

    @rx.event
    def compute_collatz(self, form_data: dict) -> int:
        n = int(form_data.get("start") or 1)
        yield rx.set_value("start", "")
        self.data = []
        for ix in range(400):
            self.data.append({"x": ix, "y": n})
            if n == 1:
                break
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1

def scatter_dynamic():
    return rx.vstack(
        rx.recharts.scatter_chart(
            rx.recharts.scatter(data=ScatterChartState.data, fill="#8884d8"),
            rx.recharts.x_axis(data_key="x", type_="number"),
            rx.recharts.y_axis(data_key="y", type_="number")
        ),
        rx.form.root(
            rx.input(placeholder="Enter a number", id="start"),
            rx.button("Compute", type="submit"),
            on_submit=ScatterChartState.compute_collatz,
            width="100%",
            height="15em",
            on_mount=ScatterChartState.compute_collatz({"start": "15"})
        )
    )
```

# Legend Type and Shape

## Legend Type: 
[Select](#)

Shape: 
[Select](#)

```python
class ScatterChartState2(rx.State):
    legend_types: list[str] = [
        "square",
        "circle",
        "cross",
        "diamond",
        "star",
        "triangle",
        "wye",
    ]
    
    legend_type: str = "circle"
    
    shapes: list[str] = [
        "square",
        "circle",
        "cross",
        "diamond",
        "star",
        "triangle",
        "wye",
    ]
    
    shape: str = "circle"
    
    data01 = [
        {"x": 100, "y": 200, "z": 200},
        {"x": 120, "y": 100, "z": 260},
        {"x": 170, "y": 300, "z": 400},
        {"x": 170, "y": 250, "z": 280},
        {"x": 150, "y": 400, "z": 500},
        {"x": 110, "y": 280, "z": 200},
    ]

def scatter_shape():
    return rx.vstack(
        rx.recharts.scatter_chart(
            rx.recharts.scatter(
                data=data01,
                fill="#8884d8",
                legend_type=ScatterChartState2.legend_type,
                shape=ScatterChartState2.shape,
            ),
            rx.recharts.x_axis(data_key="x", type_="number"),
            rx.recharts.y_axis(data_key="y"),
            rx.recharts.legend(),
            width="100%",
            height=300,
        ),
        rx.hstack(
            rx.text("Legend Type: "),
            rx.select(ScatterChartState2.legend_types, value=ScatterChartState2.legend_type, on_change=ScatterChartState2.set_legend_type),
            rx.text("Shape: "),
            rx.select(ScatterChartState2.shapes, value=ScatterChartState2.shape, on_change=ScatterChartState2.set_shape),
        ),
        width="100%",
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/scatterchart/#rx.recharts.scatterchart)

# rx.recharts.ScatterChart

A Scatter chart component in Recharts.

- **Prop**: `margin`
  - **Type | Values**: `Dict[str, Any]`
  - **Default**: `{"top": 5, "right": 5, "bottom": 5, "left": 5}`
- **Prop**: `width`
  - **Type | Values**: `Union[str, int]`
  - **Default**: `Var.create("100%")`
- **Prop**: `height`
  - **Type | Values**: `Union[str, int]`
  - **Default**: `Var.create("100%")`

# Valid Children
- LabelList
- ErrorBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.recharts.Scatter

A Scatter component in Recharts.

## Props

- **Prop** | **Type | Values** | **Default**
- `data` | Sequence | -
- `name` | str | -
- `legend_type` | "line" | "plainline" | ... | "circle"
- `x_axis_id` | Union[str, int] | 0
- `y_axis_id` | Union[str, int] | 0
- `z_axis_id` | Union[str, int] | 0
- `line` | bool | False
- `shape` | "square" | "circle" | ... | "circle"
- `line_type` | "joint" | "fitting" | "joint"
- `fill` | Union[str, Color] | rx.color("accent", 9)
- `is_animation_active` | bool | True in CSR, False in SSR
- `animation_begin` | int | 0
- `animation_duration` | int | 1500
- `animation_easing` | "ease" | "ease-in" | ... | "ease"

# Valid Children
- LabelList
- ErrorBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)