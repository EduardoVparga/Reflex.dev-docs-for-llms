# Separator

Visually or semantically separates content.

[Basic Example](https://reflex.dev/docs/library/layout/separator/#basic-example)

# Basic Example

![](https://reflex.dev/assets/icons/link.svg)

<div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-ai-center rt-r-gap-4">
        <div class="rt-BaseCard rt-Card">Section 1</div>
        <span class="rt-Separator rt-r-orientation-horizontal rt-r-size-4" data-accent-color="gray"></span>
        <div class="rt-BaseCard rt-Card">Section 2</div>
    </div>
</div>

```python
rx.flex(
    rx.card("Section 1"),
    rx.divider(),
    rx.card("Section 2"),
    spacing="4",
    direction="column",
    align="center",
)
```

[Learn more about the separator size](https://reflex.dev/docs/library/layout/separator/#size)

# Size

The `size` prop controls how long the separator is. Using `size="4"` will make the separator fill the parent container. Setting CSS `width` or `height` prop to `"100%"` can also achieve this effect, but `size` works the same regardless of the orientation.

## Example

Section 1
---

Section 2

```python
rx.flex(
    rx.card("Section 1"),
    rx.divider(size="4"),
    rx.card("Section 2"),
    spacing="4",
    direction="column",
)
```

For more information, see [Separator Orientation](https://reflex.dev/docs/library/layout/separator/#orientation)

# Orientation

Setting the orientation prop to `vertical` will make the separator appear vertically.

<div>
    <div>Section 1</div>
    <span class="Separator orientation-vertical size-4"></span>
    <div>Section 2</div>
</div>

```python
rx.flex(
    rx.card("Section 1"),
    rx.divider(orientation="vertical", size="4"),
    rx.card("Section 2"),
    spacing="4",
    width="100%",
    height="10vh",
)
```

For more information, see the [API reference](https://reflex.dev/docs/library/layout/separator/#api-reference).

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/separator/#rx.separator)

# rx.separator

Visually or semantically separates content.

## Props

| Prop       | Type | Values          | Default | Interactive |
|------------|------|-----------------|---------|-------------|
| size       | "1" | "2" | ...        | LiteralVar.create("4")  | - |
| color_scheme | "tomato" | "red" | ...    | - | <button aria-autocomplete="none" aria-controls="radix-:R23ooqe6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface w-32 font-small text-slate-11" data-state="closed" dir="ltr" role="combobox" type="button"><span class="rt-SelectTriggerInner"><span style="pointer-events:none">tomato</span></span><svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9" xmlns="http://www.w3.org/2000/svg"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg></button> |
| orientation | "horizontal" | "vertical"    | - | <button aria-autocomplete="none" aria-controls="radix-:R27ooqe6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface w-32 font-small text-slate-11" data-state="closed" dir="ltr" role="combobox" type="button"><span class="rt-SelectTriggerInner"><span style="pointer-events:none">horizontal</span></span><svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9" xmlns="http://www.w3.org/2000/svg"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg></button> |
| decorative | bool        | false          | - | <label class="rt-Text rt-r-size-2"><div class="rt-Flex rt-r-gap-2"><button aria-checked="false" class="rt-reset rt-BaseCheckboxRoot rt-CheckboxRoot rt-r-size-2 rt-variant-surface" data-state="unchecked" role="checkbox" type="button" value="on"></button>false</div></label> |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)