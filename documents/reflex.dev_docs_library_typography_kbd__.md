# rx.text.kbd (Keyboard)
Represents keyboard input or a hotkey.

```python
rx.text.kbd("Shift + Tab")
```

- `Shift + Tab`

# Size

Use the `size` prop to control text size. This prop also provides correct line height and corrective letter spacing—as text size increases, the relative line height and letter spacing decrease.

Shift + Tab  
Shift + Tab  
Shift + Tab  
Shift + Tab  
Shift + Tab  
Shift + Tab  
Shift + Tab  
Shift + Tab  

```python
rx.flex(
    rx.text.kbd("Shift + Tab", size="1"),
    rx.text.kbd("Shift + Tab", size="2"),
    rx.text.kbd("Shift + Tab", size="3"),
    rx.text.kbd("Shift + Tab", size="4"),
    rx.text.kbd("Shift + Tab", size="5"),
    rx.text.kbd("Shift + Tab", size="6"),
    rx.text.kbd("Shift + Tab", size="7"),
    rx.text.kbd("Shift + Tab", size="8"),
    rx.text.kbd("Shift + Tab", size="9"),
    direction="column",
    spacing="3",
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/typography/kbd/#rx.text.kbd)

# rx.text.kbd

Represents keyboard input or a hotkey.

## Example

```markdown
**Test**
```

### Properties

- **Prop**: `size`
  - **Type | Values**: `"1" | "2" | ...`
  - **Default**: None
  - **Interactive**: Yes

  ```markdown
  **1**
  ```

- **Prop**: `size`
  - **Type | Values**: `"1" | "2" | ...`
  - **Default**: None
  - **Interactive**: Yes

  ```markdown
  **1**
  ```

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)