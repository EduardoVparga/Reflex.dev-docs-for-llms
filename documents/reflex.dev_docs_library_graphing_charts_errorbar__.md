# Error Bar

An error bar is a graphical representation of the uncertainty or variability of a data point in a chart, depicted as a line extending from the data point parallel to one of the axes. The `data_key`, `width`, `stroke_width`, `stroke`, and `direction` props can be used to customize the appearance and behavior of the error bars, specifying the data source, dimensions, color, and orientation of the error bars.

## Code Example

```python
def error():
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
            rx.recharts.error_bar(
                data_key="errorY",
                direction="y",
                width=4,
                stroke_width=2,
                stroke="red",
            ),
            rx.recharts.error_bar(
                data_key="errorX",
                direction="x",
                width=4,
                stroke_width=2,
                stroke="red",
            ),
            data=data,
            fill="#8884d8",
            name="A",
        ),
        rx.recharts.x_axis(
            data_key="x", name="x", type_="number"
        ),
        rx.recharts.y_axis(
            data_key="y", name="y", type_="number"
        ),
        width="100%",
        height=300,
    )
```

[![Copy to Clipboard](https://raw.githubusercontent.com/alibabacloudqinglang/qlua/main/assets/copy.svg)](https://reflex.dev/docs/library/graphing/charts/errorbar/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/errorbar/#rx.recharts.errorbar)

# rx.recharts.ErrorBar

An ErrorBar component in Recharts.

## Props

- **direction**: `"x" | "y"`  
  - Default: Not specified

- **data_key**: `Union[str, int]`  
  - Default: Not specified

- **width**: `int`  
  - Default: `5`

- **stroke**: `Union[str, Color]`  
  - Default: `rx.color("gray", 8)`

- **stroke_width**: `Union[int, float]`  
  - Default: `1.5`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)