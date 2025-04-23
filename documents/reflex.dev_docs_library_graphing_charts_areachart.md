# Area Chart

A Recharts area chart displays quantitative data using filled areas between a line connecting data points and the axis.

[Learn More](https://reflex.dev/docs/library/graphing/charts/areachart/#basic-example)

# Basic Example

## Code

```python
def area_simple():
    return rx.recharts.area_chart(
        rx.recharts.area(data_key="uv"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=250,
    )
```

[Link to Reflex documentation](https://reflex.dev/docs/library/graphing/charts/areachart/#syncing-charts)

# Syncing Charts

The `sync_id` prop allows you to sync two graphs. In the example, it is set to "1" for both charts, indicating that they should be synchronized. This means that any interactions (such as brushing) performed on one chart will be reflected in the other chart.

## Example Code

```python
def area_sync():
    return rx.vstack(
        rx.recharts.bar_chart(
            rx.recharts.graphing_tooltip(),
            rx.recharts.bar(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8"
            ),
            rx.recharts.bar(
                data_key="pv",
                stroke="#82ca9d",
                fill="#82ca9d"
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=data,
            sync_id="1",
            width="100%",
            height=200
        ),
        rx.recharts.composed_chart(
            rx.recharts.area(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8"
            ),
            rx.recharts.line(
                data_key="pv",
                type_="monotone",
                stroke="#ff7300"
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(),
            rx.recharts.brush(
                data_key="name", height=30, stroke="#8884d8"
            ),
            data=data,
            sync_id="1",
            width="100%",
            height=250
        )
    )
```

## Data

```python
data = [
    {"name": "Page A", "uv": 39, "pv": 47},
    {"name": "Page B", "uv": 36, "pv": 18},
    # ... (remaining data entries)
]
```

# Stacking Charts

The `stack_id` prop allows you to stack multiple graphs on top of each other. In the example, it is set to "1" for both charts, indicating that they should be stacked together. This means that the bars or areas of the charts will be vertically stacked, with the values of each chart contributing to the total height of the stacked areas or bars.

This is similar to the `sync_id` prop, but instead of synchronizing the interaction between the charts, it just stacks the charts on top of each other.

The following code demonstrates how to create a stacked area chart:

```python
def area_stack():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
            stack_id="1",
        ),
        rx.recharts.area(
            data_key="pv",
            stroke=rx.color("green", 9),
            fill=rx.color("green", 8),
            stack_id="1",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        stack_offset="none",
        margin={
            "top": 5,
            "right": 5,
            "bottom": 5,
            "left": 5,
        },
        width="100%",
        height=300,
    )
```

For more details and examples, you can refer to the official documentation: [Reflex Dev Graphing Charts Documentation](https://reflex.dev/docs/library/graphing/charts/areachart/#multiple-axis)

# Multiple Axis

Multiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.

## Code

```python
def area_multi_axis():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke="#8884d8",
            fill="#8884d8",
            x_axis_id="primary",
            y_axis_id="left",
        ),
        rx.recharts.area(
            data_key="pv",
            x_axis_id="secondary",
            y_axis_id="right",
            type_="monotone",
            stroke="#82ca9d",
            fill="#82ca9d",
        ),
        rx.recharts.x_axis(data_key="name", x_axis_id="primary"),
        rx.recharts.x_axis(data_key="name", x_axis_id="secondary", orientation="top"),
        rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
        rx.recharts.y_axis(data_key="pv", y_axis_id="right", orientation="right"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        data=data,
        width="100%",
        height=300,
    )
```

## Data

No data provided.

# Layout

Use the `layout` prop to set the orientation to either `"horizontal"` (default) or `"vertical"`.

## Information

Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.

## Area Chart Example

The following is an example of a vertical area chart:

- **Code**

```python
def area_vertical():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 8),
            fill=rx.color("accent", 3),
        ),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(
            data_key="name", type_="category"
        ),
        data=data,
        layout="vertical",
        height=300,
        width="100%",
    )
```

- **Data**
  - This section is hidden and will be populated with the actual data when needed.

# Stateful Example

Here is an example of an area graph with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data for both graphs when the first defined `area` is clicked on using `on_click=AreaState.randomize_data`.

Curve Type:
- basis

![Area Chart](https://via.placeholder.com/140x400)

```python
class AreaState(rx.State):
    data = data
    curve_type = ""

    @rx.event
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

    def change_curve_type(self, type_input):
        self.curve_type = type_input

def area_stateful():
    return rx.vstack(
        rx.hstack(
            rx.text("Curve Type:"),
            rx.select(["basis", "natural", "step"], on_change=AreaState.change_curve_type, default_value="basis"),
        ),
        rx.recharts.area_chart(
            rx.recharts.area(data_key="uv", on_click=AreaState.randomize_data, type_=AreaState.curve_type),
            rx.recharts.area(data_key="pv", stroke="#82ca9d", fill="#82ca9d", on_click=AreaState.randomize_data, type_=AreaState.curve_type),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            rx.recharts.cartesian_grid(),
            data=AreaState.data,
            width="100%",
            height="400",
        ),
        width="100%",
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/areachart/#rx.recharts.areachart)

-

# rx.recharts.AreaChart

An Area chart component in Recharts.

## Props

- **Prop** | **Type | Values** | **Default**
  - `base_value` | `"dataMin" | "dataMax" | ...` | `"auto"`
  - `data` | `Sequence` | -
  - `margin` | `Dict[str, Any]` | -
  - `sync_id` | `str` | -
  - `sync_method` | `"index" | "value"` | `"index"`
  - `layout` | `"vertical" | "horizontal"` | `"horizontal"`
  - `stack_offset` | `"expand" | "none" | ...` | -
  - `width` | `Union[str, int]` | `Var.create("100%")`
  - `height` | `Union[str, int]` | `Var.create("100%")`

# Valid Children
LabelList

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_animation_start`
  - Description: The customized event handler of animation start

- **Trigger:** `on_animation_end`
  - Description: The customized event handler of animation end

# rx.recharts.Area

An Area component in Recharts.

## Props

- **stroke**
  - Type: `Union[str, Color]`
  - Default: `rx.color("accent", 9)`
  
- **stroke_width**
  - Type: `int`
  - Default: `1`

- **fill**
  - Type: `Union[str, Color]`
  - Default: `rx.color("accent", 5)`

- **type_**
  - Type: `"basis" | "basisClosed" | ...`
  - Default: `"monotone"`

- **dot**
  - Type: `Union[dict, bool]`
  - Default: `False`

- **active_dot**
  - Type: `Union[dict, bool]`
  - Default: `{stroke: rx.color("accent", 2), fill: rx.color("accent", 10)}`

- **label**
  - Type: `bool`
  - Default: `False`

- **base_line**
  - Type: `Union[str, Sequence]`
  - Default: None

- **points**
  - Type: `Sequence`
  - Default: None

- **stack_id**
  - Type: `Union[str, int]`
  - Default: None

- **connect_nulls**
  - Type: `bool`
  - Default: `False`

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

- **unit**
  - Type: `Union[str, int]`
  - Default: None

- **name**
  - Type: `Union[str, int]`
  - Default: None

# Valid Children
LabelList

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_animation_start`
  - Description: The customized event handler of animation start
  
- **Trigger**: `on_animation_end`
  - Description: The customized event handler of animation end