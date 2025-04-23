# Radar Chart

A radar chart shows multivariate data of three or more quantitative variables mapped onto an axis.

[Simple Example](https://reflex.dev/docs/library/graphing/charts/radarchart/#simple-example)

# Simple Example

For a radar chart we must define an `rx.recharts.radar()` component for each set of values we wish to plot. Each `rx.recharts.radar()` component has a `data_key` which clearly states which variable in our data we are plotting. In this simple example we plot the `A` column of our data against the `subject` column which we set as the `data_key` in `rx.recharts.polar_angle_axis`.

<div class="rt-Box w-full py-4 flex flex-col">
  <div class="rt-Flex w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center">
    <svg class="recharts-responsive-container" style="width:100%;height:300px;min-width:10px;min-height:10px">
      <!-- SVG content is not converted to Markdown -->
    </svg>
  </div>
</div>

<div class="rt-TabsRoot w-full mt-6 justify-end css-1ysbne9" data-orientation="horizontal" dir="ltr">
  <div aria-orientation="horizontal" class="rt-BaseTabList rt-TabsList rt-r-size-2 css-ishps6" data-orientation="horizontal" role="tablist" style="outline:none" tabindex="0">
    <button aria-controls="radix-:R18p6kml6:-content-code" aria-selected="true" class="rt-reset rt-BaseTabListTrigger rt-TabsTrigger tab-style css-1eafhys" data-orientation="horizontal" data-radix-collection-item="" data-state="active" id="radix-:R18p6kml6:-trigger-code" role="tab" tabindex="-1" type="button">
      <span class="rt-BaseTabListTriggerInner rt-TabsTriggerInner">Code</span>
    </button>
    <button aria-controls="radix-:R18p6kml6:-content-data" aria-selected="false" class="rt-reset rt-BaseTabListTrigger rt-TabsTrigger tab-style css-1eafhys" data-orientation="horizontal" data-radix-collection-item="" data-state="inactive" id="radix-:R18p6kml6:-trigger-data" role="tab" tabindex="-1" type="button">
      <span class="rt-BaseTabListTriggerInner rt-TabsTriggerInner">Data</span>
    </button>
  </div>
  <div aria-labelledby="radix-:R18p6kml6:-trigger-code" class="rt-TabsContent w-full px-0 css-10qvqtq" data-orientation="horizontal" data-state="active" id="radix-:R18p6kml6:-content-code" role="tabpanel" style="animation-duration:0s" tabindex="0">
    <div class="rt-Box relative mb-4">
      <div class="rt-Box code-block css-1islnds">
        <pre><code>
def radar_simple():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.polar_radius_axis(
            angle=90,
            domain=[0, 150]
        ),
        data=data,
        width="100%",
        height=300,
    )
</code></pre>
      </div>
    </div>
  </div>
  <div aria-labelledby="radix-:R18p6kml6:-trigger-data" class="rt-TabsContent w-full px-0 css-10qvqtq" data-orientation="horizontal" data-state="inactive" hidden="" id="radix-:R18p6kml6:-content-data" role="tabpanel" tabindex="0"></div>
</div>

# Multiple Radars

We can also add two radars on one chart by using two `rx.recharts.radar` components.

In this plot an `inner_radius` and an `outer_radius` are set which determine the chart's size and shape. The `inner_radius` sets the distance from the center to the innermost part of the chart (creating a hollow center if greater than zero), while the `outer_radius` defines the chart's overall size by setting the distance from the center to the outermost edge of the radar plot.

Here is an example:

- `A`: #8884d8
- `B`: #82ca9d

```python
def radar_multiple():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.radar(
            data_key="B",
            stroke="#82ca9d",
            fill="#82ca9d",
            fill_opacity=0.6,
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.polar_radius_axis(angle=90, domain=[0, 150]),
        rx.recharts.legend(),
        data=data,
        inner_radius="15%",
        outer_radius="80%",
        width="100%",
        height=300,
    )
```

