# Funnel Chart

A funnel chart is a graphical representation used to visualize how data moves through a process. In a funnel chart, the dependent variable’s value diminishes in the subsequent stages of the process. It can be used to demonstrate the flow of users through a business or sales process.

[View Simple Example](https://reflex.dev/docs/library/graphing/charts/funnelchart/#simple-example)

# Simple Example

![](https://reflex.dev/docs/library/graphing/charts/funnelchart/#event-triggers)

## Code

```python
def funnel_simple():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            rx.recharts.label_list(
                position="right",
                data_key="name",
                fill="#000",
                stroke="none",
            ),
            data_key="value",
            data=data,
        ),
        width="100%",
        height=250,
    )
```

# Event Triggers

Funnel chart supports `on_click`, `on_mouse_enter`, `on_mouse_leave` and `on_mouse_move` event triggers, allows you to interact with the funnel chart and perform specific actions based on user interactions.

## Code

```python
def funnel_events():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            rx.recharts.label_list(
                position="right",
                data_key="name",
                fill="#000",
                stroke="none"
            ),
            data_key="value",
            data=data,
        ),
        on_click=rx.toast("Clicked on funnel chart"),
        on_mouse_enter=rx.toast("Mouse entered"),
        on_mouse_leave=rx.toast("Mouse left"),
        width="100%",
        height=250,
    )
```

# Dynamic Data

Here is an example of a funnel chart with a `State`. Here we have defined a function `randomize_data`, which randomly changes the data when the graph is clicked on using `on_click=FunnelState.randomize_data`.

class FunnelState(rx.State):
    data = data

    @rx.event
    def randomize_data(self):
        self.data[0]["value"] = 100
        for i in range(len(self.data) - 1):
            self.data[i + 1]["value"] = self.data[i]["value"] - random.randint(0, 20)

def funnel_state():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            rx.recharts.label_list(
                position="right",
                data_key="name",
                fill="#000",
                stroke="none",
            ),
            data_key="value",
            data=FunnelState.data,
            on_click=FunnelState.randomize_data,
        ),
        rx.recharts.graphing_tooltip(),
        width="100%",
        height=250,
    )

# Changing the Chart Animation

The `is_animation_active` prop can be used to turn off the animation, but defaults to `True`. `animation_begin` sets the delay before animation starts, `animation_duration` determines how long the animation lasts, and `animation_easing` defines the speed curve of the animation for smooth transitions.

## Code

```python
def funnel_animation():
    return rx.recharts.funnel_chart(
        rx.recharts.funnel(
            data_key="value",
            data=data,
            animation_begin=300,
            animation_duration=9000,
            animation_easing="ease-in-out",
        ),
        rx.recharts.graphing_tooltip(),
        rx.recharts.legend(),
        width="100%",
        height=300,
    )
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/funnelchart/#rx.recharts.funnelchart)

# rx.recharts.FunnelChart

A Funnel chart component in Recharts.

## Props

| Prop       | Type | Default |
|------------|------|---------|
| layout     | str  | "centric" |
| margin    | Dict[str, Any] | {"top": 5, "right": 5, "bottom": 5, "left": 5} |
| stroke    | Union[str, Color] | - |
| width     | Union[str, int] | Var.create("100%") |
| height    | Union[str, int] | Var.create("100%") |

# Valid Children
- LabelList
- Cell

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

## Trigger | Description
- **on_animation_start** | Valid children components The customized event handler of animation start
- **on_animation_end** | The customized event handler of animation end

# rx.recharts.Funnel

A Funnel component in Recharts.

## Props

| Prop         | Type | Values             | Default |
|--------------|------|--------------------|---------|
| data         |      | Sequence           |         |
| data_key     |      | Union[str, int]    |         |
| name_key     |      | str                | "name"  |
| legend_type  |      | "line" | "plainline" ...    | "line"  |
| is_animation_active | bool | True               | 0       |
| animation_begin | int  | 1500               |         |
| animation_duration | int |                     |         |
| animation_easing | str | "ease" | "ease-in" ...      |         |
| stroke       |      | Union[str, Color]  | rx.color("gray", 3) |
| trapezoids   |      | Sequence           |         |

# Valid Children
- LabelList
- Cell

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

* `on_animation_start`
    - Valid children components The customized event handler of animation start
* `on_animation_end`
    - The customized event handler of animation end