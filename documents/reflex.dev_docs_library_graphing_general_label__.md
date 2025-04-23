# Label
Label is a component used to display a single label at a specific position within a chart or axis, while LabelList is a component that automatically renders a list of labels for each data point in a chart series, providing a convenient way to display multiple labels without manually positioning each one.

[Learn More](https://reflex.dev/docs/library/graphing/general/label/#simple-example)

# Simple Example

Here's a simple example that demonstrates how you can customize the label of your axis using `rx.recharts.label`. The `value` prop represents the actual text of the label, the `position` prop specifies where the label is positioned within the axis component, and the `offset` prop is used to fine-tune the label's position.

```python
def label_simple():
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.bar(
            rx.recharts.label_list(data_key="uv", position="top"),
            data_key="uv",
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(
            rx.recharts.label(
                value="center",
                position="center",
                offset=30,
            ),
            rx.recharts.label(
                value="inside left",
                position="insideLeft",
                offset=10,
            ),
            rx.recharts.label(
                value="inside right",
                position="insideRight",
                offset=10,
            ),
            height=50,
        ),
        data=data,
        margin={
            "left": 20,
            "right": 20,
            "top": 20,
            "bottom": 20,
        },
        width="100%",
        height=250,
    )
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/graphing/general/label/#label-list-example">Learn More</a>

# Label List Example

rx.recharts.label_list takes in a `data_key` where we define the data column to plot.

<div class="rt-Box w-full py-4 flex flex-col">
  <div class="rt-Flex w-full flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center">
    <svg height="300" style="width:100%;height:300px;min-width:10px;min-height:10px" viewBox="0 0 107 300" width="107">
      <!-- SVG content omitted for brevity -->
    </svg>
  </div>
</div>

<div class="rt-TabsRoot w-full mt-6 justify-end css-1ysbne9" data-orientation="horizontal" dir="ltr">
  <div aria-orientation="horizontal" class="rt-BaseTabList rt-TabsList rt-r-size-2 css-ishps6" data-orientation="horizontal" role="tablist" style="outline:none" tabindex="0">
    <button aria-controls="radix-:Rl56kml6:-content-code" aria-selected="true" class="rt-reset rt-BaseTabListTrigger rt-TabsTrigger tab-style css-1eafhys" data-orientation="horizontal" data-radix-collection-item="" data-state="active" id="radix-:Rl56kml6:-trigger-code" role="tab" tabindex="-1" type="button">
      <span class="rt-BaseTabListTriggerInner rt-TabsTriggerInner">Code</span>
    </button>
    <button aria-controls="radix-:Rl56kml6:-content-data" aria-selected="false" class="rt-reset rt-BaseTabListTrigger rt-TabsTrigger tab-style css-1eafhys" data-orientation="horizontal" data-radix-collection-item="" data-state="inactive" id="radix-:Rl56kml6:-trigger-data" role="tab" tabindex="-1" type="button">
      <span class="rt-BaseTabListTriggerInner rt-TabsTriggerInner">Data</span>
    </button>
  </div>
  <div aria-labelledby="radix-:Rl56kml6:-trigger-code" class="rt-TabsContent w-full px-0 css-10qvqtq" data-orientation="horizontal" data-state="active" id="radix-:Rl56kml6:-content-code" role="tabpanel" style="animation-duration:0s" tabindex="0">
    <div class="rt-Box relative mb-4">
      <pre><code>
def label_list():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            rx.recharts.label_list(data_key="uv", position="top"),
            data_key="uv",
            stroke="#8884d8",
            fill="#8884d8",
        ),
        rx.recharts.bar(
            rx.recharts.label_list(data_key="pv", position="top"),
            data_key="pv",
            stroke="#82ca9d",
            fill="#82ca9d",
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        margin={
            "left": 10,
            "right": 0,
            "top": 20,
            "bottom": 10,
        },
        data=data,
        width="100%",
        height=300,
    )
      </code></pre>
    </div>
  </div>
</div>

[Learn more](https://reflex.dev/docs/library/graphing/general/label/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/general/label/#rx.recharts.label)

# rx.recharts.Label

A Label component in Recharts.

## Props

- **view_box**: `Dict[str, Any]`
- **value**: `str`
- **offset**: `int`
- **position**: `"top" | "left" | ...`

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.recharts.LabelList

A LabelList component in Recharts.

## Props

- **Prop** | **Type | Values** | **Default**
  - `data_key` | `Union[str, int]` | -
  - `position` | `"top" | "left" | ..."` | -
  - `offset` | `int` | `5`
  - `fill` | `Union[str, Color]` | `rx.color("gray", 10)`
  - `stroke` | `Union[str, Color]` | `"none"`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)