# Area Chart

A Recharts area chart displays quantitative data using filled areas between a line connecting data points and the axis.

[Learn More](https://reflex.dev/docs/library/graphing/charts/areachart/#basic-example)

# Basic Example

[Link](https://reflex.dev/docs/library/graphing/charts/areachart/#syncing-charts)

<div class="w-full py-4 flex flex-col">
  <div class="w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center">
    <svg height="250" width="107">
      <title></title>
      <desc></desc>
      <defs>
        <clippath id="recharts1-clip">
          <rect height="210" width="37" x="65" y="5"></rect>
        </clippath>
      </defs>
      <g class="recharts-layer recharts-area">
        <g class="recharts-layer">
          <path class="recharts-curve recharts-area-area" d="M65,5C99.833,22.5,134.667,40,169.5,57.5C204.333,75,239.167,110,274,110C308.833,110,343.667,69.05,378.5,69.05C413.333,69.05,448.167,115.775,483,115.775C517.833,115.775,552.667,103.525,587.5,89.525C622.333,75.525,657.167,53.65,692,31.775L692,215C657.167,215,622.333,215,587.5,215C552.667,215,517.833,215,483,215C448.167,215,413.333,215,378.5,215C343.667,215,308.833,215,274,215C239.167,215,204.333,215,169.5,215C134.667,215,99.833,215,65,215Z" fill="var(--accent-5)" fill-opacity="0.6"></path>
          <path class="recharts-curve recharts-area-curve" d="M65,5C99.833,22.5,134.667,40,169.5,57.5C204.333,75,239.167,110,274,110C308.833,110,343.667,69.05,378.5,69.05C413.333,69.05,448.167,115.775,483,115.775C517.833,115.775,552.667,103.525,587.5,89.525C622.333,75.525,657.167,53.65,692,31.775" fill="none" fill-opacity="0.6"></path>
        </g>
      </g>
      <g class="recharts-layer recharts-cartesian-axis rechts-xAxis">
        <line x1="65" x2="102" y1="215" y2="215"></line>
        <text x="80.63333129882812">PageG</text>
      </g>
      <g class="recharts-layer rechts-cartesian-axis rechts-yAxis">
        <line x1="65" x2="65" y1="5" y2="215"></line>
        <text x="57">0</text>
        <text x="57">1000</text>
        <text x="57">2000</text>
        <text x="57">3000</text>
        <text x="57">4000</text>
      </g>
    </svg>
  </div>
</div>

- [Code](#code)
- [Data](#data)

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

## Data

# Syncing Charts

The `sync_id` prop allows you to sync two graphs. In the example, it is set to "1" for both charts, indicating that they should be synchronized. This means that any interactions (such as brushing) performed on one chart will be reflected in the other chart.

## Code Example

```python
def area_sync():
    return rx.vstack(
        rx.recharts.bar_chart(
            rx.recharts.graphing_tooltip(),
            rx.recharts.bar(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8",
            ),
            rx.recharts.bar(
                data_key="pv",
                stroke="#82ca9d",
                fill="#82ca9d",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=data,
            sync_id="1",
            width="100%",
            height=200,
        ),
        rx.recharts.composed_chart(
            rx.recharts.area(
                data_key="uv",
                stroke="#8884d8",
                fill="#8884d8",
            ),
            rx.recharts.line(
                data_key="pv",
                type_="monotone",
                stroke="#ff7300",
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            rx.recharts.graphing_tooltip(),
            rx.recharts.brush(
                data_key="name",
                height=30,
                stroke="#8884d8"
            ),
            data=data,
            sync_id="1",
            width="100%",
            height=250,
        )
    )
```

## Synchronized Bar Chart

![Synchronized Bar Chart](https://via.placeholder.com/107x200)

## Synchronized Area and Line Chart with Brushing

![Synchronized Area and Line Chart with Brushing](https://via.placeholder.com/107x250)

# Stacking Charts

The `stack_id` prop allows you to stack multiple graphs on top of each other. In the example, it is set to "1" for both charts, indicating that they should be stacked together. This means that the bars or areas of the charts will be vertically stacked, with the values of each chart contributing to the total height of the stacked areas or bars.

This is similar to the `sync_id` prop, but instead of synchronizing the interaction between the charts, it just stacks the charts on top of each other.

The example code for creating a stacked area chart is as follows:

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

For more details, you can refer to the official documentation: [Reflex Dev Docs](https://reflex.dev/docs/library/graphing/charts/areachart/#multiple-axis)

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

# Layout

Use the `layout` prop to set the orientation to either `"horizontal"` (default) or `"vertical"`.

Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.

## Code Example

```python
def area_vertical():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke=rx.color("accent", 8),
            fill=rx.color("accent", 3),
        ),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category"),
        data=data,
        layout="vertical",
        height=300,
        width="100%",
    )
```

[![Copy to Clipboard](https://github.com/alibabacloudqingwen/images/raw/main/copy_icon.svg)](javascript:copyToClipboard('def area_vertical():\n    return rx.recharts.area_chart(\n        rx.recharts.area(\n            data_key="uv",\n            stroke=rx.color("accent", 8),\n            fill=rx.color("accent", 3),\n        ),\n        rx.recharts.x_axis(type_="number"),\n        rx.recharts.y_axis(data_key="name", type_="category"),\n        data=data,\n        layout="vertical",\n        height=300,\n        width="100%",\n    )'))

# Stateful Example

Here is an example of an area graph with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data for both graphs when the first defined `area` is clicked on using `on_click=AreaState.randomize_data`.

Curve Type:
- basis

The graph shows two areas: one in different shades, representing `uv` and `pv`. You can change the curve type by selecting from "basis", "natural", or "step".

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
            height=400
        ),
        width="100%"
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/areachart/#rx.recharts.areachart)

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

- **on_animation_start**
  - The customized event handler of animation start
  
- **on_animation_end**
  - The customized event handler of animation end