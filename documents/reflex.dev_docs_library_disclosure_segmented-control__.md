# Segmented Control
Segmented Control offers a clear and accessible way to switch between predefined values and views, e.g., "Inbox," "Drafts," and "Sent."

With Segmented Control, you can make mutually exclusive choices, where only one option can be active at a time, clear and accessible. Without Segmented Control, end users might have to deal with controls like dropdowns or multiple buttons that don't clearly convey state or group options together visually.

[View Basic Example](https://reflex.dev/docs/library/disclosure/segmented-control/#basic-example)

# Basic Example

The `Segmented Control` component is made up of a `rx.segmented_control.root` which groups `rx.segmented_control.item`.

The `rx.segmented_control.item` components define the individual segments of the control, each with a label and a unique value.

Home | About | Test

- Home
- About
- Test

```python
rx.vstack(
    rx.segmented_control.root(
        rx.segmented_control.item("Home", value="home"),
        rx.segmented_control.item("About", value="about"),
        rx.segmented_control.item("Test", value="test"),
        on_change=SegmentedState.setvar("control"),
        value=SegmentedState.control,
    ),
    rx.card(
        rx.text(SegmentedState.control, align="left"),
        rx.text(SegmentedState.control, align="center"),
        rx.text(SegmentedState.control, align="right"),
        width="100%",
    ),
)
```

In the example above:
- `on_change` is used to specify a callback function that will be called when the user selects a different segment. In this case, the `SegmentedState.setvar("control")` function is used to update the `control` state variable when the user changes the selected segment.
- `value` prop is used to specify the currently selected segment, which is bound to the `SegmentedState.control` state variable.

For more information, visit [Reflex Dev Documentation](https://reflex.dev/docs/library/disclosure/segmented-control/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/disclosure/segmented-control/#rx.segmented_control.root)

# rx.segmented_control.root
Root element for a SegmentedControl component.

## Test
<div>
  <div color="tomato" data-radius="none" dir="ltr" role="group" style="outline:none" tabindex="-1">Test</div>
</div>

### Properties

| Prop         | Type | Default | Interactive |
|--------------|------|---------|------------|
| size         | "1" | "2" | ...       | -          |
| variant      | "classic" | "surface" |           |            |
| type         | "single" | "multiple" |          |            |
| color_scheme | "tomato" | "red" | ...       |            |
| radius       | "none" | "small" | ...       |            |
| default_value| Union[str, Sequence] | -      |           |            |
| value        | Union[str, Sequence] | -      |           |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.segmented_control.item

An item in the SegmentedControl component.

## Prop

| Prop        | Type | Default | Interactive |
|-------------|------|---------|------------|
| value       | str  |         |            |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)