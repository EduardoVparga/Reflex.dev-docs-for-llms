# Spacer

Creates an adjustable, empty space that can be used to tune the spacing between child elements within `flex`.

## Example

Example
---
Example
---
Example

```python
rx.flex(
    rx.center(rx.text("Example", bg="lightblue")),
    rx.spacer(),
    rx.center(rx.text("Example", bg="lightgreen")),
    rx.spacer(),
    rx.center(rx.text("Example", bg="salmon"), width="100%"),
)
```

As `stack`, `vstack` and `hstack` are all built from `flex`, it is possible to also use `spacer` inside of these components.

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/spacer/#rx.spacer)

# rx.spacer

A spacer component.

## Test

---

### Props

| Prop         | Type | Values                    | Default | Interactive |
| ------------ | ---- | ------------------------- | ------- | ---------- |
| as_child     | bool | -                         | -       |            |
| direction    | str  | "row" | "column" | ...        | -          |
| align        | str  | "start" | "center" | ...        | -          |
| justify      | str  | "start" | "center" | ...        | -          |
| wrap         | str  | "nowrap" | "wrap"   | ...        | -          |
| spacing      | str  | "0" | "1"     | ...        | -          |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)