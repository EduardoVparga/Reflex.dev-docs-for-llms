# Center

`Center` is a component that centers its children within itself. It is based on the `flex` component and therefore inherits all of its props.

## Example Usage

```python
rx.center(
    rx.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="50%",
)
```

For more details, see [API Reference](/docs/library/layout/center/#api-reference)

# API Reference

[API Reference](/docs/library/layout/center/#rx.center)

# rx.center

A center component.

## Test

---

Prop | Type | Default | Interactive  
--- | --- | --- | ---  
as_child | bool |  |   
direction | "row" | "column" | ... | row  
align | "start" | "center" | ... | start  
justify | "start" | "center" | ... | start  
wrap | "nowrap" | "wrap" | ... | nowrap  
spacing | "0" | "1" | ... | 0

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)