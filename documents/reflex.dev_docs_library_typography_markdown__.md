# Markdown

The `rx.markdown` component can be used to render markdown text. It is based on [Github Flavored Markdown](https://github.github.com/gfm/).

<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
<div>
</div>

# Hello World!

# Hello World!

# Hello World!
## Hello World!
### Hello World!

Support us on [Github](https://github.com/reflex-dev/reflex).

Use `reflex deploy` to deploy your app with **a single command**.

# Math Equations

You can render math equations using LaTeX.
For inline equations, surround the equation with `$`:

Pythagorean theorem: \(a^2 + b^2 = c^2\).

```python
rx.markdown("Pythagorean theorem: $a^2 + b^2 = c^2$.")
```

For more information on syntax highlighting, see [Reflex.dev](https://reflex.dev/docs/library/typography/markdown/#syntax-highlighting) documentation.

# Syntax Highlighting

You can render code blocks with syntax highlighting using the ```{language} syntax:

```python
import reflex as rx
from .pages import index

app = rx.App()
app.add_page(index)
```

rx.markdown(
    r"""`
``python
import reflex as rx
from .pages import index

app = rx.App()
app.add_page(index)
``
"""
)

# Tables

You can render tables using the `|` syntax:

```
Syntax      | Description 
----------- | -----------
Header      | Title       
Paragraph   | Text        
```

```python
rx.markdown("""
    | Syntax      | Description |
    | ----------- | ----------- |
    | Header      | Title       |
    | Paragraph   | Text        |
""")
```

# Component Map

You can specify which components to use for rendering markdown elements using the `component_map` prop.

Each key in the `component_map` prop is a markdown element, and the value is a function that takes the text of the element as input and returns a Reflex component.

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed"></div>
</div>

# The `codeblock` and `a` tags are special cases. In addition to the `text`, they also receive a `props` argument containing additional props for the component.

<svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24">
<path d="m6 9 6 6 6-6"></path>
</svg>

# Hello World!

# This is a Subheader

# Hello World!

## This is a Subheader

### And Another Subheader

Here is some `code`:

```python
import reflex as rx

component = rx.text("Hello World!")
```

And then some more text here, followed by a link to [Reflex](https://reflex.dev/).

# API Reference

[API Reference](https://reflex.dev/docs/library/typography/markdown/#rx.markdown)

# rx.markdown

A markdown component.

## Properties

- **Prop**: `component_map`
  - **Type | Values**: `Dict[str, Any]`
  - **Default**: `{}`

- **Prop**: `component_map_hash`
  - **Type | Values**: `str`
  - **Default**: `""`

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)