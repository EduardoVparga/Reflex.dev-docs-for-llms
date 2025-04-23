# Theming

As of Reflex v0.4.0, you can now theme your Reflex applications. The core of our theming system is directly based on the [Radix Themes](https://www.radix-ui.com) library. This allows you to easily change the theme of your application along with providing a default light and dark theme. Themes cause all the components to have a unified color appearance.

[Overview](https://reflex.dev/docs/styling/theming/#overview)

# Overview

The `Theme` component is used to change the theme of the application. The `Theme` can be set directly in your rx.App.

```python
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
```

Here are the props that can be passed to the `rx.theme` component:

- **has_background**
  - Type: Bool
  - Description: Whether to apply the themes background color to the theme node. Defaults to True.

- **appearance**
  - Type: "inherit" | "light" | "dark"
  - Description: The appearance of the theme. Can be 'light' or 'dark'. Defaults to 'light'.

- **accent_color**
  - Type: Str
  - Description: The primary color used for default buttons, typography, backgrounds, etc.

- **gray_color**
  - Type: Str
  - Description: The secondary color used for default buttons, typography, backgrounds, etc.

- **panel_background**
  - Type: "solid" | "translucent"
  - Description: Whether panel backgrounds are translucent: "solid" | "translucent" (default).

- **radius**
  - Type: "none" | "small" | "medium" | "large" | "full"
  - Description: The radius of the theme. Can be 'small', 'medium', or 'large'. Defaults to 'medium'.

- **scaling**
  - Type: "90%" | "95%" | "100%" | "105%" | "110%"
  - Description: Scale of all theme items.

Additionally you can modify the theme of your app through using the `Theme Panel` component which can be found in the [Theme Panel docs](/docs/library/other/theme/).

# Colors

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/styling/theming/#color-scheme">

# Color Scheme

On a high-level, component `color_scheme` inherits from the color specified in the theme. This means that if you change the theme, the color of the component will also change. Available colors can be found [here](https://www.radix-ui.com/colors).

You can also specify the `color_scheme` prop.

## Example

```python
rx.flex(
    rx.button(
        "Hello World",
        color_scheme="tomato",
    ),
    rx.button(
        "Hello World",
        color_scheme="teal",
    ),
    spacing="2",
)
```

For more details, check out [Styling and Theming](https://reflex.dev/docs/styling/theming/#shades).

# Shades

Sometime you may want to use a specific shade of a color from the theme. This is recommended vs using a hex color directly as it will automatically change when the theme changes appearance change from light/dark.

To access a specific shade of color from the theme, you can use the `rx.color`. When switching to light and dark themes, the color will automatically change. Shades can be accessed by using the color name and the shade number. The shade number ranges from 1 to 12. Additionally, they can have their alpha value set by using the `True` parameter it defaults to `False`. A full list of colors can be found [here](https://www.radix-ui.com/colors).

## Example

```python
rx.flex(
    rx.button(
        "Hello World",
        color=rx.color("grass", 1),
        background_color=rx.color("grass", 7),
        border_color=f"1px solid {rx.color('grass', 1)}",
    ),
    spacing="2",
)
```

## Table of Color Properties

- **Name**: `color`
- **Type**: `Str`
- **Description**: The color to use. Can be any valid accent color or 'accent' to reference the current theme color.

- **Name**: `shade`
- **Type**: 
  - [1 - 12](https://www.radix-ui.com/colors)
- **Description**: The shade of the color to use. Defaults to 7.

- **Name**: `alpha`
- **Type**: `Bool`
- **Description**: Whether to use the alpha value of the color. Defaults to False.

# Regular Colors

You can also use standard hex, rgb, and rgba colors.

Hello World

```python
rx.flex(
    rx.button(
        "Hello World",
        color="white",
        background_color="#87CEFA",
        border="1px solid rgb(176,196,222)",
    ),
    spacing="2",
)
```

[Toggle Appearance](https://reflex.dev/docs/styling/theming/#toggle-appearance)

# Toggle Appearance

To toggle between the light and dark mode manually, you can use the `toggle_color_mode` with the desired event trigger of your choice.

```python
from reflex.style import toggle_color_mode

def index():
    return rx.button(
        "Toggle Color Mode",
        on_click=toggle_color_mode,
    )
```

[View Code](https://reflex.dev/docs/styling/theming/#appearance-conditional-rendering)

# Appearance Conditional Rendering

To render a different component depending on whether the app is in `light` mode or `dark` mode, you can use the `rx.color_mode_cond` component. The first component will be rendered if the app is in `light` mode and the second component will be rendered if the app is in `dark` mode.

![](https://logos/dark/reflex.svg)

```python
rx.color_mode_cond(
    light=rx.image(
        src="/logos/light/reflex.svg",
        alt="Reflex Logo light",
        height="4em",
    ),
    dark=rx.image(
        src="/logos/dark/reflex.svg",
        alt="Reflex Logo dark",
        height="4em",
    ),
)
```

This can also be applied to props.

## Hello World Button

```python
rx.button(
    "Hello World",
    color=rx.color_mode_cond(light="black", dark="white"),
    background_color=rx.color_mode_cond(light="white", dark="black"),
)
```