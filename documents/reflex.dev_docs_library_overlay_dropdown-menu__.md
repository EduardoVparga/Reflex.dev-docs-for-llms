# Dropdown Menu

A Dropdown Menu is a menu that offers a list of options that a user can select from. They are typically positioned near a button that will control their appearance and disappearance.

A Dropdown Menu is composed of a `menu.root`, a `menu.trigger` and a `menu.content`. The `menu.trigger` is the element that the user interacts with to open the menu. It wraps the element that will open the dropdown menu. The `menu.content` is the component that pops out when the dropdown menu is open.

The `menu.item` contains the actual dropdown menu items and sits under the `menu.content`. The `shortcut` prop is an optional shortcut command displayed next to the item text.

The `menu.sub` contains all the parts of a submenu. There is a `menu.sub_trigger`, which is an item that opens a submenu. It must be rendered inside a `menu.sub` component. The `menu.sub_component` is the component that pops out when a submenu is open. It must also be rendered inside a `menu.sub` component.

The `menu.separator` is used to visually separate items in a dropdown menu.

```python
rx.menu.root(
    rx.menu.trigger(
        rx.button("Options", variant="soft"),
    ),
    rx.menu.content(
        rx.menu.item("Edit", shortcut="⌘ E"),
        rx.menu.item("Duplicate", shortcut="⌘ D"),
        rx.menu.separator(),
        rx.menu.item("Archive", shortcut="⌘ N"),
        rx.menu.sub(
            rx.menu.sub_trigger("More"),
            rx.menu.sub_content(
                rx.menu.item("Move to project…"),
                rx.menu.item("Move to folder…"),
                rx.menu.separator(),
                rx.menu.item("Advanced options…"),
            ),
        ),
        rx.menu.separator(),
        rx.menu.item("Share"),
        rx.menu.item("Add to favorites"),
        rx.menu.separator(),
        rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
    ),
)
```

