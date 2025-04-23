# Callout

A `callout` is a short message to attract user's attention.

You will need admin privileges to install and access this application.
You will need admin privileges to install and access this application.

```python
rx.callout(
    "You will need admin privileges to install and access this application.",
    icon="info",
)
```

The `icon` prop allows an icon to be passed to the `callout` component. See the [icon](/docs/library/data-display/icon/) component for all icons that are available.

# As alert

Access denied. Please contact the network administrator to view this page.

```python
rx.callout(
    "Access denied. Please contact the network administrator to view this page.",
    icon="triangle_alert",
    color_scheme="red",
    role="alert",
)
```

Learn more about styling [here](https://reflex.dev/docs/library/data-display/callout/#style)

# Style

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/data-display/callout/#size"></a>

# Size

Use the `size` prop to control the size.

## Callouts

You will need admin privileges to install and access this application.
You will need admin privileges to install and access this application.
You will need admin privileges to install and access this application.

```python
rx.flex(
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        size="3",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        size="2",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        size="1",
    ),
    direction="column",
    spacing="3",
    align="start",
)
```

# Variant

Use the `variant` prop to control the visual style. It is set to `soft` by default.

You will need admin privileges to install and access this application.
- Soft variant
- Surface variant
- Outline variant

```python
rx.flex(
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        variant="soft",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        variant="surface",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        variant="outline",
    ),
    direction="column",
    spacing="3",
)
```

# Color

Use the `color_scheme` prop to assign a specific color, ignoring the global theme.

## Callouts

You will need admin privileges to install and access this application.
- **Blue**
- **Green**
- **Red**

```python
rx.flex(
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        color_scheme="blue",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        color_scheme="green",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        color_scheme="red",
    ),
    direction="column",
    spacing="3",
)
```

# High Contrast

Use the `high_contrast` prop to add additional contrast.

You will need admin privileges to install and access this application.
You will need admin privileges to install and access this application.

rx.flex(
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        high_contrast=True,
    ),
    direction="column",
    spacing="3",
)

rx.flex(
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
    ),
    rx.callout(
        "You will need admin privileges to install and access this application.",
        icon="info",
        high_contrast=True,
    ),
    direction="column",
    spacing="3",
)

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/callout/#rx.callout)

# rx.callout

A short message to attract user's attention.

## Basic Callout

<div>
  <svg class="lucide lucide-search" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    <circle cx="11" cy="11" r="8"></circle>
    <path d="m21 21-4.3-4.3"></path>
  </svg>
  <p>Basic Callout</p>
</div>

### Properties

| Prop          | Type | Default | Interactive |
|---------------|------|---------|------------|
| `text`        | str  |         |            |
| `icon`        | str  |         |            |
| `as_child`    | bool |         |            |
| `size`        | "1" | "2" ... | <select><option value="1">1</option></select> |
| `variant`     | "soft" | "surface" | <select><option value="soft">soft</option></select> |
| `color_scheme` | "tomato" | "red" ... | <button>tomato</button> |
| `high_contrast` | bool  |         | <label><input type="checkbox"> false</label> |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.callout.root

Groups Icon and Text parts of a Callout.

## Callout Example
<div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
  <div class="rt-CalloutRoot rt-r-size-1 rt-variant-soft" data-accent-color="tomato">
    <div class="rt-CalloutIcon">
      <svg class="lucide lucide-info" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24">
        <circle cx="12" cy="12" r="10"></circle>
        <path d="M12 16v-4"></path>
        <path d="M12 8h.01"></path>
      </svg>
    </div>
    <p class="rt-Text rt-r-size-2 rt-CalloutText">You will need admin privileges to install and access this application.</p>
  </div>
</div>

## Properties

| Prop          | Type | Values                  | Default | Interactive |
|---------------|------|-------------------------|---------|------------|
| as_child      | bool |                         |         |            |
| size          | str  | "1" | "2" | ...       |           | Dropdown   |
| variant       | str  | "soft" | "surface" | ...     | soft      | Dropdown   |
| color_scheme  | str  | "tomato" | "red" | ...       | tomato    | Button     |
| high_contrast | bool |                         |         |            |

- `as_child`: 
  - **Type**: bool
- `size`: 
  - **Type**: str, Values: `"1"` | `"2"` | ...
- `variant`: 
  - **Type**: str, Values: `"soft"` | `"surface"` | ...
  - Default value: `soft`
- `color_scheme`: 
  - **Type**: str, Values: `"tomato"` | `"red"` | ...
  - Default value: `tomato`
- `high_contrast`: 
  - **Type**: bool

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.callout.icon

Provides width and height for the icon associated with the callout.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.callout.text

Renders the callout text. This component is based on the p element.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div>
<p></p>
</div>

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)