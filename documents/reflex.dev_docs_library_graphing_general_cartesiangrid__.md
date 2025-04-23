# Cartesian Grid

The Cartesian Grid is a component in Recharts that provides a visual reference for data points in charts. It helps users to better interpret the data by adding horizontal and vertical lines across the chart area.

[Simple Example](https://reflex.dev/docs/library/graphing/general/cartesiangrid/#simple-example)

# Simple Example

The `stroke_dasharray` prop in Recharts is used to create dashed or dotted lines for various chart elements like lines, axes, or grids. It's based on the SVG stroke-dasharray attribute. The `stroke_dasharray` prop accepts a comma-separated string of numbers that define a repeating pattern of dashes and gaps along the length of the stroke.

- `stroke_dasharray="5,5"`: creates a line with 5-pixel dashes and 5-pixel gaps
- `stroke_dasharray="10,5,5,5"`: creates a more complex pattern with 10-pixel dashes, 5-pixel gaps, 5-pixel dashes, and 5-pixel gaps

Here's a simple example using it on a Line component:

```python
def cgrid_simple():
    return rx.recharts.line_chart(
        rx.recharts.line(data_key="pv"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="4 4"),
        data=data,
        width="100%",
        height=300,
    )
```

For more details, you can refer to the official documentation.

# Hidden Axes

A `cartesian_grid` component can be used to hide the horizontal and vertical grid lines in a chart by setting the `horizontal` and `vertical` props to `False`. This can be useful when you want to show the grid lines only on one axis or when you want to create a cleaner look for the chart.

```python
def cgrid_hidden():
    return rx.recharts.area_chart(
        rx.recharts.area(data_key="uv", stroke="#8884d8", fill="#8884d8"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(
            stroke_dasharray="2 4",
            vertical=False,
            horizontal=True,
        ),
        data=data,
        width="100%",
        height=300,
    )
```

[![Copy](https://github.com/alibabacloudqingwen/Qwen/assets/71859566/eaf0e720-40a5-47b8-b99f-d2d802f1a7c3))](#)

# Custom Grid Lines

The `horizontal_points` and `vertical_points` props allow you to specify custom grid lines on the chart, offering fine-grained control over the grid's appearance.

These props accept arrays of numbers, where each number represents a pixel offset:

- For `horizontal_points`, the offset is measured from the top edge of the chart
- For `vertical_points`, the offset is measured from the left edge of the chart

## Important

Important: The values provided to these props are not directly related to the axis values. They represent pixel offsets within the chart's rendering area.

Here's an example demonstrating custom grid lines in a scatter chart:

```python
def cgrid_custom():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(data=data2, fill="#8884d8"),
        rx.recharts.x_axis(data_key="x", type_="number"),
        rx.recharts.y_axis(data_key="y"),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3",
                                  horizontal_points=[0, 25, 50],
                                  vertical_points=[65, 90, 115]),
        width="100%",
        height=200,
    )
```

Use these props judiciously to enhance data visualization without cluttering the chart. They're particularly useful for highlighting specific data ranges or creating visual reference points.

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/general/cartesiangrid/#rx.recharts.cartesiangrid)

# rx.recharts.CartesianGrid

A CartesianGrid component in Recharts.

## Props

| Prop          | Type        | Default |
| ------------- | ----------- | ------- |
| horizontal    | bool        | True    |
| vertical      | bool        | True    |
| vertical_points | Sequence   | []      |
| horizontal_points | Sequence  | []      |
| fill          | Union[str, Color] | -       |
| fill_opacity  | float      | -       |
| stroke_dasharray | str     | -       |
| stroke        | Union[str, Color] | rx.color("gray", 7) |
| x             | int        | 0       |
| y             | int        | 0       |
| width         | int        | 0       |
| height        | int        | 0       |

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)