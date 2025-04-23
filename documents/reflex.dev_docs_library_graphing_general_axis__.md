# Axis

The Axis component in Recharts is a powerful tool for customizing and configuring the axes of your charts. It provides a wide range of props that allow you to control the appearance, behavior, and formatting of the axis. Whether you're working with an AreaChart, LineChart, or any other chart type, the Axis component enables you to create precise and informative visualizations.

[Learn More](/docs/library/graphing/general/axis/#basic-example)

# Basic Example

![Link](#/docs/library/graphing/general/axis/#multiple-axes)

<div class="w-full py-4 flex flex-col">
  <div class="w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center">
    <!-- A chart is represented here but not converted to Markdown -->
  </div>
</div>

## Code

```python
def axis_simple():
    return rx.recharts.area_chart(
        rx.recharts.area(data_key="uv", stroke=rx.color("accent", 9), fill=rx.color("accent", 8)),
        rx.recharts.x_axis(data_key="name", label={"value": "Pages", "position": "bottom"}),
        rx.recharts.y_axis(data_key="uv", label={
            "value": "Views",
            "angle": -90,
            "position": "left"
        }),
        data=data,
        width="100%",
        height=300,
        margin={"bottom": 40, "left": 40, "right": 40}
    )
```

<button>
  <svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="16">
    <rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect>
    <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path>
  </svg>
</button>

# Multiple Axes

Multiple axes can be used for displaying different data series with varying scales or units on the same chart. This allows for a more comprehensive comparison and analysis of the data.

## Code Example

```python
def multi_axis():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke="#8884d8",
            fill="#8884d8",
            y_axis_id="left"
        ),
        rx.recharts.area(
            data_key="pv",
            y_axis_id="right",
            type_="monotone",
            stroke="#82ca9d",
            fill="#82ca9d"
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(data_key="uv", y_axis_id="left"),
        rx.recharts.y_axis(
            data_key="pv",
            y_axis_id="right",
            orientation="right"
        ),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        data=data,
        width="100%",
        height=300
    )
```

## Data

- UV: `["uv"]`
- PV: `["pv"]`

# Choosing Location of Labels for Axes

The axes label can take several positions. The example below allows you to try out different locations for the x and y axis labels.

X Label Position: 
- [bottom](#)
- [0](#)

X Label Offset: 
- [0](#)

Y Label Position: 
- [left](#)
- [-90](#)

Y Label Offset: 
- [0](#)
- [to_string()](#)

```python
def axis_labels():
    return rx.vstack(
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="uv",
                stroke=rx.color("accent", 9),
                fill=rx.color("accent", 8),
            ),
            rx.recharts.x_axis(
                data_key="name",
                label={
                    "value": "Pages",
                    "position": AxisState.x_axis_postion,
                    "offset": AxisState.x_axis_offset,
                },
            ),
            rx.recharts.y_axis(
                data_key="uv",
                label={
                    "value": "Views",
                    "angle": -90,
                    "position": AxisState.y_axis_postion,
                    "offset": AxisState.y_axis_offset,
                },
            ),
            width="100%",
            height=300,
            margin={
                "bottom": 40,
                "left": 40,
                "right": 40,
            },
        ),
        rx.hstack(
            rx.text("X Label Position: "),
            rx.select(AxisState.label_positions, value=AxisState.x_axis_postion, on_change=AxisState.set_x_axis_postion),
            rx.text("X Label Offset: "),
            rx.select(AxisState.label_offsets, value=AxisState.x_axis_offset.to_string(), on_change=AxisState.set_x_axis_offset),
            rx.text("Y Label Position: "),
            rx.select(AxisState.label_positions, value=AxisState.y_axis_postion, on_change=AxisState.set_y_axis_postion),
            rx.text("Y Label Offset: "),
            rx.select(AxisState.label_offsets, value=AxisState.y_axis_offset.to_string(), on_change=AxisState.set_y_axis_offset),
        ),
        width="100%",
    )
```

# API Reference

[API Reference](/docs/library/graphing/general/axis/#rx.recharts.xaxis)

The `rx.plot.line` function is used to create a line chart in Reaktor, and the `rx.plot.scatter` function is used for creating scatter plots. The `rx.plot.histogram` function generates a histogram plot.

In your case, you're trying to create a line plot with specific configurations using `rx.plot.line`. Here are some key points about the configuration options available for `rx.plot.line`, based on the provided data:

1. **General Configuration**:
   - `name`: Name of the plot.
   - `domain`: Domain values for the x-axis (default is `[0, "auto"]`).
   - `scale`: Scaling method for the y-axis (`"auto"`, `"linear"`, etc.).
   - `unit`: Unit of measurement for the y-axis.

2. **Tick and Label Configuration**:
   - `ticks`: Custom ticks.
   - `tick_count`: Number of automatic ticks (default is 5 if not specified).
   - `label`: Labels for the x-axis, can be a string, integer, or dictionary with custom labels.

3. **Line and Stroke Configuration**:
   - `stroke`: Color of the line.

4. **Tick Line Configuration**:
   - `tick_line`: Whether to show tick lines.
   - `tick_size`: Size of the tick marks.
   - `min_tick_gap`: Minimum gap between ticks.

5. **Domain and Range Configuration**:
   - `domain`: Custom domain for x-axis.
   - `axis_line`: Show or hide axis line (`True` by default).
   - `mirror`: Mirror the plot (default is `False`).

6. **Scaling and Unit Configuration**:
   - `scale`: Scaling method.
   - `unit`: Unit of measurement.

### Example Usage

Here's an example usage based on the provided configuration options:

```python
import rx

# Sample data
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 4, 9, 16, 25]

# Creating a line plot with custom configurations
rx.plot.line(
    name="My Line Plot",
    x=x_data,
    y=y_data,
    domain=[-2, "auto"],
    scale="linear",
    unit="cm",
    ticks=[0, 2, 4, 6],
    tick_count=5,
    label="Custom Label",
    stroke="red",
    text_anchor="middle",
    axis_line=True,
    mirror=False
)
```

### Explanation of Configuration Options in the Example

- `name`: "My Line Plot" (Name of the plot).
- `domain`: `[-2, "auto"]` (Custom domain for x-axis from -2 to automatically determined upper limit).
- `scale`: `"linear"` (Linear scaling on y-axis).
- `unit`: `"cm"` (Unit of measurement for y-axis).
- `ticks`: `[0, 2, 4, 6]` (Custom ticks on the x-axis).
- `tick_count`: `5` (Number of automatic ticks if not specified by custom ticks).
- `label`: "Custom Label" (Label for the x-axis).
- `stroke`: `"red"` (Color of the line).
- `text_anchor`: `"middle"` (Text anchor point for labels).
- `axis_line`: `True` (Show axis line).
- `mirror`: `False` (Do not mirror the plot).

This should give you a good starting point to customize your plots according to your needs. If you need more specific configurations or further customization, please provide additional details!

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.recharts.YAxis

A YAxis component in Recharts.

## Props

| Prop          | Type | Values               | Default |
|---------------|------|----------------------|---------|
| orientation   |      | "left" | "right"            | "left"  |
| y_axis_id     |      | Union[str, int]      | 0       |
| padding       |      | Dict[str, int]       | {"top": 0, "bottom": 0} |
| data_key      |      | Union[str, int]      | -       |
| hide          |      | bool                 | False   |
| width         |      | Union[str, int]      | -       |
| height        |      | Union[str, int]      | -       |
| type_         |      | "number" | "category"        | -       |
| interval      |      | "preserveStart" | "preserveEnd" | ...    | "preserveEnd" |
| allow_decimals |     | bool                 | True    |
| allow_data_overflow |   | bool                 | False   |
| allow_duplicated_category |  | bool                 | True    |
| domain        |      | Sequence             | [0, "auto"] |
| axis_line     |      | bool                 | True    |
| mirror        |      | bool                 | False   |
| reversed      |      | bool                 | False   |
| label         |      | Union[str, int, dict] | -       |
| scale         |      | "auto" | "linear" | ...    | "auto"  |
| unit          |      | Union[str, int]      | -       |
| name          |      | Union[str, int]      | -       |
| ticks         |      | Sequence             | -       |
| tick          |      | bool                 | -       |
| tick_count    |      | int                  | 5       |
| tick_line     |      | bool                 | True    |
| tick_size     |      | int                  | 6       |
| min_tick_gap  |      | int                  | 5       |
| stroke        |      | Union[str, Color]    | rx.color("gray", 9) |
| text_anchor   |      | "start" | "middle" | ...    | "middle" |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.recharts.ZAxis

A ZAxis component in Recharts.

## Props

- **Prop** | **Type | Values** | **Default**
  - `data_key` | `Union[str, int]` | 
  - `z_axis_id` | `Union[str, int]` | `0`
  - `range` | `Sequence` | `[60, 400]`
  - `unit` | `Union[str, int]` | 
  - `name` | `Union[str, int]` | 
  - `scale` | `"auto" | "linear" | ...` | `"auto"`

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)