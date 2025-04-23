# Radial Bar Chart

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/graphing/charts/radialbarchart/#simple-example">

# Simple Example

This example demonstrates how to use a `radial_bar_chart` with a `radial_bar`. The `radial_bar_chart` takes in `data` and then the `radial_bar` takes in a `data_key`. A radial bar chart is a circular visualization where data categories are represented by bars extending outward from a central point, with the length of each bar proportional to its value.

Fill color supports `rx.color()`, which automatically adapts to dark/light mode changes.

```python
def radial_bar_simple():
    return rx.recharts.radial_bar_chart(
        rx.recharts.radial_bar(
            data_key="x",
            min_angle=15,
        ),
        data=data,
        width="100%",
        height=500,
    )
```

The example also includes a chart with multiple sectors:

```plaintext
C: 1.782857142857143,1.782857142857143,0,0,52.60857142857143,248.45600042296718
D: 7.325714285714286,7.325714285714286,0,0,46.61608034372838,247.4944581500371
E: 12.868571428571428,12.868571428571428,0,1,41.40749838851505,254.4013106443966
F: 18.41142857142857,18.41142857142857,0,1,44.29428571428571,265.9447648628198
G: 23.954285714285714,23.954285714285714,0,1,57.659618061598685,273.5903662892982
H: 29.497142857142858,29.497142857142858,0,1,76.09612237360093,268.96039794972523
I: 35.03999999999999,35.03999999999999,0,1,88.53999999466309,250.00061156336986
```

For the code and data examples, see the tabs below:

- [Code](#)
- [Data](#)

[More details on Reflex documentation](https://reflex.dev/docs/library/graphing/charts/radialbarchart/#advanced-example)

# Advanced Example

The `start_angle` and `end_angle` define the circular arc over which the bars are distributed, while `inner_radius` and `outer_radius` determine the radial extent of the bars from the center.

## Code

```python
def radial_bar_advanced():
    return rx.recharts.radial_bar_chart(
        rx.recharts.radial_bar(
            data_key="uv",
            min_angle=90,
            background=True,
            label={
                "fill": "#666",
                "position": "insideStart",
            },
        ),
        data=data_radial_bar,
        inner_radius="10%",
        outer_radius="80%",
        start_angle=180,
        end_angle=0,
        width="100%",
        height=300,
    )
```

## Data

No data provided.

# API Reference

[![Link](https://reflex.dev/docs/library/graphing/charts/radialbarchart/#rx.recharts.radialbarchart)](#)

# rx.recharts.RadialBarChart

A RadialBar chart component in Recharts.

## Properties

- **data**
  - Type: Sequence
  - Default: None

- **margin**
  - Type: Dict[str, Any]
  - Default: {"top": 5, "right": 5, "left": 5, "bottom": 5}

- **cx**
  - Type: Union[str, int]
  - Default: "50%"

- **cy**
  - Type: Union[str, int]
  - Default: "50%"

- **start_angle**
  - Type: int
  - Default: 0

- **end_angle**
  - Type: int
  - Default: 360

- **inner_radius**
  - Type: Union[str, int]
  - Default: "30%"

- **outer_radius**
  - Type: Union[str, int]
  - Default: "100%"

- **bar_category_gap**
  - Type: Union[str, int]
  - Default: "10%"

- **bar_gap**
  - Type: str
  - Default: "4"

- **bar_size**
  - Type: int
  - Default: None

- **width**
  - Type: Union[str, int]
  - Default: Var.create("100%")

- **height**
  - Type: Union[str, int]
  - Default: Var.create("100%")

# Valid Children

- PolarAngleAxis
- PolarRadiusAxis
- PolarGrid
- Legend
- GraphingTooltip
- RadialBar

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)