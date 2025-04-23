# Grid

Component for creating grid layouts. Either `rows` or `columns` may be specified.

[Basic Example](https://reflex.dev/docs/library/layout/grid/)

# Basic Example

Card 1
Card 2
Card 3
Card 4
Card 5
Card 6
Card 7
Card 8
Card 9
Card 10
Card 11
Card 12

```python
rx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
    ),
    columns="3",
    spacing="4",
    width="100%",
)
```

Card 1
Card 2
Card 3
Card 4
Card 5
Card 6
Card 7
Card 8
Card 9
Card 10
Card 11
Card 12

```python
rx.grid(
    rx.foreach(
        rx.Var.range(12),
        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
    ),
    rows="3",
    flow="column",
    justify="between",
    spacing="4",
    width="100%",
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/grid/#rx.grid)

# rx.grid

Component for creating grid layouts.

## Test

### Props

| Prop       | Type | Default | Interactive |
|------------|------|---------|-------------|
| as_child   | bool |         |             |
| columns    | str  |         |             |
| rows       | str  |         |             |
| flow       | "row" |        | <select><option value="row">row</option><option value="column">column</option></select>... |
| align      | "start" |       | <select><option value="start">start</option><option value="center">center</option></select>... |
| justify    | "start" |       | <select><option value="start">start</option><option value="center">center</option></select>... |
| spacing    | "0" |        | <select><option value="0">0</option><option value="1">1</option></select>... |
| spacing_x  | "0" |        | <select><option value="0">0</option><option value="1">1</option></select>... |
| spacing_y  | "0" |        | <select><option value="0">0</option><option value="1">1</option></select>... |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)