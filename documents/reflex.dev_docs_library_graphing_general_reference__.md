# Reference

The Reference components in Recharts, including ReferenceLine, ReferenceArea, and ReferenceDot, are used to add visual aids and annotations to the chart, helping to highlight specific data points, ranges, or thresholds for better data interpretation and analysis.

[Learn more](https://reflex.dev/docs/library/graphing/general/reference/#reference-area)

# Reference Area

The `rx.recharts.reference_area` component in Recharts is used to highlight a specific area or range on the chart by drawing a rectangular region. It is defined by specifying the coordinates (x1, x2, y1, y2) and can be used to emphasize important data ranges or intervals on the chart.

The following code defines a scatter chart with a reference area:

```python
def reference():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data,
            fill="#8884d8",
            name="A"
        ),
        rx.recharts.reference_area(
            x1=150,
            x2=180,
            y1=150,
            y2=300,
            fill="#8884d8",
            fill_opacity=0.3
        ),
        rx.recharts.x_axis(
            data_key="x",
            name="x",
            type_="number"
        ),
        rx.recharts.y_axis(
            data_key="y",
            name="y",
            type_="number"
        ),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=300
    )
```

The chart includes an x-axis and y-axis with specific values, a scatter plot, and a reference area highlighted in light blue with 30% opacity.

# Reference Line

The `rx.recharts.reference_line` component in rx.recharts is used to draw a horizontal or vertical line on the chart at a specified position. It helps to highlight important values, thresholds, or ranges on the axis, providing visual reference points for better data interpretation.

## Code Example

```python
def reference_line():
    return rx.recharts.area_chart(
        rx.recharts.area(
            data_key="pv",
            stroke=rx.color("accent", 8),
            fill=rx.color("accent", 7),
        ),
        rx.recharts.reference_line(
            x="Page C",
            stroke=rx.color("accent", 10),
            label="Max PV PAGE",
        ),
        rx.recharts.reference_line(
            y=9800,
            stroke=rx.color("green", 10),
            label="Max",
        ),
        rx.recharts.reference_line(
            y=4343,
            stroke=rx.color("green", 10),
            label="Average",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data_2,
        height=300,
        width="100%",
    )
```

For more information, see the [Reference Dot documentation](https://reflex.dev/docs/library/graphing/general/reference/#reference-dot).

# Reference Dot

The `rx.recharts.reference_dot` component in Recharts is used to mark a specific data point on the chart with a customizable dot. It allows you to highlight important values, outliers, or thresholds by providing a visual reference marker at the specified coordinates (x, y) on the chart.

## Example Code

```python
def reference_dot():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            data=data_3,
            fill=rx.color("accent", 9),
            name="A",
        ),
        rx.recharts.x_axis(
            data_key="x",
            name="x",
            type_="number"
        ),
        rx.recharts.y_axis(
            data_key="y",
            name="y",
            type_="number"
        ),
        rx.recharts.reference_dot(
            x=160,
            y=350,
            r=15,
            fill=rx.color("accent", 5),
            stroke=rx.color("accent", 10)
        ),
        rx.recharts.reference_dot(
            x=170,
            y=300,
            r=20,
            fill=rx.color("accent", 7),
            stroke="#ccc"
        ),
        rx.recharts.reference_dot(
            x=90,
            y=220,
            r=18,
            fill=rx.color("green", 7)
        ),
        height=200,
        width="100%",
    )
```

## Reference Dot Example

The following example shows a chart with multiple reference dots:

- **Dot 1**: At coordinates (160, 350) with radius 15 and fill color `accent-5`.
- **Dot 2**: At coordinates (170, 300) with radius 20, fill color `accent-7`, and stroke color `#ccc`.
- **Dot 3**: At coordinates (90, 220) with radius 18, fill color `green-7`.

![](https://i.imgur.com/example.png)

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/general/reference/#rx.recharts.referenceline)

# rx.recharts.ReferenceLine
A ReferenceLine component in Recharts.

## Props

| Prop         | Type | Default |
|--------------|------|---------|
| x            | Union[str, int] | -       |
| y            | Union[str, int] | -       |
| stroke       | Union[str, Color] | 1       |
| stroke_width | Union[str, int] | 1       |
| segment      | Sequence | []      |
| x_axis_id    | Union[str, int] | 0       |
| y_axis_id    | Union[str, int] | 0       |
| if_overflow  | "discard" | "discard" |
| label        | Union[str, int] | -       |
| is_front     | bool | False   |

# Valid Children
- Label

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.recharts.ReferenceDot

A ReferenceDot component in Recharts.

## Props

| Prop     | Type | Values        | Default |
|----------|------|---------------|---------|
| x        | Union[str, int] | -          |         |
| y        | Union[str, int] | -          |         |
| r        | int   | -            |         |
| fill     | Union[str, Color] | -       |         |
| stroke   | Union[str, Color] | -       |         |
| x_axis_id | Union[str, int] | 0         |         |
| y_axis_id | Union[str, int] | 0         |         |
| if_overflow | "discard" | "discard"     |         |
| label    | Union[str, int] | -          |         |
| is_front | bool  | False         |         |

# Valid Children
- Label

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.recharts.ReferenceArea

A ReferenceArea component in Recharts.

## Props

- **stroke**
  - Type: `Union[str, Color]`
  - Default: Not specified

- **fill**
  - Type: `Union[str, Color]`
  - Default: Not specified

- **fill_opacity**
  - Type: `float`
  - Default: Not specified

- **x_axis_id**
  - Type: `Union[str, int]`
  - Default: Not specified

- **y_axis_id**
  - Type: `Union[str, int]`
  - Default: Not specified

- **x1**
  - Type: `Union[str, int]`
  - Default: Not specified

- **x2**
  - Type: `Union[str, int]`
  - Default: Not specified

- **y1**
  - Type: `Union[str, int]`
  - Default: Not specified

- **y2**
  - Type: `Union[str, int]`
  - Default: Not specified

- **if_overflow**
  - Type: `"discard" | "hidden" | ...`
  - Default: `"discard"`

- **is_front**
  - Type: `bool`
  - Default: `False`

# Valid Children
- Label

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)