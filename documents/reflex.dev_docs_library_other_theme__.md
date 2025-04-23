# Theme

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in the `rx.App`.

```python
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
```

For more information, see [Theme Panel](https://reflex.dev/docs/library/other/theme/#theme-panel).

# Theme Panel

The `ThemePanel` component is a container for the `Theme` component. It provides a way to change the theme of the application.

```python
rx.theme_panel()
```

The theme panel is closed by default. You can set it open with `default_open=True`.

```python
rx.theme_panel(default_open=True)
```

# API Reference

[![Link](https://reflex.dev/docs/library/other/theme/#rx.theme)](https://reflex.dev/docs/library/other/theme/#rx.theme)

# rx.theme
A theme provider for radix components.

This should be applied as `App.theme` to apply the theme to all radix components in the app with the given settings.
It can also be used in a normal page to apply specified properties to all child elements as an override of the main theme.

- **has_background** - bool
- **appearance** - "inherit" | "light" | ...
- **accent_color** - "tomato" | "red" | ... or palette
- **gray_color** - "gray" | "mauve" | ...
- **panel_background** - "solid" | "translucent"
- **radius** - "none" | "small" | ...
- **scaling** - "90%" | "95%" | ...

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.theme_panel

Visual editor for creating and editing themes.

Include as a child component of Theme to use in your app.
```
Include as a child component of Theme to use in your app.
```


## Props

| Prop        | Type | Values | Default |
|-------------|------|--------|---------|
| default_open | bool | - | - |

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)