# Code

```python
console.log()
```

rx.code("console.log()")

![](https://reflex.dev/docs/library/typography/code/#size)

# Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

```python
rx.flex(
    rx.code("console.log()", size="1"),
    rx.code("console.log()", size="2"),
    rx.code("console.log()", size="3"),
    rx.code("console.log()", size="4"),
    rx.code("console.log()", size="5"),
    rx.code("console.log()", size="6"),
    rx.code("console.log()", size="7"),
    rx.code("console.log()", size="8"),
    rx.code("console.log()", size="9"),
    direction="column",
    spacing="3",
    align="start",
)
```

For more information, see [Code Weight](https://reflex.dev/docs/library/typography/code/#weight) in the Reflex documentation.

# Weight

Use the `weight` prop to set the text weight.

```python
console.log()
console.log()
console.log()
console.log()
```

```python
rx.flex(
    rx.code("console.log()", weight="light"),
    rx.code("console.log()", weight="regular"),
    rx.code("console.log()", weight="medium"),
    rx.code("console.log()", weight="bold"),
    direction="column",
    spacing="3",
)
```

# Variant

Use the `variant` prop to control the visual style.

```python
console.log()
console.log()
console.log()
console.log()
```

```python
rx.flex(
    rx.code("console.log()", variant="solid"),
    rx.code("console.log()", variant="soft"),
    rx.code("console.log()", variant="outline"),
    rx.code("console.log()", variant="ghost"),
    direction="column",
    spacing="2",
    align="start",
)
```

# Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

```python
console.log()
console.log()
console.log()
console.log()
```

```python
rx.flex(
    rx.code("console.log()", color_scheme="indigo"),
    rx.code("console.log()", color_scheme="crimson"),
    rx.code("console.log()", color_scheme="orange"),
    rx.code("console.log()", color_scheme="cyan"),
    direction="column",
    spacing="2",
    align="start",
)
```

# High Contrast

Use the `high_contrast` prop to increase color contrast with the background.

```python
console.log()
console.log()
console.log()
console.log()
```

```python
console.log(), variant="solid", high_contrast=True
console.log(), variant="soft", high_contrast=True
console.log(), variant="outline", high_contrast=True
console.log(), variant="ghost", high_contrast=True
```

# API Reference

For more information, see the [API reference](https://reflex.dev/docs/library/typography/code/#api-reference).

# API Reference

[![Link](https://reflex.dev/docs/library/typography/code/#rx.code)](https://reflex.dev/docs/library/typography/code/#rx.code)

# rx.code

A block level extended quotation.

## Code Example
```python
Test
```

### Props Table
| Prop            | Type | Default | Interactive |
|-----------------|------|---------|------------|
| variant         | `"classic" | "solid"`... | -          | <button>classic</button> |
| size            | `"1" | "2"`... | -        | <button>1</button>       |
| weight          | `"light" | "regular"`... | -     | <button>light</button>    |
| color_scheme    | `"tomato" | "red"`... | -         | [tomato](#)               |
| high_contrast   | `bool` | -       | <label><button>false</button></label> |

---

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)