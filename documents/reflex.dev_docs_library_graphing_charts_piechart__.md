# Pie Chart

A pie chart is a circular statistical graphic which is divided into slices to illustrate numerical proportion.

For a pie chart we must define an `rx.recharts.pie()` component for each set of values we wish to plot. Each `rx.recharts.pie()` component has a `data`, a `data_key` and a `name_key` which clearly states which data and which variables in our data we are tracking. In this simple example we plot `value` column as our `data_key` against the `name` column which we set as our `name_key`.
We also use the `fill` prop to set the color of the pie slices.

## Code

```python
def pie_simple():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            fill="#8884d8",
            label=True,
        ),
        width="100%",
        height=300,
    )
```

We can also add two pies on one chart by using two `rx.recharts.pie` components.

In this example `inner_radius` and `outer_radius` props are used. They define the doughnut shape of a pie chart: `inner_radius` creates the hollow center (use "0%" for a full pie), while `outer_radius` sets the overall size. The `padding_angle` prop, used on the green pie below, adds space between pie slices, enhancing visibility of individual segments.

## Code

```python
def pie_double():
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data01,
            data_key="value",
            name_key="name",
            fill="#82ca9d",
            inner_radius="60%",
            padding_angle=5,
        ),
        rx.recharts.pie(
            data=data02,
            data_key="value",
            name_key="name",
            fill="#8884d8",
            outer_radius="50%",
        ),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=300,
    )
```

# Dynamic Data

Chart data tied to a State var causes the chart to automatically update when the state changes, providing a nice way to visualize data in response to user interface elements. View the "Data" tab to see the substate driving this half-pie chart.

- 🏆 1
- 🪵 1
- 🥑 1
- 🧱 1

```python
from typing import Any

class PieChartState(rx.State):
    resources: list[dict[str, Any]] = [
        dict(type_="🏆", count=1),
        dict(type_="🪵", count=1),
        dict(type_="🥑", count=1),
        dict(type_="🧱", count=1),
    ]

    @rx.var(cache=True)
    def resource_types(self) -> list[str]:
        return [r["type_"] for r in self.resources]

    @rx.event
    def increment(self, type_: str):
        for resource in self.resources:
            if resource["type_"] == type_:
                resource["count"] += 1
                break

    @rx.event
    def decrement(self, type_: str):
        for resource in self.resources:
            if (resource["type_"] == type_
                    and resource["count"] > 0):
                resource["count"] -= 1
                break

def dynamic_pie_example():
    return rx.hstack(
        rx.recharts.pie_chart(
            rx.recharts.pie(
                data=PieChartState.resources,
                data_key="count",
                name_key="type_",
                cx="50%",
                cy="50%",
                start_angle=180,
                end_angle=0,
                fill="#8884d8",
                label=True,
            ),
            rx.recharts.graphing_tooltip(),
        ),
        rx.vstack(
            rx.foreach(PieChartState.resource_types, lambda type_, i: rx.hstack(
                rx.button("-", on_click=PieChartState.decrement(type_)),
                rx.text(type_, PieChartState.resources[i]["count"]),
                rx.button("+", on_click=PieChartState.increment(type_)),
            )),
        ),
    )
```

[More information](https://reflex.dev/docs/library/graphing/charts/piechart/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/piechart/#rx.recharts.piechart)

# rx.recharts.PieChart

A Pie chart component in Recharts.

## Props

- **Prop**: `margin`
  - **Type | Values**: `Dict[str, Any]`
  - **Default**: -
- **Prop**: `width`
  - **Type | Values**: `Union[str, int]`
  - **Default**: `Var.create("100%")`
- **Prop**: `height`
  - **Type | Values**: `Union[str, int]`
  - **Default**: `Var.create("100%")`

Valid Children
Cell
LabelList
Bare

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_animation_start`
  - Description: The on_animation_start event handler is called when the animation starts. It receives the animation name as an argument.
  
- **Trigger:** `on_animation_end`
  - Description: The on_animation_end event handler is called when the animation ends. It receives the animation name as an argument.

# rx.recharts.Pie

A Pie chart component in Recharts.

## Props

- **data**
  - Type: Sequence
  - Default: None

- **data_key**
  - Type: Union[str, int]
  - Default: None

- **cx**
  - Type: Union[str, int]
  - Default: "50%"

- **cy**
  - Type: Union[str, int]
  - Default: "50%"

- **inner_radius**
  - Type: Union[str, int]
  - Default: 0

- **outer_radius**
  - Type: Union[str, int]
  - Default: "80%"

- **start_angle**
  - Type: int
  - Default: 0

- **end_angle**
  - Type: int
  - Default: 360

- **min_angle**
  - Type: int
  - Default: 0

- **padding_angle**
  - Type: int
  - Default: 0

- **name_key**
  - Type: str
  - Default: "name"

- **legend_type**
  - Type: "line" | "plainline" | ...
  - Default: "rect"

- **label**
  - Type: bool
  - Default: False

- **label_line**
  - Type: bool
  - Default: False

- **stroke**
  - Type: Union[str, Color]
  - Default: rx.color("accent", 9)

- **fill**
  - Type: Union[str, Color]
  - Default: rx.color("accent", 3)

- **is_animation_active**
  - Type: bool
  - Default: true in CSR, and false in SSR

- **animation_begin**
  - Type: int
  - Default: 400

- **animation_duration**
  - Type: int
  - Default: 1500

- **animation_easing**
  - Type: "ease" | "ease-in" | ...
  - Default: "ease"

- **root_tab_index**
  - Type: int
  - Default: 0

# Valid Children
* Cell
* LabelList
* Bare

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_animation_start**
  The on_animation_start event handler is called when the animation starts. It receives the animation name as an argument.
  
- **on_animation_end**
  The on_animation_end event handler is called when the animation ends. It receives the animation name as an argument.