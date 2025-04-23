# Stack

Stack is a layout component used to group elements together and apply a space between them.

`vstack` is used to stack elements in the vertical direction.

`hstack` is used to stack elements in the horizontal direction.

`stack` is used to stack elements in the vertical or horizontal direction.

These components are based on the `flex` component and therefore inherit all of its props. The `stack` component can be used with the `flex_direction` prop to set to either `row` or `column` to set the direction.

Example:

```python
rx.flex(
    rx.stack(
        rx.box(
            "Example",
            bg="orange",
            border_radius="3px",
            width="20%",
        ),
        rx.box(
            "Example",
            bg="lightblue",
            border_radius="3px",
            width="30%",
        ),
        rx.box(
            "Example",
            bg="lightgreen",
            border_radius="3px",
            width="50%",
        ),
        flex_direction="row",
        width="100%",
    ),
    rx.stack(
        rx.box(
            "Example",
            bg="orange",
            border_radius="3px",
            width="20%",
        ),
        rx.box(
            "Example",
            bg="lightblue",
            border_radius="3px",
            width="30%",
        ),
        rx.box(
            "Example",
            bg="lightgreen",
            border_radius="3px",
            width="50%",
        ),
        flex_direction="column",
        width="100%",
    ),
    width="100%",
)
```

[Learn More](https://reflex.dev/docs/library/layout/stack/#hstack)

# Hstack

Example
Example
Example
Example
Example

```python
rx.hstack(
    rx.box(
        "Example",
        bg="red",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="orange",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="yellow",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="lightblue",
        border_radius="3px",
        width="10%",
    ),
    rx.box(
        "Example",
        bg="lightgreen",
        border_radius="3px",
        width="60%",
    ),
    width="100%",
)
```

[Link to Reflex docs](https://reflex.dev/docs/library/layout/stack/#vstack)

# Vstack

Example
Example
Example
Example
Example

```python
rx.vstack(
    rx.box(
        "Example",
        bg="red",
        border_radius="3px",
        width="20%",
    ),
    rx.box(
        "Example",
        bg="orange",
        border_radius="3px",
        width="40%",
    ),
    rx.box(
        "Example",
        bg="yellow",
        border_radius="3px",
        width="60%",
    ),
    rx.box(
        "Example",
        bg="lightblue",
        border_radius="3px",
        width="80%",
    ),
    rx.box(
        "Example",
        bg="lightgreen",
        border_radius="3px",
        width="100%",
    ),
    width="100%",
)
```

[Real-world example](https://reflex.dev/docs/library/layout/stack/#real-world-example)

# Real World Example

[![Link](/link-to-example)](/link-to-example)

<div>
  <div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack">
      <div></div>
    </div>
  </div>
</div>

# Saving Money
Saving money is an art that combines discipline, strategic planning, and the wisdom to foresee future needs and emergencies. It begins with the simple act of setting aside a portion of one's income, creating a buffer that can grow over time through interest or investments.

# Spending Money

Spending money is a balancing act between fulfilling immediate desires and maintaining long-term financial health. It's about making choices, sometimes indulging in the pleasures of the moment, and at other times, prioritizing essential expenses.

---

## Saving Money

Saving money is an art that combines discipline, strategic planning, and the wisdom to foresee future needs and emergencies. It begins with the simple act of setting aside a portion of one's income, creating a buffer that can grow over time through interest or investments.

## Spending Money

Spending money is a balancing act between fulfilling immediate desires and maintaining long-term financial health. It's about making choices, sometimes indulging in the pleasures of the moment, and at other times, prioritizing essential expenses.

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/stack/#rx.stack)

# rx.stack

A stack component.

## Cards
- Card 1
- Card 2
- Card 3

### Props
| Prop | Type | Default | Interactive |
| --- | --- | --- | --- |
| spacing | `"0" | "1" | ...` | `Var.create("3")` | - |
| align | `"start" | "center" | ..."` | `Var.create("start")` | - |
| as_child | `bool` |  | - |
| direction | `"row" | "column" | ..."` |  | <button>row</button> |
| justify | `"start" | "center" | ..."` |  | <button>start</button> |
| wrap | `"nowrap" | "wrap" | ..."` |  | <button>nowrap</button> |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.hstack

A horizontal stack component.

## Test

### Props

| Prop | Type | Default | Interactive |
| --- | --- | --- | --- |
| direction | `"row" | "column"` | `Var.create("row")` | - |
| spacing | `"0" | "1" | ...` | `Var.create("3")` | - |
| align | `"start" | "center" | ...` | `Var.create("start")` | - |
| as_child | `bool` |  | - |
| justify | `"start" | "center" | ...` |  | - |
| wrap | `"nowrap" | "wrap"` |  | - |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.vstack

A vertical stack component.

## Test

### Props

| Prop     | Type | Default         | Interactive |
|----------|------|-----------------|-------------|
| direction | "row" | "column" | Var.create("column") | Dropdown  |
| spacing   | "0"  | "3"    | Var.create("3")      | Dropdown  |
| align     | "start"| "center" | Var.create("start")  | Dropdown  |
| as_child  | bool | -               | -            |
| justify   | "start"| "center" | -                | Dropdown  |
| wrap      | "nowrap"| "wrap" | -                | Dropdown  |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)