For more details and code examples, you can refer to the [Reflex documentation](https://reflex.dev/docs/library/graphing/charts/radarchart/#using-more-props).

# Using More Props

The `dot` prop shows points at each data vertex when true. `legend_type="line"` displays a line in the chart legend. `animation_begin=0` starts the animation immediately, `animation_duration=8000` sets an 8-second animation, and `animation_easing="ease-in"` makes the animation start slowly and speed up. These props control the chart's appearance and animation behavior.

## Code Example

```python
def radar_start_end():
    return rx.recharts.radar_chart(
        rx.recharts.radar(
            data_key="A",
            dot=True,
            stroke="#8884d8",
            fill="#8884d8",
            fill_opacity=0.6,
            legend_type="line",
            animation_begin=0,
            animation_duration=8000,
            animation_easing="ease-in",
        ),
        rx.recharts.polar_grid(),
        rx.recharts.polar_angle_axis(data_key="subject"),
        rx.recharts.polar_radius_axis(
            angle=90, domain=[0, 150]
        ),
        rx.recharts.legend(),
        data=data,
        width="100%",
        height=300,
    )
```

# Dynamic Data

Chart data tied to a State var causes the chart to automatically update when the state changes, providing a nice way to visualize data in response to user interface elements. View the "Data" tab to see the substate driving this radar chart of character traits.

## Character Traits

- **Strength**: 15
- **Dexterity**: 15
- **Constitution**: 15
- **Intelligence**: 15
- **Wisdom**: 15
- **Charisma**: 15

Remaining points: 10

```python
class RadarChartState(rx.State):
    total_points: int = 100
    traits: list[dict[str, Any]] = [
        dict(trait="Strength", value=15),
        dict(trait="Dexterity", value=15),
        dict(trait="Constitution", value=15),
        dict(trait="Intelligence", value=15),
        dict(trait="Wisdom", value=15),
        dict(trait="Charisma", value=15),
    ]

    @rx.var
    def remaining_points(self) -> int:
        return self.total_points - sum(t["value"] for t in self.traits)

    @rx.var(cache=True)
    def trait_names(self) -> list[str]:
        return [t["trait"] for t in self.traits]

    @rx.event
    def set_trait(self, trait: str, value: int):
        for t in self.traits:
            if t["trait"] == trait:
                available_points = (self.remaining_points + t["value"])
                value = min(value, available_points)
                t["value"] = value
                break

def radar_dynamic():
    return rx.hstack(
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="value",
                stroke="#8884d8",
                fill="#8884d8",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="trait"),
            data=RadarChartState.traits,
        ),
        rx.vstack(
            rx.foreach(RadarChartState.trait_names, lambda trait_name, i: rx.hstack(
                rx.text(trait_name, width="7em"),
                rx.slider(default_value=RadarChartState.traits[i]["value"].to(int), on_change=lambda value: RadarChartState.set_trait(trait_name, value), width="25vw"),
                rx.text(RadarChartState.traits[i]["value"]),
            )),
            rx.text("Remaining points: ", RadarChartState.remaining_points),
        ),
    )
```

<a href="https://reflex.dev/docs/library/graphing/charts/radarchart/#api-reference">View API Reference</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/charts/radarchart/#rx.recharts.radarchart)

# rx.recharts.RadarChart

A Radar chart component in Recharts.

## Properties

- **Prop** | **Type | Values** | **Default**
  - `data` | Sequence | -
  - `margin` | Dict[str, Any] | {"top": 0, "right": 0, "left": 0, "bottom": 0}
  - `cx` | Union[str, int] | "50%"
  - `cy` | Union[str, int] | "50%"
  - `start_angle` | int | 90
  - `end_angle` | int | -270
  - `inner_radius` | Union[str, int] | 0
  - `outer_radius` | Union[str, int] | "80%"
  - `width` | Union[str, int] | Var.create("100%")
  - `height` | Union[str, int] | Var.create("100%")

# Valid Children
LabelList

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_animation_start`
  - Description: The on_animation_start event handler is called when the animation starts. It receives the animation name as an argument.

- **Trigger**: `on_animation_end`
  - Description: The on_animation_end event handler is called when the animation ends. It receives the animation name as an argument.

# rx.recharts.Radar

A Radar chart component in Recharts.

## Props

| Prop       | Type | Values        | Default |
|------------|------|---------------|---------|
| `data_key` | Union[str, int] | -           | None    |
| `points`   | Sequence  | -            | None    |
| `dot`      | bool     | True         | True    |
| `stroke`   | Union[str, Color] | rx.color("accent", 9) | rx.color("accent", 9) |
| `fill`     | Union[str, Color] | rx.color("accent", 3) | rx.color("accent", 3) |
| `fill_opacity` | float  | 0.6         | 0.6     |
| `legend_type` | "line" | "rect"       | "rect"  |
| `label`    | bool    | True         | True    |
| `is_animation_active` | bool  | True in CSR, and False in SSR | True in CSR, and False in SSR |
| `animation_begin` | int   | 0           | 0       |
| `animation_duration` | int  | 1500        | 1500    |
| `animation_easing` | "ease" | "ease", "ease-in", ... | "ease"  |

# Valid Children
LabelList

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

## Trigger | Description
- **on_animation_start** - The on_animation_start event handler is called when the animation starts. It receives the animation name as an argument.
- **on_animation_end** - The on_animation_end event handler is called when the animation ends. It receives the animation name as an argument.