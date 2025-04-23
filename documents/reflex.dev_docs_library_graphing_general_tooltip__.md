# Tooltip

Tooltips are the little boxes that pop up when you hover over something. Tooltips are always attached to something, like a dot on a scatter chart, or a bar on a bar chart.

## Code Example

```python
def tooltip_simple():
    return rx.recharts.composed_chart(
        rx.recharts.area(data_key="uv", stroke="#8884d8", fill="#8884d8"),
        rx.recharts.bar(data_key="amt", bar_size=20, fill="#413ea0"),
        rx.recharts.line(data_key="pv", type_="monotone", stroke="#ff7300"),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        data=data,
        width="100%",
        height=300,
    )
```

## Data

The provided code snippet also includes a tab for the data, but it is hidden.

# Custom Styling

The `rx.recharts.graphing_tooltip` component allows for customization of the tooltip's style, position, and layout. `separator` sets the separator between the data key and value. `view_box` prop defines the dimensions of the chart's viewbox while `allow_escape_view_box` determines whether the tooltip can extend beyond the viewBox horizontally (x) or vertically (y). `wrapper_style` prop allows you to style the outer container or wrapper of the tooltip. `content_style` prop allows you to style the inner content area of the tooltip. `is_animation_active` prop determines if the tooltip animation is active or not.

```python
def tooltip_custom_styling():
    return rx.recharts.composed_chart(
        rx.recharts.area(
            data_key="uv", stroke="#8884d8", fill="#8884d8"
        ),
        rx.recharts.bar(
            data_key="amt", bar_size=20, fill="#413ea0"
        ),
        rx.recharts.line(
            data_key="pv",
            type_="monotone",
            stroke="#ff7300",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.graphing_tooltip(
            separator=" - ",
            view_box={"width": 675, " height": 300},
            allow_escape_view_box={"x": True, "y": False},
            wrapper_style={
                "backgroundColor": rx.color("accent", 3),
                "borderRadius": "8px",
                "padding": "10px",
            },
            content_style={
                "backgroundColor": rx.color("accent", 4),
                "borderRadius": "4px",
                "padding": "8px",
            },
            position={"x": 600, "y": 0},
            is_animation_active=False,
        ),
        data=data,
        height=300,
        width="100%",
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/general/tooltip/#rx.recharts.graphingtooltip)

# rx.recharts.GraphingTooltip

A Tooltip component in Recharts.

## Props

| Prop         | Type | Values            | Default |
|--------------|------|-------------------|---------|
| separator    | str  | ":"               | ""      |
| offset       | int  |                   | 10      |
| filter_null  | bool |                    | True    |
| cursor       | Union[dict, bool] |                   | {"strokeWidth": 1, "fill": rx.color("gray", 3)} |
| view_box     | Dict[str, Any]   |                    |         |
| item_style   | Dict[str, Any]   |                    | {"color": rx.color("gray", 12)} |
| wrapper_style| Dict[str, Any]   |                    | {}      |
| content_style| Dict[str, Any]   |                    | {"background": rx.color("gray", 1), "borderColor": rx.color("gray", 4), "borderRadius": "8px"} |
| label_style  | Dict[str, Any]   |                    | {"color": rx.color("gray", 11)} |
| allow_escape_view_box | Dict[str, bool] |                  | {"x": False, "y": False} |
| active       | bool            |                    | False   |
| position     | Dict[str, Any]   |                    | {}      |
| coordinate   | Dict[str, Any]   |                    | {"x": 0, "y": 0} |
| is_animation_active | bool          |                    | True    |
| animation_duration | int           |                    | 1500    |
| animation_easing | str            | "ease", "ease-in" ... | "ease"  |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)