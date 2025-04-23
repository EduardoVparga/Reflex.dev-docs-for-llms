# Grid

A simple responsive grid layout. We specify the number of columns to the `grid_template_columns` property as a list. The grid will automatically adjust the number of columns based on the screen size.

For details, see the [responsive docs page](/docs/styling/responsive/).

# Cards

![Link](https://reflex.dev/docs/recipes/content/grid/#inset-cards)

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
    gap="1rem",
    grid_template_columns=[
        "1fr",
        "repeat(2, 1fr)",
        "repeat(2, 1fr)",
        "repeat(3, 1fr)",
        "repeat(4, 1fr)",
    ],
    width="100%",
)
```

# Inset cards

## Card 1  
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
        lambda i: rx.card(
            rx.inset(
                rx.image(
                    src="/reflex_banner.png",
                    width="100%",
                    height="auto"
                ),
                side="top",
                pb="current"
            ),
            rx.text(f"Card {i + 1}")
        )
    ),
    gap="1rem",
    grid_template_columns=[
        "1fr",
        "repeat(2, 1fr)",
        "repeat(2, 1fr)",
        "repeat(3, 1fr)",
        "repeat(4, 1fr)"
    ],
    width="100%"
)
```