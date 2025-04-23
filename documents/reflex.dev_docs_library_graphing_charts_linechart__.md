# Line Chart

A line chart is a type of chart used to show information that changes over time. Line charts are created by plotting a series of several points and connecting them with a straight line.

[Simple Example](https://reflex.dev/docs/library/graphing/charts/linechart/#simple-example)

# Simple Example

For a line chart we must define an `rx.recharts.line()` component for each set of values we wish to plot. Each `rx.recharts.line()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `pv` and `uv` as separate lines against the `name` column which we set as the `data_key` in `rx.recharts.x_axis`.

In the chart below, two lines represent different metrics (`pv` and `uv`) plotted against a categorical variable (`name`).

```python
def line_simple():
    return rx.recharts.line_chart(
        rx.recharts.line(data_key="pv"),
        rx.recharts.line(data_key="uv"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=300
    )
```

![Line Chart](https://reflex.dev/docs/library/graphing/charts/linechart/simple-example.png)

For more details, see the [example with props](https://reflex.dev/docs/library/graphing/charts/linechart/#example-with-props).

# Example with Props

Our second example uses exactly the same data as our first example, except now we add some extra features to our line graphs. We add a `type_` prop to `rx.recharts.line` to style the lines differently. In addition, we add an `rx.recharts.cartesian_grid` to get a grid in the background, an `rx.recharts.legend` to give us a legend for our graphs and an `rx.recharts.graphing_tooltip` to add a box with text that appears when you pause the mouse pointer on an element in the graph.

The example code is as follows:

```python
def line_features():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="pv",
            type_="monotone",
            stroke="#8884d8"
        ),
        rx.recharts.line(
            data_key="uv",
            type_="monotone",
            stroke="#82ca9d"
        ),
        rx.rechts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        data=data,
        width="100%",
        height=300
    )
```

For more details, you can refer to the [official documentation](https://reflex.dev/docs/library/graphing/charts/linechart/#layout).

# Layout

The `layout` prop allows you to set the orientation of the graph to be vertical or horizontal. The `margin` prop defines the spacing around the graph.

Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.

```python
def line_vertical():
    return rx.recharts.line_chart(
        rx.recharts.line(data_key="pv", stroke=rx.color("accent", 9)),
        rx.recharts.line(data_key="uv", stroke=rx.color("green", 9)),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category"),
        layout="vertical",
        margin={
            "top": 20,
            "right": 20,
            "left": 20,
            "bottom": 20,
        },
        data=data,
        height=300,
        width="100%",
    )
```

Learn more about dynamic data in the [Reflex Line Chart documentation](https://reflex.dev/docs/library/graphing/charts/linechart/#dynamic-data).

# Dynamic Data

Chart data can be modified by tying the `data` prop to a State var. Most other props, such as `type_`, can be controlled dynamically as well. In the following example the "Munge Data" button can be used to randomly modify the data, and the two `select` elements change the line `type_`. Since the data and style is saved in the per-browser-tab State, the changes will not be visible to other visitors.

The initial data is set as follows:

```python
initial_data = data

class LineChartState(rx.State):
    data: list[dict[str, Any]] = initial_data
    pv_type: str = "monotone"
    uv_type: str = "monotone"

    @rx.event
    def munge_data(self):
        for row in self.data:
            row["uv"] += random.randint(-500, 500)
            row["pv"] += random.randint(-1000, 1000)

def line_dynamic():
    return rx.vstack(
        rx.recharts.line_chart(
            rx.recharts.line(data_key="pv", type_=LineChartState.pv_type, stroke="#8884d8"),
            rx.recharts.line(data_key="uv", type_=LineChartState.uv_type, stroke="#82ca9d"),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=LineChartState.data,
            margin={"top": 20, "right": 20, "left": 20, "bottom": 20},
            width="100%",
            height=300
        ),
        rx.hstack(
            rx.button("Munge Data", on_click=LineChartState.munge_data),
            rx.select(["monotone", "linear", "step", "stepBefore", "stepAfter"], value=LineChartState.pv_type, on_change=LineChartState.set_pv_type),
            rx.select(["monotone", "linear", "step", "stepBefore", "stepAfter"], value=LineChartState.uv_type, on_change=LineChartState.set_uv_type)
        ),
        width="100%"
    )
```

To learn how to use the `sync_id`, `x_axis_id` and `y_axis_id` props check out the area chart [documentation](/docs/library/graphing/charts/areachart/), where these props are all described with examples.

[Documentation Link](https://reflex.dev/docs/library/graphing/charts/linechart/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/linechart/#rx.recharts.linechart)

# rx.recharts.LineChart

A Line chart component in Recharts.

## Props

- **Prop** | **Type | Values** | **Default**
- `data` | Sequence | -
- `margin` | Dict\[str, Any\] | -
- `sync_id` | str | -
- `sync_method` | `"index" | "value"` | `"index"`
- `layout` | `"vertical" | "horizontal"` | `"horizontal"`
- `stack_offset` | `"expand" | "none" | ...` | -
- `width` | Union\[str, int\] | Var.create("100%")
- `height` | Union\[str, int\] | Var.create("100%")

# Valid Children
- LabelList
- ErrorBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_animation_start`
  - Description: The customized event handler of animation start

- **Trigger**: `on_animation_end`
  - Description: The customized event handler of animation end

# rx.recharts.Line

A Line component in Recharts.

## Props

- **type_**
  - Type: `"basis" | "basisClosed" | ...`
  - Default: None

- **stroke**
  - Type: `Union[str, Color]`
  - Default: `rx.color("accent", 9)`

- **stroke_width**
  - Type: `int`
  - Default: `1`

- **dot**
  - Type: `Union[dict, bool]`
  - Default: `{"stroke": rx.color("accent", 10), "fill": rx.color("accent", 4)}`

- **active_dot**
  - Type: `Union[dict, bool]`
  - Default: `{"stroke": rx.color("accent", 2), "fill": rx.color("accent", 10)}`

- **label**
  - Type: `bool`
  - Default: `False`

- **hide**
  - Type: `bool`
  - Default: `False`

- **connect_nulls**
  - Type: `bool`
  - Default: None

- **unit**
  - Type: `Union[str, int]`
  - Default: None

- **points**
  - Type: `Sequence`
  - Default: None

- **stroke_dasharray**
  - Type: `str`
  - Default: None

- **layout**
  - Type: `"vertical" | "horizontal"`
  - Default: None

- **data_key**
  - Type: `Union[str, int]`
  - Default: None

- **x_axis_id**
  - Type: `Union[str, int]`
  - Default: `0`

- **y_axis_id**
  - Type: `Union[str, int]`
  - Default: `0`

- **legend_type**
  - Type: `"line" | "plainline" | ...`
  - Default: None

- **is_animation_active**
  - Type: `bool`
  - Default: `True`

- **animation_begin**
  - Type: `int`
  - Default: `0`

- **animation_duration**
  - Type: `int`
  - Default: `1500`

- **animation_easing**
  - Type: `"ease" | "ease-in" | ...`
  - Default: `"ease"`

- **name**
  - Type: `Union[str, int]`
  - Default: None

# Valid Children
- LabelList
- ErrorBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_animation_start`
  - Description: The customized event handler of animation start
  
- **Trigger:** `on_animation_end`
  - Description: The customized event handler of animation end