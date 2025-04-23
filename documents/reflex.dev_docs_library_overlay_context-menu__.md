# Context Menu  
A Context Menu is a popup menu that appears upon user interaction, such as a right-click or a hover.

[Learn more](https://reflex.dev/docs/library/overlay/context-menu/#basic-usage)

# Basic Usage

A Context Menu is composed of a `context_menu.root`, a `context_menu.trigger` and a `context_menu.content`. The `context_menu_root` contains all the parts of a context menu. The `context_menu.trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the context menu. The `context_menu.content` is the component that pops out when the context menu is open.

The `context_menu.item` contains the actual context menu items and sits under the `context_menu.content`.

The `context_menu.sub` contains all the parts of a submenu. There is a `context_menu.sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `context_menu.sub` component. The `context_menu.sub_content` is the component that pops out when a submenu is open. It must also be rendered inside a `context_menu.sub` component.

The `context_menu.separator` is used to visually separate items in a context menu.

```python
rx.context_menu.root(
    rx.context_menu.trigger(rx.button("Right click me")),
    rx.context_menu.content(
        rx.context_menu.item("Edit", shortcut="⌘ E"),
        rx.context_menu.item("Duplicate", shortcut="⌘ D"),
        rx.context_menu.separator(),
        rx.context_menu.item("Archive", shortcut="⌘ N"),
        rx.context_menu.sub(
            rx.context_menu.sub_trigger("More"),
            rx.context_menu.sub_content(
                rx.context_menu.item("Move to project…"),
                rx.context_menu.item("Move to folder…"),
                rx.context_menu.separator(),
                rx.context_menu.item("Advanced options…")
            )
        ),
        rx.context_menu.separator(),
        rx.context_menu.item("Share"),
        rx.context_menu.item("Add to favorites"),
        rx.context_menu.separator(),
        rx.context_menu.item(
            "Delete",
            shortcut="⌘ ⌫",
            color="red"
        ),
    ),
)
```

## Opening a Dialog from Context Menu using State

Accessing an overlay component from within another overlay component is a common use case but does not always work exactly as expected.

The code below will not work as expected as because the dialog is within the menu and the dialog will only be open when the menu is open, rendering the dialog unusable.

```python
rx.context_menu.root(
    rx.context_menu.trigger(rx.icon("ellipsis-vertical")),
    rx.context_menu.content(
        rx.context_menu.item(
            rx.dialog.root(
                rx.dialog.trigger(rx.text("Edit")),
                rx.dialog.content(...),
                ....
            )
        ),
    ),
)
```

In this example, we will show how to open a dialog box from a context menu, where the menu will close and the dialog will open and be functional.

```python
class ContextMenuState(rx.State):
    which_dialog_open: str = ""

    @rx.event
    def delete(self):
        yield rx.toast("Deleted item")

    @rx.event
    def save_settings(self):
        yield rx.toast("Saved settings")

def delete_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Are you Sure?"),
            rx.alert_dialog.description(
                rx.text(
                    "This action cannot be undone. Are you sure you want to delete this item?",
                ),
                margin_bottom="20px",
            ),
            rx.hstack(
                rx.alert_dialog.action(
                    rx.button(
                        "Delete",
                        color_scheme="red",
                        on_click=ContextMenuState.delete,
                    )
                ),
                rx.spacer(),
                rx.alert_dialog.cancel(rx.button("Cancel")),
            ),
        ),
        open=ContextMenuState.which_dialog_open == "delete",
        on_open_change=ContextMenuState.set_which_dialog_open("")
    )

def settings_dialog():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Settings"),
            rx.dialog.description(
                rx.text(
                    "Set your settings in this settings dialog.",
                ),
                margin_bottom="20px",
            ),
            rx.dialog.close(
                rx.button(
                    "Close",
                    on_click=ContextMenuState.save_settings,
                )
            ),
        ),
        open=ContextMenuState.which_dialog_open == "settings",
        on_open_change=ContextMenuState.set_which_dialog_open("")
    )

def context_menu_call_dialog():
    return rx.vstack(
        rx.context_menu.root(
            rx.context_menu.trigger(rx.icon("ellipsis-vertical")),
            rx.context_menu.content(
                rx.context_menu.item(
                    "Delete",
                    on_click=ContextMenuState.set_which_dialog_open("delete"),
                ),
                rx.context_menu.item(
                    "Settings",
                    on_click=ContextMenuState.set_which_dialog_open("settings"),
                ),
            ),
        ),
        rx.cond(ContextMenuState.which_dialog_open,
                rx.heading(f"{ContextMenuState.which_dialog_open} dialog is open")),
        delete_dialog(),
        settings_dialog(),
        align="center"
    )
```

[API Reference](https://reflex.dev/docs/library/overlay/context-menu/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/context-menu/#rx.context_menu.root)

# rx.context_menu.root

Menu representing a set of actions, displayed at the origin of a pointer right-click or long-press.

## Context Menu (right click)
Prop | Type | Default | Interactive
--- | --- | --- | ---
modal | bool |  | false
dir | "ltr" | "ltr" | ltr

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.
  
- **on_pointer_down_outside**
  Fired when a pointer down event happens outside the context menu.
  
- **on_focus_outside**
  Fired when focus moves outside the context menu.
  
- **on_interact_outside**
  Fired when interacting outside the context menu.

# rx.context_menu.item

The component that contains the context menu items.

## Context Menu (right click)

```python
Context Menu (right click)
```

### Properties

| Prop          | Type | Default | Interactive |
|---------------|------|---------|------------|
| `color_scheme` | `"tomato" | "red" | ...` | - | - |
| `shortcut`    | `str` | - | - |
| `as_child`    | `bool` | - | - |
| `disabled`    | `bool` | - | <label class="rt-Text rt-r-size-2"><div class="rt-Flex rt-r-gap-2"><button aria-checked="false" class="rt-reset rt-BaseCheckboxRoot rt-CheckboxRoot rt-r-size-2 rt-variant-surface" data-state="unchecked" role="checkbox" type="button" value="on"></button>false</div></label> |
| `text_value`  | `str` | - | - |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.
  
- **on_pointer_down_outside**
  Fired when a pointer down event happens outside the context menu.
  
- **on_focus_outside**
  Fired when focus moves outside the context menu.
  
- **on_interact_outside**
  Fired when interacting outside the context menu.

# rx.context_menu.separator

Separates items in a context menu.

## Description

```markdown
<p>Separates items in a context menu.</p>
```
```python
# Example Python code to illustrate the use (if any)
def separate_context_menu_items():
    # Code to separate context menu items
    pass
```

Props

No component specific props

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.
- **on_pointer_down_outside**
  Fired when a pointer down event happens outside the context menu.
- **on_focus_outside**
  Fired when focus moves outside the context menu.
- **on_interact_outside**
  Fired when interacting outside the context menu.

# rx.context_menu.trigger

Wraps the element that will open the context menu.

## Context Menu (right click)

### Props

- **Prop**: `disabled`
  - **Type | Values**: `bool`
  - **Default**: 
  - **Interactive**: 
    - false

---

This is the converted content in Markdown format.

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_escape_key_down`
  - Description: Fired when the escape key is pressed.

- **Trigger:** `on_pointer_down_outside`
  - Description: Fired when a pointer down event happens outside the context menu.

- **Trigger:** `on_focus_outside`
  - Description: Fired when focus moves outside the context menu.

- **Trigger:** `on_interact_outside`
  - Description: Fired when interacting outside the context menu.

# rx.context_menu.content

The component that pops out when the context menu is open.

## Props

| Prop          | Type | Values           | Default | Interactive |
|---------------|------|------------------|---------|------------|
| size          | "1" | "2"              |         |            |
| variant       | "solid" | "soft"           |         |            |
| color_scheme  | "tomato" | "red" ...        |         |            |
| high_contrast | bool                    | false   |            |
| as_child      | bool                    | false   |            |
| loop          | bool                    | false   |            |
| force_mount   | bool                    | false   |            |
| side          | "top" | "right" ...      | top     |            |
| side_offset   | int, float               |         |            |
| align         | "start" | "center" ...     | start   |            |
| align_offset  | int, float               |         |            |
| avoid_collisions | bool       | false            |         |
| collision_padding | float, int, dict        |         |            |
| sticky        | "partial" | "always"         | partial |            |
| hide_when_detached | bool       | false            |         |

Context Menu (right click)

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- `on_escape_key_down`: Fired when the escape key is pressed.
- `on_pointer_down_outside`: Fired when a pointer down event happens outside the context menu.
- `on_focus_outside`: Fired when focus moves outside the context menu.
- `on_interact_outside`: Fired when interacting outside the context menu.

# rx.context_menu.sub

Contains all the parts of a submenu.

## Context Menu (right click)

<div>
  <p>Context Menu (right click)</p>
</div>

### Props

| Prop        | Type | Values | Default | Interactive |
|-------------|------|--------|---------|------------|
| open        | bool | -      |         |            |
| default_open| bool | -      |         |            |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.
  
- **on_pointer_down_outside**
  Fired when a pointer down event happens outside the context menu.
  
- **on_focus_outside**
  Fired when focus moves outside the context menu.
  
- **on_interact_outside**
  Fired when interacting outside the context menu.

# rx.context_menu.sub_trigger

An item that opens a submenu.

## Context Menu (right click)

Prop | Type | Values | Default | Interactive
--- | --- | --- | --- | ---
as_child | bool |
disabled | bool |
text_value | str |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.

- **on_pointer_down_outside**
  Fired when a pointer down event happens outside the context menu.

- **on_focus_outside**
  Fired when focus moves outside the context menu.

- **on_interact_outside**
  Fired when interacting outside the context menu.

# rx.context_menu.sub_content

The component that pops out when a submenu is open.

Context Menu (right click)

* `as_child`: bool
* `loop`: bool
* `force_mount`: bool
* `side_offset`: Union[int, float]
* `align_offset`: Union[int, float]
* `avoid_collisions`: bool
* `collision_padding`: Union[float, int, dict]
* `sticky`: "partial" | "always"
* `hide_when_detached`: bool

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- `on_escape_key_down`: Fired when the escape key is pressed.
- `on_pointer_down_outside`: Fired when a pointer down event happens outside the context menu.
- `on_focus_outside`: Fired when focus moves outside the context menu.
- `on_interact_outside`: Fired when interacting outside the context menu.