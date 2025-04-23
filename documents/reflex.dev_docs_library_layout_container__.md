# Container

Constrains the maximum width of page content, while keeping flexible margins for responsive layouts.

A Container is generally used to wrap the main content for a page.

[Basic Example](https://reflex.dev/docs/library/layout/container/#basic-example)

# Basic Example

This content is constrained to a max width of 448px.
This content is constrained to a max width of 688px.
This content is constrained to a max width of 880px.
This content is constrained to a max width of 1136px.

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
    rx.container(
        rx.card(
            "This content is constrained to a max width of 1136px.",
            width="100%",
        ),
        size="4",
    ),
    background_color="var(--gray-3)",
    width="100%",
)
```
![Copy Code](https://reflex.dev/docs/library/layout/container/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/container/#rx.container)

# rx.container

Constrains the maximum width of page content.

See https://www.radix-ui.com/themes/docs/components/container

```python
See https://www.radix-ui.com/themes/docs/components/container
```

---

Test

| Prop | Type | Default | Interactive |
|------|------|---------|------------|
| size | "1" | LiteralVar.create("3") | 1 |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)