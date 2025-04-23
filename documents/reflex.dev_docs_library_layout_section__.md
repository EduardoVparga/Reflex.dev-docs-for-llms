# Section

Denotes a section of page content, providing vertical padding by default.

Primarily this is a semantic component that is used to group related textual content.

[View Basic Example](https://reflex.dev/docs/library/layout/section/#basic-example)

# Basic Example

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="rt-Box css-8atqhb">
<section class="rt-Section rt-r-size-2 css-18oef6h">

# First
This is the first content section

## Second
This is another section

# Second

This is the second content section

```python
rx.box(
    rx.section(
        rx.heading("First"),
        rx.text("This is the first content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    rx.section(
        rx.heading("Second"),
        rx.text("This is the second content section"),
        padding_left="12px",
        padding_right="12px",
        background_color="var(--gray-2)",
    ),
    width="100%",
)
```
[Link to API Reference](https://reflex.dev/docs/library/layout/section/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/section/#rx.section)

# rx.section

Denotes a section of page content.

## Test

Prop | Type | Default | Interactive
--- | --- | --- | ---
size | "1" | "2" | ... | LiteralVar.create("2")
|  |  |  | 

- Value: 1
- Value: 2

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)