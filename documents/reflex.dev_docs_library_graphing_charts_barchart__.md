# Bar Chart

A bar chart presents categorical data with rectangular bars with heights or lengths proportional to the values that they represent.

For a bar chart we must define an `rx.recharts.bar()` component for each set of values we wish to plot. Each `rx.recharts.bar()` component has a `data_key` which clearly states which variable in our data we are tracking. In this simple example we plot `uv` as a bar against the `name` column which we set as the `data_key` in `rx.recharts.x_axis`.

[View Simple Example](https://reflex.dev/docs/library/graphing/charts/barchart/#simple-example)

# Simple Example

![](https://example.com/link-icon.svg)

<div class="w-full py-4 flex flex-col">
  <div class="w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center">
    [Bar Chart Data]
  </div>
</div>

## Code

```python
def bar_simple():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=250,
    )
```

## Data

[Data Content]

# Multiple Bars

Multiple bars can be placed on the same `bar_chart`, using multiple `rx.recharts.bar()` components.

## Code

```python
def bar_double():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.bar(
            data_key="pv",
            stroke=rx.color("green", 9),
            fill=rx.color("green", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        width="100%",
        height=250,
    )
```

## Data

The chart uses the following data:

# Ranged Charts

You can also assign a range in the bar by assigning the `data_key` in the `rx.recharts.bar` to a list with two elements, i.e. here a range of two temperatures for each date.

```python
def bar_range():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="temperature",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="day"),
        rx.recharts.y_axis(),
        data=range_data,
        width="100%",
        height=250,
    )
```

[View Code](https://reflex.dev/docs/library/graphing/charts/barchart/#stateful-charts)

# Stateful Charts

Here is an example of a bar graph with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data for both graphs when the first defined `bar` is clicked on using `on_click=BarState.randomize_data`.

```python
class BarState(rx.State):
    data = data

    @rx.event
    def randomize_data(self):
        for i in range(len(self.data)):
            self.data[i]["uv"] = random.randint(0, 10000)
            self.data[i]["pv"] = random.randint(0, 10000)
            self.data[i]["amt"] = random.randint(0, 10000)

def bar_with_state():
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.bar(data_key="uv", stroke=rx.color("accent", 9), fill=rx.color("accent", 8)),
        rx.recharts.bar(data_key="pv", stroke=rx.color("green", 9), fill=rx.color("green", 8)),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        rx.recharts.legend(),
        on_click=BarState.randomize_data,
        data=BarState.data,
        width="100%",
        height=300
    )
```

For more details, you can refer to the [example with props](https://reflex.dev/docs/library/graphing/charts/barchart/#example-with-props).

# Example with Props

Here's an example demonstrates how to customize the appearance and layout of bars using the `bar_category_gap`, `bar_gap`, `bar_size`, and `max_bar_size` props. These props accept values in pixels to control the spacing and size of the bars.

The bar chart displays data for different pages, with each page represented as a bar:

- Page A: 62.40000000000001
- Page B: 36.347999999999985
- Page C: 254.79999999999998
- Page D: 101.608
- Page E: 124.79999999999998
- Page F: 98.79999999999998

The code example is as follows:

```python
def bar_features():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=data,
        bar_category_gap="15%",
        bar_gap=6,
        bar_size=100,
        max_bar_size=40,
        width="100%",
        height=300,
    )
```

For more details, you can refer to the [Reflex documentation](https://reflex.dev/docs/library/graphing/charts/barchart/#vertical-example).

# Vertical Example

The `layout` prop allows you to set the orientation of the graph to be vertical or horizontal, it is set horizontally by default.

Include margins around your graph to ensure proper spacing and enhance readability. By default, provide margins on all sides of the chart to create a visually appealing and functional representation of your data.

```python
def bar_vertical():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="uv",
            stroke=rx.color("accent", 8),
            fill=rx.color("accent", 3),
        ),
        rx.recharts.x_axis(type_="number"),
        rx.recharts.y_axis(data_key="name", type_="category"),
        data=data,
        layout="vertical",
        margin={
            "top": 20,
            "right": 20,
            "left": 20,
            "bottom": 20,
        },
        width="100%",
        height=300,
    )
```

To learn how to use the `sync_id`, `stack_id`, `x_axis_id`, and `y_axis_id` props check out the area chart [documentation](/docs/library/graphing/charts/areachart/), where these props are all described with examples.

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/barchart/#rx.recharts.barchart)

# rx.recharts.BarChart

A Bar chart component in Recharts.

## Properties

- **bar_category_gap**: `Union[str, int]`  
  Default: `"10%"`

- **bar_gap**: `Union[str, int]`  
  Default: `4`

- **bar_size**: `int`

- **max_bar_size**: `int`

- **stack_offset**: `"expand" | "none" | ...`  
  Default: `"none"`

- **reverse_stack_order**: `bool`  
  Default: `False`

- **data**: `Sequence`

- **margin**: `Dict[str, Any]`

- **sync_id**: `str`

- **sync_method**: `"index" | "value"`  
  Default: `"index"`

- **layout**: `"vertical" | "horizontal"`  
  Default: `"horizontal"`

- **width**: `Union[str, int]`  
  Default: `Var.create("100%")`

- **height**: `Union[str, int]`  
  Default: `Var.create("100%")`

# Valid Children
* Cell
* LabelList
* ErrorBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_animation_start**
  The customized event handler of animation start
  
- **on_animation_end**
  The customized event handler of animation end

# rx.recharts.Bar

A Bar component in Recharts.

## Properties

- **stroke**
  - Type: `Union[str, Color]`
  - Default: None

- **stroke_width**
  - Type: `int`
  - Default: None

- **fill**
  - Type: `Union[str, Color]`
  - Default: `Color("accent", 9)`

- **background**
  - Type: `bool`
  - Default: `False`

- **label**
  - Type: `bool`
  - Default: `False`

- **stack_id**
  - Type: `str`
  - Default: None

- **unit**
  - Type: `Union[str, int]`
  - Default: None

- **min_point_size**
  - Type: `int`
  - Default: None

- **name**
  - Type: `Union[str, int]`
  - Default: None

- **bar_size**
  - Type: `int`
  - Default: None

- **max_bar_size**
  - Type: `int`
  - Default: None

- **radius**
  - Type: `Union[int, Sequence]`
  - Default: `0`

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

# Valid Children
* Cell
* LabelList
* ErrorBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_animation_start**
  - The customized event handler of animation start
  
- **on_animation_end**
  - The customized event handler of animation end