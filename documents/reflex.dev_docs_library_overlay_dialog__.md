# Dialog

The `dialog.root` contains all the parts of a dialog.

The `dialog.trigger` wraps the control that will open the dialog.

The `dialog.content` contains the content of the dialog.

The `dialog.title` is a title that is announced when the dialog is opened.

The `dialog.description` is a description that is announced when the dialog is opened.

The `dialog.close` wraps the control that will close the dialog.

[Open Dialog](#)

```python
rx.dialog.root(
    rx.dialog.trigger(rx.button("Open Dialog")),
    rx.dialog.content(
        rx.dialog.title("Welcome to Reflex!"),
        rx.dialog.description(
            "This is a dialog component. You can render anything you want in here."
        ),
        rx.dialog.close(
            rx.button("Close Dialog", size="3")
        ),
    ),
)
```

[View Code]

# In context examples

## Edit Profile

Edit your profile details and preferences.

**Button:**
Edit Profile

**Dialog Content:**

- **Title:** Edit Profile
- **Description:** Change your profile details and preferences.
- **Fields:**
  - Name: Freja Johnson (Enter your name)
  - Email: freja@example.com (Enter your email)

**Buttons:**
- Cancel
- Save

## View Users

View the list of users with access to this project.

**Button:**
View users

**Dialog Content:**

- **Title:** Users
- **Description:** The following users have access to this project.
- **Table:**

  | Full Name   | Email                | Group     |
  |-------------|----------------------|-----------|
  | Danilo Rosa | danilo@example.com   | Developer |
  | Zahra Ambessa | zahra@example.com    | Admin     |

**Button:**
Close

# Events when the Dialog opens or closes

The `on_open_change` event is called when the `open` state of the dialog changes. It is used in conjunction with the `open` prop, which is passed to the event handler.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-gap-3"></div>
    </div>
</div>

# Number of times dialog opened or closed: 0

# Dialog open: false
Open Dialog

Number of times dialog opened or closed: 0
Dialog open: false

Welcome to Reflex!
This is a dialog component. You can render anything you want in here.
Close Dialog

Check out the [menu docs](/docs/library/overlay/dropdown-menu/) for an example of opening a dialog from within a dropdown menu.

# Form Submission to a Database from a Dialog

This example adds new users to a database from a dialog using a form.

1. It defines a User model with name and email fields.
2. The `add_user_to_db` method adds a new user to the database, checking for existing emails.
3. On form submission, it calls the `add_user_to_db` method.
4. The UI component has:
    - A button to open a dialog
    - A dialog containing a form to add a new user
    - Input fields for name and email
    - Submit and Cancel buttons

```python
class User(rx.Model, table=True):
    """The user model."""
    name: str
    email: str


class State(rx.State):
    current_user: User = User()

    @rx.event
    def add_user_to_db(self, form_data: dict):
        self.current_user = form_data
        # ### Uncomment the code below to add your data to a database ###
        # with rx.session() as session:
        #     if session.exec(select(User).where(user.email == self.current_user["email"])).first():
        #         return rx.window_alert("User with this email already exists")
        #     session.add(User(**self.current_user))
        #     session.commit()

        return rx.toast.info(
            f"User {self.current_user['name']} has been added.",
            position="bottom-right",
        )


def index() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon(name="plus", size=26),
                rx.text("Add User", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Add New User"),
            rx.dialog.description("Fill the form with the user's info"),
            rx.form(
                rx.flex(
                    rx.input(placeholder="User Name", name="name"),
                    rx.input(placeholder="user@reflex.dev", name="email"),
                    rx.flex(
                        rx.dialog.close(rx.button("Cancel", variant="soft", color_scheme="gray")),
                        rx.dialog.close(
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
        ),
    )
```

[Learn more about dialog in Reflex](https://reflex.dev/docs/library/overlay/dialog/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/dialog/#rx.dialog.root)

# rx.dialog.root

Root component for Dialog.

## Button

- **Open Dialog**
  - Type: `button`
  - Action: Open Dialog

---

## Properties

| Prop          | Type | Values     | Default | Interactive |
|---------------|------|------------|---------|-------------|
| open          | bool |            |         |             |
| default_open  | bool |            |         |             |

---

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.dialog.trigger
Trigger an action or event, to open a Dialog modal.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.dialog.title

Title component to display inside a Dialog modal.

Props
No component specific props

<div>
  
</div>

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.dialog.content

Content component to display inside a Dialog modal.

## Open Dialog
<button aria-controls="radix-:R1ji6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Open Dialog</button>

## Properties
- **Prop**: Type | Values
- **size**: `"1" | "2" | ...`
- **Default**: 
- **Interactive**:
  - <button aria-autocomplete="none" aria-controls="radix-:R2e66ji6kml6:" aria-expanded="false" class="rt-reset rt-SelectTrigger rt-r-size-2 rt-variant-surface w-32 font-small text-slate-11" data-state="closed" dir="ltr" role="combobox" type="button"><span class="rt-SelectTriggerInner"><span style="pointer-events:none">1</span></span><svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewbox="0 0 9 9" width="9" xmlns="http://www.w3.org/2000/svg"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg></button>

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.dialog.description

Description component to display inside a Dialog modal.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

Div with no content

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.dialog.close
Close button component to close an open Dialog modal.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)