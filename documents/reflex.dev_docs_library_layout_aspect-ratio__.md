# Aspect Ratio
Displays content with a desired ratio.

[Learn More](https://reflex.dev/docs/library/layout/aspect-ratio/#basic-example)

# Basic Example

Setting the `ratio` prop will adjust the width or height of the content such that the `width` divided by the `height` equals the `ratio`. For responsive scaling, set the `width` or `height` of the content to `"100%"`.

- Widescreen 16:9
- Letterbox 4:3
- Square 1:1
- Portrait 5:7

```python
rx.grid(
    rx.aspect_ratio(
        rx.box(
            "Widescreen 16:9",
            background_color="papayawhip",
            width="100%",
            height="100%"
        ),
        ratio=16 / 9,
    ),
    rx.aspect_ratio(
        rx.box(
            "Letterbox 4:3",
            background_color="orange",
            width="100%",
            height="100%"
        ),
        ratio=4 / 3,
    ),
    rx.aspect_ratio(
        rx.box(
            "Square 1:1",
            background_color="green",
            width="100%",
            height="100%"
        ),
        ratio=1,
    ),
    rx.aspect_ratio(
        rx.box(
            "Portrait 5:7",
            background_color="lime",
            width="100%",
            height="100%"
        ),
        ratio=5 / 7,
    ),
    spacing="2",
    width="25%",
)
```

# Never set `height` or `width` directly on an `aspect_ratio` component or its contents.

- Always use the aspect ratio component to maintain the correct proportions of your images and other content.
- For example, if you have a logo image that needs to maintain its aspect ratio regardless of the container size, use the `rx.aspect_ratio` component with the appropriate `ratio` value.

```python
rx.flex(
    [*[
        rx.box(
            rx.aspect_ratio(
                rx.image(
                    src="/logo.jpg",
                    width="100%",
                    height="100%",
                ),
                ratio=ratio,
            ),
            width="20%",
        )
        for ratio in [16 / 9, 3 / 2, 2 / 3, 1]
    ],
    justify="between",
    width="100%",
)
```

[Copy Code](#)

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/aspect-ratio/#rx.aspect_ratio)

# rx.aspect_ratio

Displays content with a desired ratio.

## Test

### Properties

- **Prop**: `ratio`
- **Type | Values**: `Union[int, float]`
- **Default**: Not specified
- **Interactive**: No

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)