For more information on events when the dropdown menu opens or closes, see [the documentation](https://reflex.dev/docs/library/overlay/dropdown-menu/#events-when-the-dropdown-menu-opens-or-closes).

# Events when the Dropdown Menu opens or closes

The `on_open_change` event, from the `menu.root`, is called when the `open` state of the dropdown menu changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
    </div>
</div>

# Number of times Dropdown Menu opened or closed: 0

# Dropdown Menu open: false

Options

Number of times Dropdown Menu opened or closed: 0

Dropdown Menu open: False

Edit (⌘ E)

Duplicate (⌘ D)

Archive (⌘ N)

Delete (⌘ ⌫, red)

# Opening a Dialog from Menu using State

Accessing an overlay component from within another overlay component is a common use case but does not always work exactly as expected.

The code below will not work as expected as because the dialog is within the menu and the dialog will only be open when the menu is open, rendering the dialog unusable.

```python
rx.menu.root(
    rx.menu.trigger(rx.icon("ellipsis-vertical")),
    rx.menu.content(
        rx.menu.item(
            rx.dialog.root(
                rx.dialog.trigger(rx.text("Edit")),
                rx.dialog.content(...)
                ...
            ),
        ),
    ),
)
```

In this example, we will show how to open a dialog box from a dropdown menu, where the menu will close and the dialog will open and be functional.

```python
class DropdownMenuState2(rx.State):
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
                        on_click=DropdownMenuState2.delete,
                    ),
                ),
                rx.spacer(),
                rx.alert_dialog.cancel(rx.button("Cancel")),
            ),
        ),
        open=DropdownMenuState2.which_dialog_open == "delete",
        on_open_change=DropdownMenuState2.set_which_dialog_open(""),
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
                    on_click=DropdownMenuState2.save_settings,
                ),
            ),
        ),
        open=DropdownMenuState2.which_dialog_open == "settings",
        on_open_change=DropdownMenuState2.set_which_dialog_open(""),
    )


def menu_call_dialog() -> rx.Component:
    return rx.vstack(
        rx.menu.root(
            rx.menu.trigger(rx.icon("menu")),
            rx.menu.content(
                rx.menu.item(
                    "Delete",
                    on_click=DropdownMenuState2.set_which_dialog_open("delete"),
                ),
                rx.menu.item(
                    "Settings",
                    on_click=DropdownMenuState2.set_which_dialog_open("settings"),
                ),
            ),
        ),
        rx.cond(DropdownMenuState2.which_dialog_open,
                rx.heading(f"{DropdownMenuState2.which_dialog_open} dialog is open")),
        delete_dialog(),
        settings_dialog(),
        align="center",
    )
```

For more information, see the [Reflex documentation](https://reflex.dev/docs/library/overlay/dropdown-menu/#api-reference).

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/dropdown-menu/#rx.dropdown_menu.root)

# rx.dropdown_menu.root

The Dropdown Menu Root Component.

## drop down menu
<button aria-expanded="false" aria-haspopup="menu" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" id="radix-:R1j66kml6:" type="button">drop down menu</button>

## Properties
- **default_open**
  - Type | Values: `bool`
  - Default: 
  
- **open**
  - Type | Values: `bool`
  - Default: 

- **modal**
  - Type | Values: `bool`
  - Default: false

- **dir**
  - Type | Values: `"ltr" | "rtl"`
  - Default: ltr

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.
  
- **on_pointer_down_outside**
  Fired when the pointer is down outside the dialog.
  
- **on_focus_outside**
  Fired when focus moves outside the dialog.
  
- **on_interact_outside**
  Fired when the pointer interacts outside the dialog.

# rx.dropdown_menu.content

The Dropdown Menu Content component that pops out when the dropdown menu is open.

## Drop Down Menu Button
<button aria-expanded="false" aria-haspopup="menu" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" id="radix-:R1ja6kml6:" type="button">drop down menu</button>

## Properties

| Prop               | Type | Values                            | Default | Interactive |
|--------------------|------|-----------------------------------|---------|-------------|
| size               |      | "1" | "2"                               |         |             |
| variant            |      | "solid" | "soft"                            |         |             |
| color_scheme       |      | "tomato" | "red" ...                          |         |             |
| high_contrast      |      | bool                              |         |             |
| as_child           |      | bool                              |         |             |
| loop               |      | bool                              | false   |             |
| force_mount        |      | bool                              | false   |             |
| side               |      | "top" | "right" ...                        | top     |             |
| side_offset        |      | Union[int, float]                  |         |             |
| align              |      | "start" | "center" ...                       | start   |             |
| align_offset       |      | Union[int, float]                  |         |             |
| avoid_collisions   |      | bool                              | false   |             |
| collision_padding  |      | Union[float, int, dict]            |         |             |
| sticky             |      | "partial" | "always"                           | partial |             |
| hide_when_detached |      | bool                              | false   |             |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- `on_escape_key_down` - Fired when the escape key is pressed.
- `on_pointer_down_outside` - Fired when the pointer is down outside the dialog.
- `on_focus_outside` - Fired when focus moves outside the dialog.
- `on_interact_outside` - Fired when the pointer interacts outside the dialog.

# rx.dropdown_menu.trigger

The button that toggles the dropdown menu.

## Prop

- **as_child**
  - **Type**: `bool`
  - **Default**: Not specified

---

## Python Code Example

```python
code_example = """
def example_function(as_child: bool):
    pass
"""
```

---

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- `on_escape_key_down`: Fired when the escape key is pressed.
- `on_pointer_down_outside`: Fired when the pointer is down outside the dialog.
- `on_focus_outside`: Fired when focus moves outside the dialog.
- `on_interact_outside`: Fired when the pointer interacts outside the dialog.

# rx.dropdown_menu.item

The Dropdown Menu Item Component.

## drop down menu
<button aria-expanded="false" aria-haspopup="menu" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" id="radix-:R1ji6kml6:" type="button">drop down menu</button>

## Available Props

| Prop          | Type | Values                      | Default | Interactive |
|---------------|------|-----------------------------|---------|------------|
| color_scheme  | str  | "tomato" | "red" | ...        | -       | -       |
| shortcut      | str  | -                           | -       |            |
| as_child      | bool | -                           | -       |            |
| disabled      | bool | -                           | false   |            |
| text_value    | str  | -                           | -       |            |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

* `on_escape_key_down` - Fired when the escape key is pressed.
* `on_pointer_down_outside` - Fired when the pointer is down outside the dialog.
* `on_focus_outside` - Fired when focus moves outside the dialog.
* `on_interact_outside` - Fired when the pointer interacts outside the dialog.

# rx.dropdown_menu.separator
Dropdown Menu Separator Component. Used to visually separate items in the dropdown menu.
<div class="rt-Box pb-2">
<p class="rt-Text font-normal text-slate-12 mb-4 leading-7">Dropdown Menu Separator Component. Used to visually separate items in the dropdown menu.</p>
</div>

Props
No component specific props

<div>
<p></p>
</div>

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger:** `on_escape_key_down`
  - Description: Fired when the escape key is pressed.
  
- **Trigger:** `on_pointer_down_outside`
  - Description: Fired when the pointer is down outside the dialog.
  
- **Trigger:** `on_focus_outside`
  - Description: Fired when focus moves outside the dialog.
  
- **Trigger:** `on_interact_outside`
  - Description: Fired when the pointer interacts outside the dialog.

# rx.dropdown_menu.sub_content

The component that pops out when a submenu is open. Must be rendered inside DropdownMenuSub.

## Button Example

<button aria-expanded="false" aria-haspopup="menu" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" id="radix-:R1jq6kml6:" type="button">drop down menu</button>

## Properties

- **as_child**: `bool`
- **loop**: `bool`
- **force_mount**: `bool`
- **side_offset**: `Union[int, float]`
- **align_offset**: `Union[int, float]`
- **avoid_collisions**: `bool`
- **collision_padding**: `Union[float, int, dict]`
- **sticky**: `"partial" | "always"`
- **hide_when_detached**: `bool`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_escape_key_down**
  Fired when the escape key is pressed.

- **on_pointer_down_outside**
  Fired when the pointer is down outside the dialog.

- **on_focus_outside**
  Fired when focus moves outside the dialog.

- **on_interact_outside**
  Fired when the pointer interacts outside the dialog.