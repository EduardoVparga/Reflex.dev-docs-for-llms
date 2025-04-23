# Composed Chart

To learn more about individual charts, checkout: [area_chart](/docs/library/graphing/charts/areachart/), [line_chart](/docs/library/graphing/charts/linechart/), or [bar_chart](/docs/library/graphing/charts/barchart/).

The composed chart is a higher-level component chart that is composed of multiple charts, where other charts are the children of the `composed_chart`. The charts are placed on top of each other in the order they are provided in the `composed_chart` function.

```python
def composed():
    return rx.recharts.composed_chart(
        rx.recharts.area(data_key="uv", stroke="#8884d8", fill="#8884d8"),
        rx.recharts.bar(data_key="amt", bar_size=20, fill="#413ea0"),
        rx.recharts.line(data_key="pv", type_="monotone", stroke="#ff7300"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        data=data,
        height=250,
        width="100%",
    )
```

To the right, you can see a composed chart that includes an area chart, a bar chart, and a line chart. The chart is interactive and provides tooltips for specific data points.

![Composed Chart](https://your-image-url.com/chart.png)

# API Reference

[Link](https://reflex.dev/docs/library/graphing/charts/composedchart/#rx.recharts.composedchart)

# rx.recharts.ComposedChart

A Composed chart component in Recharts.

## Props

| Prop         | Type | Values          | Default |
|--------------|------|-----------------|---------|
| base_value   |      | "dataMin" | "dataMax" | ...  | "auto" |
| bar_category_gap | Union[str, int] |        | "10%"     |
| bar_gap      | int  |                 | 4       |
| bar_size     | int  |                 |         |
| reverse_stack_order | bool |                 | False   |
| data         | Sequence |               |         |
| margin      | Dict[str, Any] |           |         |
| sync_id     | str  |                 |         |
| sync_method | "index" | "value"        | "index" |
| layout      | "vertical" | "horizontal"   | "horizontal" |
| stack_offset | "expand" | "none" | ...       |         |
| width       | Union[str, int] |           | Var.create("100%") |
| height      | Union[str, int] |           | Var.create("100%") |

#Valid Children

- XAxis
- YAxis
- ReferenceArea
- ReferenceDot
- ReferenceLine
- Brush
- CartesianGrid
- Legend
- GraphingTooltip
- Area
- Line
- Bar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)