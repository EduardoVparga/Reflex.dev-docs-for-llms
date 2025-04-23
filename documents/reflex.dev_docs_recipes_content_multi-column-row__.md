# Multi-column and row layout
A simple responsive multi-column and row layout. We specify the number of columns/rows to the `flex_direction` property as a list. The layout will automatically adjust the number of columns/rows based on the screen size.

For details, see the [responsive docs page](/docs/styling/responsive/).

# Column

## Python Code Example 1

```python
rx.flex(
    rx.box(
        bg=rx.color("accent", 3),
        width="100%",
        height="100%",
    ),
    rx.box(
        bg=rx.color("accent", 5),
        width="100%",
        height="100%",
    ),
    rx.box(
        bg=rx.color("accent", 7),
        width="100%",
        height="100%",
    ),
    bg=rx.color("accent", 10),
    spacing="4",
    padding="1em",
    flex_direction=["column", "column", "row"],
    height="600px",
    width="100%",
)
```

![Copy Code](https://reflex.dev/docs/recipes/content/multi-column-row/#row)

## Python Code Example 2

```python
rx.flex(
    rx.box(
        bg=rx.color("accent", 3),
        width="100%",
        height="100%",
    ),
    rx.box(
        bg=rx.color("accent", 5),
        width=["100%", "100%", "50%"],
        height=["50%", "50%", "100%"],
    ),
    rx.box(
        bg=rx.color("accent", 7),
        width="100%",
        height="100%",
    ),
    rx.box(
        bg=rx.color("accent", 9),
        width=["100%", "100%", "50%"],
        height=["50%", "50%", "100%"],
    ),
    bg=rx.color("accent", 10),
    spacing="4",
    padding="1em",
    flex_direction=["column", "column", "row"],
    height="600px",
    width="100%",
)
```

![Copy Code](https://reflex.dev/docs/recipes/content/multi-column-row/#row)

# Row

[![Link](/lucide/link.svg)](/)

```python
rx.flex(
    rx.flex(
        rx.box(
            bg=rx.color("accent", 3),
            width=["100%", "100%", "50%"],
            height="100%",
        ),
        rx.box(
            bg=rx.color("accent", 5),
            width=["100%", "100%", "50%"],
            height="100%",
        ),
        width="100%",
        height="100%",
        spacing="4",
        flex_direction=["column", "column", "row"],
    ),
    rx.box(
        bg=rx.color("accent", 7),
        width="100%",
        height="50%",
    ),
    rx.box(
        bg=rx.color("accent", 9),
        width="100%",
        height="50%",
    ),
    bg=rx.color("accent", 10),
    spacing="4",
    padding="1em",
    flex_direction="column",
    height="600px",
    width="100%",
)
```