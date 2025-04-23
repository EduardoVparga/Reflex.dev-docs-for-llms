# Scroll Area

Custom styled, cross-browser scrollable area using native functionality.

[View Basic Example](https://reflex.dev/docs/library/data-display/scroll-area/#basic-example)

# Basic Example

Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense “legible” and “readable” are often used synonymously, typographically they are separate but related concepts.

Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as “the quality of being decipherable and recognisable”. For instance, if a “b” and an “h”, or a “3” and an “8”, are difficult to distinguish at small sizes, this is a problem of legibility.

Typographers are concerned with legibility insofar as it is their job to select the correct font to use. Brush Script is an example of a font containing many characters that might be difficult to distinguish. The selection of cases influences the legibility of typography because using only uppercase letters (all-caps) reduces legibility.

```python
rx.scroll_area(
    rx.flex(
        rx.text("""
Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense “legible” and “readable” are often used synonymously, typographically they are separate but related concepts."""
        ),
        rx.text("""
Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as “the quality of being decipherable and recognisable”. For instance, if a “b” and an “h”, or a “3” and an “8”, are difficult to distinguish at small sizes, this is a problem of legibility."""
        ),
        rx.text("""
Typographers are concerned with legibility insofar as it is their job to select the correct font to use. Brush Script is an example of a font containing many characters that might be difficult to distinguish. The selection of cases influences the legibility of typography because using only uppercase letters (all-caps) reduces legibility."""
        ),
        direction="column",
        spacing="4"
    ),
    type="always",
    scrollbars="vertical",
    style={"height": 180}
)
```

# Control the scrollable axes

Use the `scrollbars` prop to limit scrollable axes. This prop can take values `"vertical" | "horizontal" | "both"`.

Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense "legible" and "readable" are often used synonymously, typographically they are separate but related concepts.

Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as "the quality of being decipherable and recognisable". For instance, if a "b" and an "h", or a "3" and an "8", are difficult to distinguish at small sizes, this is a problem of legibility.

Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense "legible" and "readable" are often used synonymously, typographically they are separate but related concepts.

Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as "the quality of being decipherable and recognisable". For instance, if a "b" and an "h", or a "3" and an "8", are difficult to distinguish at small sizes, this is a problem of legibility.

Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense "legible" and "readable" are often used synonymously, typographically they are separate but related concepts.

Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as "the quality of being decipherable and recognisable". For instance, if a "b" and an "h", or a "3" and an "8", are difficult to distinguish at small sizes, this is a problem of legibility.

Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense "legible" and "readable" are often used synonymously, typographically they are separate but related concepts.

Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as "the quality of being decipherable and recognisable". For instance, if a "b" and an "h", or a "3" and an "8", are difficult to distinguish at small sizes, this is a problem of legibility.

```python
rx.grid(
    rx.scroll_area(
        rx.flex(
            rx.text(
                """Three fundamental aspects of typography are legibility, readability, and
aesthetics. Although in a non-technical sense "legible" and "readable"
are often used synonymously, typographically they are separate but
related concepts."""
            ),
            size="2",
            trim="both",
            padding="8px",
            padding_right="48px",
            direction="column",
            spacing="4",
        ),
        rx.scroll_area(
            rx.flex(
                rx.text(
                    """Three fundamental aspects of typography are legibility, readability, and
aesthetics. Although in a non-technical sense "legible" and "readable"
are often used synonymously, typographically they are separate but
related concepts."""
                ),
                size="2",
                trim="both",
                padding="8px",
                spacing="4",
            ),
            type="always",
            scrollbars="vertical",
            style={"height": 150},
        ),
        rx.scroll_area(
            rx.flex(
                rx.text(
                    """Three fundamental aspects of typography are legibility, readability, and
aesthetics. Although in a non-technical sense "legible" and "readable"
are often used synonymously, typographically they are separate but
related concepts."""
                ),
                size="2",
                trim="both",
                padding="8px",
                spacing="4",
                style={"width": 700},
            ),
            type="always",
            scrollbars="horizontal",
            style={"height": 150},
        ),
        rx.scroll_area(
            rx.flex(
                rx.text(
                    """Three fundamental aspects of typography are legibility, readability, and
aesthetics. Although in a non-technical sense "legible" and "readable"
are often used synonymously, typographically they are separate but
related concepts."""
                ),
                size="2",
                trim="both",
                padding="8px",
                spacing="4",
                style={"width": 400},
            ),
            type="always",
            scrollbars="both",
            style={"height": 150},
        ),
        columns="3",
        spacing="2",
    )
)
```

[Copy Code](#)

# Setting the type of the Scrollbars

The `type` prop describes the nature of scrollbar visibility.

- **auto** means that scrollbars are visible when content is overflowing on the corresponding orientation.
- **always** means that scrollbars are always visible regardless of whether the content is overflowing.
- **scroll** means that scrollbars are visible when the user is scrolling along its corresponding orientation.
- **hover** means that scrollbars are visible when the user is scrolling along its corresponding orientation and when the user is hovering over the scroll area.

```python
rx.grid(
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'auto'", weight="bold"),
            rx.text("""
                Legibility describes how easily individual characters can be
                distinguished from one another. It is described by Walter Tracy as "the
                quality of being decipherable and recognisable". For instance, if a "b"
                and an "h", or a "3" and an "8", are difficult to distinguish at small
                sizes, this is a problem of legibility.
            """, size="2", trim="both"),
            padding="8px",
            direction="column",
            spacing="4",
        ),
        type="auto",
        scrollbars="vertical",
        style={"height": "150"},
    ),
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'always'", weight="bold"),
            rx.text("""
                Legibility describes how easily individual characters can be
                distinguished from one another. It is described by Walter Tracy as "the
                quality of being decipherable and recognisable". For instance, if a "b"
                and an "h", or a "3" and an "8", are difficult to distinguish at small
                sizes, this is a problem of legibility.
            """, size="2", trim="both"),
            padding="8px",
            direction="column",
            spacing="4",
        ),
        type="always",
        scrollbars="vertical",
        style={"height": "150"},
    ),
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'scroll'", weight="bold"),
            rx.text("""
                Legibility describes how easily individual characters can be
                distinguished from one another. It is described by Walter Tracy as "the
                quality of being decipherable and recognisable". For instance, if a "b"
                and an "h", or a "3" and an "8", are difficult to distinguish at small
                sizes, this is a problem of legibility.
            """, size="2", trim="both"),
            padding="8px",
            direction="column",
            spacing="4",
        ),
        type="scroll",
        scrollbars="vertical",
        style={"height": "150"},
    ),
    rx.scroll_area(
        rx.flex(
            rx.text("type = 'hover'", weight="bold"),
            rx.text("""
                Legibility describes how easily individual characters can be
                distinguished from one another. It is described by Walter Tracy as "the
                quality of being decipherable and recognisable". For instance, if a "b"
                and an "h", or a "3" and an "8", are difficult to distinguish at small
                sizes, this is a problem of legibility.
            """, size="2", trim="both"),
            padding="8px",
            direction="column",
            spacing="4",
        ),
        type="hover",
        scrollbars="vertical",
        style={"height": "150"},
    ),
    columns="4",
    spacing="2",
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/scroll-area/#rx.scroll_area)

# rx.scroll_area

Custom styled, cross-browser scrollable area using native functionality.

## Three fundamental aspects of typography are legibility, readability, and aesthetics. Although in a non-technical sense "legible" and "readable"are often used synonymously, typographically they are separate but related concepts.

Legibility describes how easily individual characters can be distinguished from one another. It is described by Walter Tracy as "the quality of being decipherable and recognisable". For instance, if a "b" and an "h", or a "3" and an "8", are difficult to distinguish at small sizes, this is a problem of legibility.

### Properties

- **scrollbars**: `"vertical" | "horizontal" | ...`
- **type**: `"auto" | "always" | ...`
- **scroll_hide_delay**: `int`

The default values for these properties are not specified in the given HTML.

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)