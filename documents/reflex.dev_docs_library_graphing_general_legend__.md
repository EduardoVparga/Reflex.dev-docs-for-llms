# Legend

A legend tells what each plot represents. Just like on a map, the legend helps the reader understand what they are looking at. For a line graph for example it tells us what each line represents.

[Simple Example](https://reflex.dev/docs/library/graphing/general/legend/#simple-example)

# Simple Example

[![Simple Example](https://via.placeholder.com/18x18)](https://reflex.dev/docs/library/graphing/general/legend/#example-with-props)

<div class="w-full py-4 flex flex-col">

  <div class="w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center">

    <svg height="300" style="width: 107px; height: 300px;" viewBox="0 0 107 300">
      <!-- SVG content omitted -->
    </svg>

  </div>
</div>

---

#### Code

```python
def legend_simple():
    return rx.recharts.composed_chart(
        rx.recharts.area(
            data_key="uv",
            stroke="#8884d8",
            fill="#8884d8"
        ),
        rx.recharts.bar(
            data_key="amt",
            bar_size=20,
            fill="#413ea0"
        ),
        rx.recharts.line(
            data_key="pv",
            type_="monotone",
            stroke="#ff7300"
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        data=data,
        width="100%",
        height=300
    )
```

---

# Example with Props

The style and layout of the legend can be customized using a set of props. `width` and `height` set the dimensions of the container that wraps the legend, and `layout` can set the legend to display vertically or horizontally. `align` and `vertical_align` set the position relative to the chart container. The type and size of icons can be set using `icon_size` and `icon_type`.

The following code example demonstrates how to customize the legend:

```python
def legend_props():
    return rx.recharts.composed_chart(
        rx.recharts.line(
            data_key="pv",
            type_="monotone",
            stroke=rx.color("accent", 7),
        ),
        rx.recharts.line(
            data_key="amt",
            type_="monotone",
            stroke=rx.color("green", 7),
        ),
        rx.recharts.line(
            data_key="uv",
            type_="monotone",
            stroke=rx.color("red", 7),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(
            width=60,
            height=100,
            layout="vertical",
            align="right",
            vertical_align="top",
            icon_size=15,
            icon_type="square",
        ),
        data=data,
        width="100%",
        height=300,
    )
```

- **width**: 60
- **height**: 100
- **layout**: "vertical"
- **align**: "right"
- **vertical_align**: "top"
- **icon_size**: 15
- **icon_type**: "square"

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/general/legend/#rx.recharts.legend)

# rx.recharts.Legend

A Legend component in Recharts.

## Props

- **width**: `int`
  - Default: None

- **height**: `int`
  - Default: None

- **layout**: `"vertical" | "horizontal"`
  - Default: `"horizontal"`

- **align**: `"left" | "center" | ...`
  - Default: `"center"`

- **vertical_align**: `"top" | "middle" | ...`
  - Default: `"bottom"`

- **icon_size**: `int`
  - Default: `14`

- **icon_type**: `"line" | "plainline" | ...`
  - Default: None

- **payload**: `Sequence`
  - Default: `[]`

- **chart_width**: `int`
  - Default: None

- **chart_height**: `int`
  - Default: None

- **margin**: `Dict[str, Any]`
  - Default: None

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)