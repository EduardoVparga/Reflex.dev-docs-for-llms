# HTML Embed
The HTML component can be used to render raw HTML code.
Before you reach for this component, consider using Reflex's raw HTML element support instead.

<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
<div class="rx-Html">

# Hello World

# Hello World

# Hello World

## Hello World

### Hello World

#### Hello World

##### Hello World

```python
rx.vstack(
    rx.html("&lt;h1&gt;Hello World&lt;/h1&gt;"),
    rx.html("&lt;h2&gt;Hello World&lt;/h2&gt;"),
    rx.html("&lt;h3&gt;Hello World&lt;/h3&gt;"),
    rx.html("&lt;h4&gt;Hello World&lt;/h4&gt;"),
    rx.html("&lt;h5&gt;Hello World&lt;/h5&gt;"),
    rx.html("&lt;h6&gt;Hello World&lt;/h6&gt;")
)
```

In this example, we render an image.

```
rx.html(
    "<img src='https://reflex.dev/reflex_banner.png' />"
)
```

[![](https://reflex.dev/reflex_banner.png)](https://reflex.dev/reflex_banner.png)

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/other/html-embed/#api-reference">Link</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/other/html-embed/#rx.html)

# rx.html

Render the html.

```python
Returns:
    The code to render the html component.
```

## Props

| Prop                  | Type | Default |
|-----------------------|------|---------|
| dangerouslySetInnerHTML | Dict[str, str] | - |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)