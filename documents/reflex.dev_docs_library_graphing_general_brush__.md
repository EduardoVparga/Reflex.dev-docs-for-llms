# Brush

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/graphing/general/brush/#simple-example">

The code you provided is a Reflex application that generates an interactive bar chart using recharts. The chart includes brushing functionality, which allows users to select and highlight ranges on the x-axis.

Here's a breakdown of the key components:

1. **Brushing Functionality**:
   - The `brush` component from recharts is used to create a brush selection area.
   - The brush can be positioned, sized, and its range can be adjusted by dragging or clicking within the chart area.

2. **Bar Chart Data**:
   - The data for the bar chart is defined in the `data` list. Each item in this list represents a bar with properties like `name`, `uv`, and `pv`.
   - Example data structure: `[{'name': 'A', 'uv': 150, 'pv': 230}, {'name': 'B', 'uv': 340, 'pv': 670}, ...]`

3. **Bar Chart Configuration**:
   - The `bar_chart` component from recharts is used to create the bar chart.
   - Two bars are defined using the `bar` component: one for `uv` (represented in blue) and another for `pv` (represented in green).
   - The `brush` component is configured with specific settings like height, stroke color, etc.

4. **X-axis and Y-axis**:
   - The x-axis is defined using the `x_axis` component, which uses the `data_key` to map the data.
   - The y-axis is defined using the `y_axis` component.

5. **Styling and Animation**:
   - Various styles are applied for visual elements like bars, axes, and ticks.
   - The chart's dimensions (width and height) are set programmatically.

6. **Interactive Elements**:
   - The brush area can be interacted with to select ranges on the x-axis.
   - Highlighting of selected ranges is handled by recharts dynamically.

### Example Data Structure
Here’s an example of how your `data` list might look:

```python
data = [
    {'name': 'A', 'uv': 150, 'pv': 230},
    {'name': 'B', 'uv': 340, 'pv': 670},
    {'name': 'C', 'uv': 80, 'pv': 300},
    {'name': 'D', 'uv': 500, 'pv': 1200},
    {'name': 'E', 'uv': 400, 'pv': 900},
    {'name': 'F', 'uv': 600, 'pv': 800},
    {'name': 'G', 'uv': 700, 'pv': 1200},
    {'name': 'H', 'uv': 450, 'pv': 950},
    {'name': 'I', 'uv': 300, 'pv': 680},
]
```

### Full Code Example
Here is the full code snippet with added comments for clarity:

```python
import reflex as rx

def brush_simple():
    return rx.recharts.bar_chart(
        # Define two bars (UV and PV) with different colors
        rx.recharts.bar(data_key="uv", stroke="#8884d8", fill="#8884d8"),
        rx.recharts.bar(data_key="pv", stroke="#82ca9d", fill="#82ca9d"),
        
        # Define a brush selection area on the x-axis
        rx.recharts.brush(
            data_key="name",
            height=30,
            stroke="#8884d8"
        ),
        
        # X-axis configuration
        rx.recharts.x_axis(data_key="name"),
        
        # Y-axis configuration (default settings)
        rx.recharts.y_axis(),
        
        # Data list for the bar chart
        data=[
            {'name': 'A', 'uv': 150, 'pv': 230},
            {'name': 'B', 'uv': 340, 'pv': 670},
            {'name': 'C', 'uv': 80, 'pv': 300},
            {'name': 'D', 'uv': 500, 'pv': 1200},
            {'name': 'E', 'uv': 400, 'pv': 900},
            {'name': 'F', 'uv': 600, 'pv': 800},
            {'name': 'G', 'uv': 700, 'pv': 1200},
            {'name': 'H', 'uv': 450, 'pv': 950},
            {'name': 'I', 'uv': 300, 'pv': 680},
        ],
        
        # Chart dimensions
        width="100%",
        height=300,
    )
```

This code will generate a bar chart with brushing functionality. Users can interactively select ranges on the x-axis and see the corresponding bars highlighted in real-time.

# Position, Size, and Range

This example showcases ways to set the Position, Size, and Range. The `gap` prop provides the spacing between stops on the brush when the graph will refresh. The `start_index` and `end_index` props defines the default range of the brush. `traveller_width` prop specifies the width of each handle ("traveller" in recharts lingo).

## Code

```python
def brush_pos_size_range():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="uv",
            stroke="#8884d8",
            fill="#8884d8"
        ),
        rx.recharts.area(
            data_key="pv",
            stroke="#82ca9d",
            fill="#82ca9d"
        ),
        rx.recharts.brush(
            data_key="name",
            traveller_width=15,
            start_index=3,
            end_index=10,
            stroke=rx.color("mauve", 10),
            fill=rx.color("mauve", 3)
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=200
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/general/brush/#rx.recharts.brush)

# rx.recharts.Brush

A Brush component in Recharts.

## Props

- **Prop** | **Type | Values** | **Default**
  - `stroke` | Union[str, Color] | `rx.color("gray", 9)`
  - `fill` | Union[str, Color] | `rx.color("gray", 2)`
  - `data_key` | Union[str, int]
  - `x` | int | `0`
  - `y` | int | `0`
  - `width` | int | `0`
  - `height` | int | `40`
  - `data` | Sequence
  - `traveller_width` | int | `5`
  - `gap` | int | `1`
  - `start_index` | int | `0`
  - `end_index` | int

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_change`
  - Description: Function or event handler called when the value of an element has changed. For example, it is called when the user types into a text input each keystroke triggers the on change.