# Data List

The `DataList` component displays key-value pairs and is particularly helpful for showing metadata.

A `DataList` needs to be initialized using `rx.data_list.root()` and currently takes in data list items: `rx.data_list.item`

- **Status**: Authorized
- **ID**: U-474747
- **Name**: Developer Success
- **Email**: [success@reflex.dev](mailto:success@reflex.dev)
- **Company**: [Reflex](https://reflex.dev)

```python
rx.card(
    rx.data_list.root(
        rx.data_list.item(
            rx.data_list.label("Status"),
            rx.data_list.value(rx.badge("Authorized", variant="soft", radius="full")),
            align="center",
        ),
        rx.data_list.item(
            rx.data_list.label("ID"),
            rx.data_list.value(rx.code("U-474747")),
        ),
        rx.data_list.item(
            rx.data_list.label("Name"),
            rx.data_list.value("Developer Success", align="center"),
        ),
        rx.data_list.item(
            rx.data_list.label("Email"),
            rx.data_list.value(rx.link("success@reflex.dev", href="mailto:success@reflex.dev")),
        ),
        rx.data_list.item(
            rx.data_list.label("Company"),
            rx.data_list.value(rx.link("Reflex", href="https://reflex.dev")),
        ),
    )
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/data-list/#rx.data_list.root)

# rx.data_list.root
Root element for a DataList component.

## Status
- **Status**: Authorized

## ID
- **ID**: U-474747

## Name
- **Name**: Developer Success

## Email
- **Email**: foo@reflex.dev

### Properties
- **orientation**
  - Type | Values: `"horizontal" | "vertical"`
  - Default: `not specified`
  - Interactive: No

- **size**
  - Type | Values: `"1" | "2" | ...`
  - Default: `1`
  - Interactive: Yes

- **trim**
  - Type | Values: `"normal" | "start" | ...`
  - Default: `normal`
  - Interactive: Yes

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.data_list.item

An item in the DataList component.

## Status
Authorized

## ID
U-474747

## Name
Developer Success

## Email
foo@reflex.dev

### Properties

| Prop         | Type | Default | Interactive |
|--------------|------|---------|------------|
| align        | "start" | center | ... |   | - |
|              |       |        |            | <code>align</code> [![Info](./lucide-info.svg)](./lucide-info.svg)  | - |
|              |      |        |            | - [![Ellipsis](./lucide-circle-ellipsis.svg)](./lucide-circle-ellipsis.svg) [![Info](./lucide-info.svg)](./lucide-info.svg)  | - |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.data_list.label
A label in the DataList component.

## Status: Authorized

ID: U-474747

Name: Developer Success

Email: foo@reflex.dev

### Properties:
- **Prop**: `width`
  - Type | Values: str
  - Default: -
  - Interactive: -

- **Prop**: `min_width`
  - Type | Values: str
  - Default: -
  - Interactive: -

- **Prop**: `max_width`
  - Type | Values: str
  - Default: -
  - Interactive: -

- **Prop**: `color_scheme`
  - Type | Values: "tomato" | "red" | ...
  - Default: -
  - Interactive: [tomato]

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.data_list.value  
A value in the DataList component.  

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

# Props

No component specific props

#

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)