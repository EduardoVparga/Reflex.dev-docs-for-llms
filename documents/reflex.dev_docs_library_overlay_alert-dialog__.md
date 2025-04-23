# Alert Dialog

An alert dialog is a modal confirmation dialog that interrupts the user and expects a response.

The `alert_dialog.root` contains all the parts of the dialog.
The `alert_dialog.trigger` wraps the control that will open the dialog.
The `alert_dialog.content` contains the content of the dialog.
The `alert_dialog.title` is the title that is announced when the dialog is opened.
The `alert_dialog.description` is an optional description that is announced when the dialog is opened.
The `alert_dialog.action` wraps the control that will close the dialog. This should be distinguished visually from the `alert_dialog.cancel` control.
The `alert_dialog.cancel` wraps the control that will close the dialog. This should be distinguished visually from the `alert_dialog.action` control.

[Learn more](https://reflex.dev/docs/library/overlay/alert-dialog/#basic-example)

# Basic Example

![](https://via.placeholder.com/30)

<button aria-controls="radix-:R5h6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Revoke access</button>

```python
rx.alert_dialog.root(
    rx.alert_dialog.trigger(rx.button("Revoke access")),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Revoke access"),
        rx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
        ),
        rx.flex(
            rx.alert_dialog.cancel(rx.button("Cancel")),
            rx.alert_dialog.action(rx.button("Revoke access")),
            spacing="3",
            justify="end",
        ),
    ),
)
```

This example has a different color scheme and the `cancel` and `action` buttons are right aligned.

<button aria-controls="radix-:R5p6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="red" data-state="closed" type="button">Revoke access</button>

```python
rx.alert_dialog.root(
    rx.alert_dialog.trigger(rx.button("Revoke access", color_scheme="red")),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Revoke access"),
        rx.alert_dialog.description(
            "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
            size="2",
        ),
        rx.flex(
            rx.alert_dialog.cancel(rx.button("Cancel", variant="soft", color_scheme="gray")),
            rx.alert_dialog.action(rx.button("Revoke access", color_scheme="red", variant="solid")),
            spacing="3",
            justify="end",
            margin_top="16px",
            style={"max_width": 450},
        ),
    ),
)
```

Use the `inset` component to align content flush with the sides of the dialog.

<button aria-controls="radix-:R616kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="red" data-state="closed" type="button">Delete Users</button>

```python
rx.alert_dialog.root(
    rx.alert_dialog.trigger(rx.button("Delete Users", color_scheme="red")),
    rx.alert_dialog.content(
        rx.alert_dialog.title("Delete Users"),
        rx.alert_dialog.description(
            "Are you sure you want to delete these users? This action is permanent and cannot be undone.",
            size="2",
        ),
        rx.inset(
            rx.table.root(
                rx.table.header(rx.table.row(
                    rx.table.column_header_cell("Full Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Group"),
                )),
                rx.table.body(rx.table.row(
                    rx.table.row_header_cell("Danilo Rosa"),
                    rx.table.cell("danilo@example.com"),
                    rx.table.cell("Developer"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("Zahra Ambessa"),
                    rx.table.cell("zahra@example.com"),
                    rx.table.cell("Admin"),
                )),
            ),
            side="x",
            margin_top="24px",
            margin_bottom="24px",
        ),
        rx.flex(
            rx.alert_dialog.cancel(rx.button("Cancel", variant="soft", color_scheme="gray")),
            rx.alert_dialog.action(rx.button("Delete users", color_scheme="red")),
            spacing="3",
            justify="end",
            style={"max_width": 500},
        ),
    ),
)
```

For more information, you can visit the [documentation](https://reflex.dev/docs/library/overlay/alert-dialog/#events-when-the-alert-dialog-opens-or-closes).

# Events when the Alert Dialog opens or closes

The `on_open_change` event is called when the `open` state of the dialog changes. It is used in conjunction with the `open` prop.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
  </div>
</div>

# Number of times alert dialog opened or closed: 0

# Alert Dialog open: false

**Revoke access**

## Number of times alert dialog opened or closed: 0

## Alert Dialog open: false

- **Button:** Revoke access (Red, Solid)
- **Cancel Button:** Cancel (Gray, Soft)
- **Description:** Are you sure? This application will no longer be accessible and any existing sessions will be expired.
- **Title:** Revoke access

# Controlling Alert Dialog with State

This example shows how to control whether the dialog is open or not with state. This is an easy way to show the dialog without needing to use the `rx.alert_dialog.trigger`.

`rx.alert_dialog.root` has a prop `open` that can be set to a boolean value to control whether the dialog is open or not.

We toggle this `open` prop with a button outside of the dialog and the `rx.alert_dialog.cancel` and `rx.alert_dialog.action` buttons inside the dialog.

- **Button to Open the Dialog**

```python
class AlertDialogState2(rx.State):
    opened: bool = False

    @rx.event
    def dialog_open(self):
        self.opened = not self.opened


def alert_dialog2():
    return rx.box(
        rx.alert_dialog.root(
            rx.alert_dialog.content(
                rx.alert_dialog.title("Revoke access"),
                rx.alert_dialog.description(
                    "Are you sure? This application will no longer be accessible and any existing sessions will be expired.",
                ),
                rx.flex(
                    rx.alert_dialog.cancel(
                        rx.button(
                            "Cancel",
                            on_click=AlertDialogState2.dialog_open,
                        ),
                    ),
                    rx.alert_dialog.action(
                        rx.button(
                            "Revoke access",
                            on_click=AlertDialogState2.dialog_open,
                        ),
                    ),
                    spacing="3",
                ),
            ),
            open=AlertDialogState2.opened,
        ),
        rx.button(
            "Button to Open the Dialog",
            on_click=AlertDialogState2.dialog_open,
        ),
    )
```

[View Code](https://reflex.dev/docs/library/overlay/alert-dialog/#form-submission-to-a-database-from-an-alert-dialog)

# Form Submission to a Database from an Alert Dialog

This example adds new users to a database from an alert dialog using a form.

1. It defines a `User1` model with name and email fields.
2. The `add_user_to_db` method adds a new user to the database, checking for existing emails.
3. On form submission, it calls the `add_user_to_db` method.
4. The UI component has:
    - A button to open an alert dialog
    - An alert dialog containing a form to add a new user
        - Input fields for name and email
        - Submit and Cancel buttons

```python
class User1(rx.Model, table=True):
    """The user model."""
    name: str
    email: str


class State(rx.State):
    current_user: User1 = User1()

    @rx.event
    def add_user_to_db(self, form_data: dict):
        self.current_user = form_data

        return rx.toast.info(
            f"User {self.current_user['name']} has been added.",
            position="bottom-right",
        )


def index() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon(name="plus", size=26),
                rx.text("Add User", size="4"),
            )
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Add New User"),
            rx.alert_dialog.description("Fill the form with the user's info"),
            rx.form(
                rx.flex(
                    rx.input(placeholder="User Name", name="name"),
                    rx.input(placeholder="user@reflex.dev", name="email"),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.alert_dialog.action(
                            rx.button("Submit", type="submit"),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=State.add_user_to_db,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
```

For more details, see the [API Reference](https://reflex.dev/docs/library/overlay/alert-dialog/#api-reference).

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/alert-dialog/#rx.alert_dialog.root)

# rx.alert_dialog.root

Contains all the parts of the dialog.

## Revoke access
<button aria-controls="radix-:R1j66kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Revoke access</button>

## Properties
Prop | Type | Default | Interactive
--- | --- | --- | ---
open | bool |  | 
default_open | bool | 

This table describes the properties of the dialog.

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.alert_dialog.content

Contains the content of the dialog. This component is based on the div element.

## Revoke access

<button aria-controls="radix-:R1ja6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Revoke access</button>

### Properties

- **size**
  - Type | Values: `"1" | "2" | ...`
  - Default: None
  - Interactive: Dropdown

- **force_mount**
  - Type: `bool`
  - Default: None
  - Interactive: Checkbox

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.alert_dialog.trigger

Wraps the control that will open the dialog.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.alert_dialog.title

An accessible title that is announced when the dialog is opened.
This part is based on the Heading component with a pre-defined font size and
leading trim on top.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.alert_dialog.description

An optional accessible description that is announced when the dialog is opened.
This part is based on the Text component with a pre-defined font size.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.alert_dialog.action

Wraps the control that will close the dialog. This should be distinguished
visually from the Cancel control.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.alert_dialog.cancel

Wraps the control that will close the dialog. This should be distinguished
visually from the Action control.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)