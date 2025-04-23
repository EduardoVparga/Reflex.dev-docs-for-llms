# List

A `list` is a component that is used to display a list of items, stacked vertically by default. A `list` can be either `ordered` or `unordered`. It is based on the `flex` component and therefore inherits all of its props.

`list.unordered` has bullet points to display the list items.

- Example 1
- Example 2
- Example 3

```python
rx.list.unordered(
    rx.list.item("Example 1"),
    rx.list.item("Example 2"),
    rx.list.item("Example 3"),
)
```

`list.ordered` has numbers to display the list items.

1. Example 1
2. Example 2
3. Example 3

```python
rx.list.ordered(
    rx.list.item("Example 1"),
    rx.list.item("Example 2"),
    rx.list.item("Example 3"),
)
```

`list.unordered()` and `list.ordered()` can have no bullet points or numbers by setting the `list_style_type` prop to `none`. This is effectively the same as using the `list()` component.

- Example 1
- Example 2
- Example 3

```python
rx.hstack(
    rx.list(
        rx.list.item("Example 1"),
        rx.list.item("Example 2"),
        rx.list.item("Example 3"),
    ),
    rx.list.unordered(
        rx.list.item("Example 1"),
        rx.list.item("Example 2"),
        rx.list.item("Example 3"),
        list_style_type="none",
    ),
)
```

Lists can also be used with icons.

- [✓] Allowed
- [✗] Not
- [⚙️] Settings

```python
rx.list(
    rx.list.item(
        rx.icon("circle_check_big", color="green"), " Allowed"
    ),
    rx.list.item(
        rx.icon("octagon_x", color="red"), " Not"
    ),
    rx.list.item(
        rx.icon("settings", color="grey"), " Settings"
    ),
    list_style_type="none",
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/list/#rx.list.item)

# rx.list.item

Display an item of an ordered or unordered list.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props

No component specific props

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.list.ordered

Display an ordered list.

## Properties

- **Prop** | **Type | Values** | **Default**
  - `list_style_type` | `"none" | "disc" | ...` | -
  - `items` | `Iterable` | `Var.create([])`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.list.unordered

Display an unordered list.

## Props

- **list_style_type**
  - **Type | Values**: `"none" | "disc" | ...`
  - **Default**: Not specified

- **items**
  - **Type | Values**: `Iterable`
  - **Default**: `Var.create([])`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)