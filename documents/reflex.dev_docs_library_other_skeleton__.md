# Skeleton (loading placeholder)
Skeleton is a loading placeholder component that serves as a visual placeholder while content is loading. It is useful for maintaining the layout's structure and providing users with a sense of progression while awaiting the final content.

## Example

- **Button Small**:
  - Skeleton: A small button placeholder.
  - Text: Text is loaded.

- **Button Big**:
  - Skeleton: A big button placeholder.
  - Text: Text is already loaded.

```python
rx.vstack(
    rx.skeleton(rx.button("button-small"), height="10px"),
    rx.skeleton(rx.button("button-big"), height="20px"),
    rx.skeleton(rx.text("Text is loaded."), loading=True),
    rx.skeleton(rx.text("Text is already loaded."), loading=False),
)
```

When using `Skeleton` with text, wrap the text itself instead of the parent element to have a placeholder of the same size.

Use the loading prop to control whether the skeleton or its children are displayed. Skeleton preserves the dimensions of children when they are hidden and disables interactive elements.

# API Reference

[API Reference](https://reflex.dev/docs/library/other/skeleton/#rx.skeleton)

# rx.skeleton

Skeleton component.

## Test

```python
Test
```

Prop | Type | Default | Interactive
--- | --- | --- | ---
width | str |  | 
min_width | str |  | 
max_width | str |  | 
height | str |  | 
min_height | str |  | 
max_height | str |  | 
loading | bool |  | [false](#)

-

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)