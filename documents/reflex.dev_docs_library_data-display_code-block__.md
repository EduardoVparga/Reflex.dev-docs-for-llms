# Code Block

The Code Block component can be used to display code easily within a website.
Put in a multiline string with the correct spacing and specify and language to show the desired code.

```python
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))
```

```shiki
rx.code_block(
    """def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))""",
    language="python",
    show_line_numbers=True,
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/code-block/#rx.code_block)

# rx.code_block

A code block.

## Properties

- **Prop**: `theme`
  - **Type | Values**: `Union[Theme, str]`
  - **Default**: `Theme.one_light`

- **Prop**: `language`
  - **Type | Values**: `"abap" | "abnf" | ...`
  - **Default**: `Var.create("python")`

- **Prop**: `code`
  - **Type | Values**: `str`
  - **Default**: None

- **Prop**: `show_line_numbers`
  - **Type | Values**: `bool`
  - **Default**: None

- **Prop**: `starting_line_number`
  - **Type | Values**: `int`
  - **Default**: None

- **Prop**: `wrap_long_lines`
  - **Type | Values**: `bool`
  - **Default**: None

- **Prop**: `custom_style`
  - **Type | Values**: `Dict[str, str | reflex.vars.base.Var | reflex.constants.colors.Color]`
  - **Default**: `{}`

- **Prop**: `code_tag_props`
  - **Type | Values**: `Dict[str, str]`
  - **Default**: None

- **Prop**: `can_copy`
  - **Type | Values**: `bool`
  - **Default**: `False`

- **Prop**: `copy_button`
  - **Type | Values**: `Union[bool, Component, NoneType]`
  - **Default**: `None`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)