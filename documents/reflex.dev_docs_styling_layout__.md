# Layout Components

Layout components such as `rx.flex`, `rx.container`, `rx.box`, etc. are used to organize and structure the visual presentation of your application. This page gives a breakdown of when and how each of these components might be used.

<div class="css-10ddbmu" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-tzz23y" data-orientation="vertical" data-state="closed">

# Video: Example of Laying Out the Main Content of a Page

[View Documentation](https://reflex.dev/docs/styling/layout/#box)

# Box

`rx.box` is a generic component that can apply any CSS style to its children. It's a building block that can be used to apply a specific layout or style property.

**When to use:** Use `rx.box` when you need to apply specific styles or constraints to a part of your interface.

- **CSS color**
- **Radix Color**

```python
rx.box(
    rx.box(
        "CSS color",
        background_color="red",
        border_radius="2px",
        width="50%",
        margin="4px",
        padding="4px",
    ),
    rx.box(
        "Radix Color",
        background_color=rx.color("tomato", 3),
        border_radius="5px",
        width="80%",
        margin="12px",
        padding="12px",
    ),
    text_align="center",
    width="100%",
)
```

[Learn more about styling and layout](https://reflex.dev/docs/styling/layout/#stack)

# Stack

`rx.stack` is a layout component that arranges its children in a single column or row, depending on the direction. It’s useful for consistent spacing between elements.

## When to use:
Use `rx.stack` when you need to lay out a series of components either vertically or horizontally with equal spacing.

### Example

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
        flex_direction="column",
        width="100%",
    ),
    width="100%",
)
```

For more information, see [Flex Layout](https://reflex.dev/docs/styling/layout/#flex).

# Flex

The `rx.flex` component is used to create a flexible box layout, inspired by CSS Flexbox. It's ideal for designing a layout where the size of the items can grow and shrink dynamically based on the available space.

**When to use:** Use `rx.flex` when you need a responsive layout that adjusts the size and position of child components dynamically.

## Example

```python
rx.flex(
    rx.card("Card 1"),
    rx.card("Card 2"),
    rx.card("Card 3"),
    spacing="2",
    width="100%",
)
```

![Copy Code](https://reflex.dev/docs/styling/layout/#grid)

# Grid

`rx.grid` components are used to create complex responsive layouts based on a grid system, similar to CSS Grid Layout.

## When to use:
Use `rx.grid` when dealing with complex layouts that require rows and columns, especially when alignment and spacing among multiple axes are needed.

### Example Usage:

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

For more details, see the [Reflex documentation](https://reflex.dev/docs/styling/layout/#container).

# Container

The `rx.container` component typically provides padding and fixes the maximum width of the content inside it, often used to center content on large screens.

**When to use:** Use `rx.container` for wrapping your application’s content in a centered block with some padding.

## Examples

- This content is constrained to a max width of 448px.
- This content is constrained to a max width of 688px.
- This content is constrained to a max width of 880px.

```python
rx.box(
    rx.container(
        rx.card(
            "This content is constrained to a max width of 448px.",
            width="100%",
        ),
        size="1",
    ),
    rx.container(
        rx.card(
            "This content is constrained to a max width of 688px.",
            width="100%",
        ),
        size="2",
    ),
    rx.container(
        rx.card(
            "This content is constrained to a max width of 880px.",
            width="100%",
        ),
        size="3",
    ),
    background_color="var(--gray-3)",
    width="100%",
)
```