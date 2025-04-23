# Drawer

![Open Drawer](#)

<button aria-controls="radix-:R1d6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Open Drawer</button>

rx.drawer.root(rx.drawer.trigger(rx.button("Open Drawer")), rx.drawer.overlay(z_index="5"), rx.drawer.portal(rx.drawer.content(rx.flex(rx.drawer.close(rx.box(rx.button("Close"))), align_items="start", direction="column"), top="auto", right="auto", height="100%", width="20em", padding="2em", background_color="#FFF")), direction="left"))

![Copy Code](#)

# Sidebar Menu with a Drawer and State
This example shows how to create a sidebar menu with a drawer. The drawer is opened by clicking a button. The drawer contains links to different sections of the page. When a link is clicked, the drawer closes and the page scrolls to the section.

The `rx.drawer.root` component has an `open` prop that is set by the state variable `is_open`. Setting the `modal` prop to `False` allows the user to interact with the rest of the page while the drawer is open and allows the page to be scrolled when a user clicks one of the links.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
            <div aria-controls="radix-:Rpt6kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-Flex" data-state="closed" type="button">
                <button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="">Open Drawer</button>
            </div>
        </section>
    </div>
</div>

# Test1

## test2

# Test2

```python
class DrawerState(rx.State):
    is_open: bool = False
    
    @rx.event
    def toggle_drawer(self):
        self.is_open = not self.is_open


def drawer_content():
    return rx.drawer.content(
        rx.flex(
            rx.drawer.close(
                rx.button("Close", on_click=DrawerState.toggle_drawer),
            ),
            rx.link("Link 1", href="#test1", on_click=DrawerState.toggle_drawer),
            rx.link("Link 2", href="#test2", on_click=DrawerState.toggle_drawer),
            align_items="start",
            direction="column"
        ),
        height="100%",
        width="20%",
        padding="2em",
        background_color=rx.color("grass", 7)
    )


def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button("Open Drawer", on_click=DrawerState.toggle_drawer),
        ),
        rx.drawer.overlay(),
        rx.drawer.portal(drawer_content()),
        open=DrawerState.is_open,
        direction="left",
        modal=False
    )


def drawer_sidebar():
    return rx.vstack(
        lateral_menu(),
        rx.section(rx.heading("Test1", size="8", id="test1", height="400px")),
        rx.section(rx.heading("Test2", size="8", id="test2", height="400px"))
    )
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/overlay/drawer/#api-reference">...</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/overlay/drawer/#rx.drawer.root)

# rx.drawer.root

The Root component of a Drawer, contains all parts of a drawer.

## Open Drawer Button
<button aria-controls="radix-:R1j66kml6:" aria-expanded="false" aria-haspopup="dialog" class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-state="closed" type="button">Open Drawer</button>

## Props

| Prop       | Type | Default | Description |
|------------|------|---------|-------------|
| default_open | bool |         |             |
| open       | bool |         |             |
| modal      | bool |         |             |
| direction  | "top" | "right" | ...        |         |
| dismissible | bool |         |             |
| handle_only | bool |         |             |
| snap_points | Sequence |          |             |
| fade_from_index | int |         |             |
| scroll_lock_timeout | int |         |             |
| prevent_scroll_restoration | bool |         |             |
| should_scale_background | bool |         |             |
| close_threshold | float |         |             |
| as_child   | bool |         |             |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.drawer.trigger

The button that opens the dialog.

## Prop

| Prop        | Type | Default       |
|-------------|------|---------------|
| as_child    | bool | Var.create(True) |

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.drawer.overlay

A layer that covers the inert portion of the view when the dialog is open.

## Prop

- **as_child**
  - Type: `bool`
  - Default: Not specified

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.drawer.portal
Portals your drawer into the body.

## Props

- **as_child**
  - Type: `bool`
  - Default: None

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.drawer.content

Content that should be rendered in the drawer.

## Prop | Type | Values | Default

- **as_child**
  - **Type:** `bool`
  - **Default:** `None`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.drawer.close

A button that closes the drawer.

## Prop

- **as_child** - `bool`  
  Default: `Var.create(True)`  

![Info](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAADUlEQVQIW2P8z8/AADCAcAEZ5SOGgAAAABJRU5ErkJggg==) - More information about `as_child`.

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)