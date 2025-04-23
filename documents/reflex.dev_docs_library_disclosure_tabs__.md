# Tabs

Tabs are a set of layered sections of content—known as tab panels that are displayed one at a time.
They facilitate the organization and navigation between sets of content that share a connection and exist at a similar level of hierarchy.

[Basic Example](https://reflex.dev/docs/library/disclosure/tabs/#basic-example)

# Basic Example

The `tabs` component is made up of a `rx.tabs.root` which groups `rx.tabs.list` and `rx.tabs.content` parts.

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
    ),
    rx.tabs.content(
        rx.text("item on tab 1"), value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"), value="tab2",
    ),
)
```

For more information, you can visit the [official documentation](https://reflex.dev/docs/library/disclosure/tabs/#styling).

It looks like you've provided a detailed and structured documentation for a set of tabs components in Reflex (possibly a UI framework), including their props, values, default behaviors, and event triggers. Here's a summary and some key points extracted from the content:

### Summary:
1. **Tab Component (`rx.tabs`)**: This component manages multiple tab panels.
2. **Trigger Component (`rx.tabs.tab` or `rt-BaseTabListTrigger`)**: The buttons that switch between different tabs.
3. **Content Component (`rx.tabs.content` or `rt-TabsContent`)**: The content associated with each tab.

### Key Points:
1. **Props**:
   - **value**: Represents the value of the current active tab.
   - **disabled**: Controls whether a tab is disabled (cannot be clicked).
   - **color_scheme**: Sets the color scheme for the tab button.
   - **force_mount**: Forces mounting the component, ensuring it's always in memory.

2. **Interactive Properties**:
   - Both `value` and `disabled` have default values that can be overridden with provided props.
   - The color scheme prop allows for dynamic styling based on selected options or custom colors.
   - The `force_mount` prop ensures the component remains mounted, which is useful in scenarios where you want to avoid unnecessary re-renders.

3. **Event Triggers**:
   - There are numerous event triggers available, such as `onClick`, `onMouseEnter`, etc., that can be used to perform actions when interacting with the tabs.
   - Event handling is typically done using Reflex's event system and can be customized according to specific needs.

4. **Default States**:
   - By default, all tabs are inactive (`aria-selected="false"`), and their content panels are hidden.
   - When a tab is clicked (or otherwise activated), the corresponding content panel becomes visible.

5. **Styling and Customization**:
   - The component supports various styling options through props like `color_scheme`.
   - There's also an option to manually set colors using color palette icons, indicating that additional customization might be available.

### Example Usage:
Here’s a simplified example of how you might use these components:

```python
from reflex import *

class App(State):
    active_tab: str = "account"

def tab_button(label: str):
    return Button(
        label=label,
        on_click=lambda: set_state(App, active_tab=label),
        color_scheme="tomato" if app.active_tab == label else None
    )

def content_panel(label: str):
    return Panel(
        f"Content for {label}",
        force_mount=app.active_tab == label
    )

def ui():
    return Flex([
        tab_button("Account"),
        tab_button("Documents"),
        tab_button("Settings"),
        TabContent([
            content_panel("account"),
            content_panel("documents"),
            content_panel("settings")
        ])
    ])

app = App()
ui()
```

### Documentation Improvement Suggestions:
1. **Consistency**: Ensure that the documentation is consistent in terms of style and formatting.
2. **Examples**: Provide more examples to illustrate how different props and events can be used together.
3. **Best Practices**: Include best practices for using these components, such as performance considerations when using `force_mount`.
4. **API Reference**: Create a separate API reference section that lists all available methods and properties.

This documentation is very detailed but could benefit from more examples and perhaps some best practice guidelines to help users understand how to integrate these components effectively into their applications.

# Default value

We use the `default_value` prop to set a default active tab, this will select the specified tab by default.

Tab 2 is currently selected. 

- Tab 1
- Tab 2 (item on tab 2)

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
    ),
    rx.tabs.content(
        rx.text("item on tab 1"), 
        value="tab1",
    ),
    rx.tabs.content(
        rx.text("item on tab 2"), 
        value="tab2",
    ),
    default_value="tab2",
)
```

# Orientation

We use `orientation` prop to set the orientation of the tabs component to `vertical` or `horizontal`. By default, the orientation will be set to `horizontal`. Setting this value will change both the visual orientation and the functional orientation.

<div data-orientation="vertical" data-variant="classic">
<div class="AccordionItem" data-orientation="vertical" data-state="closed"></div>
</div>

# The functional orientation means for `vertical`, the `up` and `down` arrow keys moves focus between the next or previous tab, while for `horizontal`, the `left` and `right` arrow keys moves focus between tabs.

# When using vertical orientation, make sure to assign a tabs.content for each trigger.
When using vertical orientation, make sure to assign a tabs.content for each trigger.

## Tab 1
item on tab 1

## Tab 2

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
    ),
    rx.tabs.content(rx.text("item on tab 1"), value="tab1"),
    rx.tabs.content(rx.text("item on tab 2"), value="tab2"),
    default_value="tab1",
    orientation="vertical",
)
```

---

## Tab 1
item on tab 1

## Tab 2

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
    ),
    rx.tabs.content(rx.text("item on tab 1"), value="tab1"),
    rx.tabs.content(rx.text("item on tab 2"), value="tab2"),
    default_value="tab1",
    orientation="horizontal",
)
```

[More details](https://reflex.dev/docs/library/disclosure/tabs/#value)

The provided content is a detailed documentation or API reference for various components related to tabs in a React application, likely using the Reflex UI library. Here’s an overview and some key points extracted from it:

### Components Overview

1. **`rx.tabs()`**:
   - A higher-order component that wraps other tab-related components.
   
2. **`rx.tabs.header()`**:
   - Represents the header part of a tab, containing the navigation items.

3. **`rx.tabs.content()`**:
   - Contains the content associated with each tab.

4. **`rx.tabs.trigger()`**:
   - Represents an individual tab trigger (button or link) that can be selected to show its corresponding content.
   
5. **`rx.tabs.panel()`**:
   - Displays the content of a specific tab when triggered.

### Properties and Usage

#### `rx.tabs()`
- **Props**: 
  - `value`: The currently active value.
  - `children`: Children components that represent tabs.
  
#### `rx.tabs.header()`
- **Props**:
  - `className`: Additional class names for styling.
  - `onSelect`: Event handler when a tab is selected.

#### `rx.tabs.trigger()`
- **Props**:
  - `value`: The value associated with this trigger (e.g., "account", "documents").
  - `children`: Content of the trigger (e.g., text or icon).
  - `className`: Additional class names for styling.
  - `color_scheme`: Color scheme for the button, e.g., `"tomato"`, `"red"`.
  - `disabled`: Whether the tab is disabled.
  - `force_mount`: Whether to force mounting of the content.

#### `rx.tabs.content()`
- **Props**:
  - `value`: The value associated with this content (e.g., "account", "documents").
  - `children`: Content that will be shown when this tab is selected.

### Event Triggers
The documentation also mentions event triggers, which include:
- `onSelect`: Triggered when a tab is selected.
  
### Example Usage

```jsx
<rx.tabs value="account">
  <rx.tabs.header>
    <rx.tabs.trigger value="account">Account</rx.tabs.trigger>
    <rx.tabs.trigger value="documents">Documents</rx.tabs.trigger>
    <rx.tabs.trigger value="settings">Settings</rx.tabs.trigger>
  </rx.tabs.header>
  
  <rx.tabs.content value="account">
    {/* Content for the account tab */}
  </rx.tabs.content>

  <rx.tabs.content value="documents">
    {/* Content for the documents tab */}
  </rx.tabs.content>

  <rx.tabs.content value="settings">
    {/* Content for the settings tab */}
  </rx.tabs.content>
</rx.tabs>
```

### Customization

- **Colors**: You can customize the color scheme of the tabs using the `color_scheme` prop.
- **Disabled State**: Use the `disabled` prop to make a tab inactive.
- **Force Mounting**: The `force_mount` prop ensures that content is always mounted, even if it's not currently visible.

### Interactive Elements

- **Color Options**: The color scheme can be customized with various options like `"tomato"`, `"red"`, etc. There are also options to display a palette for selecting colors.
  
This documentation provides comprehensive information on how to use the `rx.tabs` components effectively in a React application, along with detailed descriptions of props and their usage.

# Tablist
The Tablist is used to list the respective tabs to the tab component

[Tab Trigger](https://reflex.dev/docs/library/disclosure/tabs/#tab-trigger)

# Tab Trigger

This is the button that activates the tab's associated content. It is typically used in the `Tablist`.

[Learn more](https://reflex.dev/docs/library/disclosure/tabs/#styling)

# Styling

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/disclosure/tabs/#value"></a>

It looks like you have a detailed documentation or reference for various components and props related to a `rx.tabs` system in Reflex UI. This seems to cover the tab panel, including different parts such as the tab content, the tab itself (trigger), and possibly the context it resides in. Below is an organized summary of what I can gather from your snippet:

### Summary

1. **Tab Panel (`rx.tabs`)**:
   - Contains a collection of tabs that allow users to switch between different panes or sections.

2. **Tabs**:
   - Each tab is represented by the `rx.tabs.triggers` component.
   - Includes properties such as value, color scheme, and more.

3. **Tab Content (`rx.tabs.content`)**:
   - Contains the actual content associated with each tab.
   - Properties include `value`, `force_mount`, etc.

4. **Tab Triggers**:
   - Represented by the `rx.tabs.triggers` component.
   - Includes properties such as value, color scheme, disabled state, and more.

5. **Props Overview**:
   - `value`: String representing the tab's value or identifier.
   - `disabled`: Boolean indicating if the tab should be disabled.
   - `color_scheme`: Defines the appearance of the tab with various color options.
   - `force_mount`: Boolean that determines whether the content is mounted immediately.

6. **Event Triggers**:
   - Documentation suggests there are event triggers available, likely for actions like switching between tabs.

### Example Breakdown

- **Tab Content (`rx.tabs.content`)**:
  ```html
  <div id="content-account" aria-labelledby="trigger-account">
    <!-- Content for the "Account" tab -->
  </div>
  ```

- **Tab Trigger (`rx.tabs.triggers`)**:
  ```html
  <button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-surface rt-Button w-32 justify-between" data-accent-color="tomato">
    <p class="rt-Text font-small">Account</p>
    <svg aria-hidden="true" class="rt-SelectIcon" fill="currentcolor" height="9" viewBox="0 0 9 9" width="9">
      <!-- Icon path -->
    </svg>
  </button>
  ```

### Interactive Components

- **Color Scheme**:
  - Customizable color schemes are provided, such as `tomato`, `red`, etc.
  - Color can be dynamically changed using a picker or predefined options.

- **Disabled State**:
  - A boolean property to disable the tab button if needed.

- **Value Property**:
  - Represents the unique identifier for each tab, used internally for switching logic.

### Event Handling

- The system supports event triggers that allow you to handle actions like switching between tabs.
- These events can be custom-defined and handled in your Reflex UI application logic.

### Conclusion

The provided documentation offers a comprehensive set of props and components necessary to build a functional tabbed interface with dynamic content. It includes interactive elements, customizable styling options, and event handling capabilities.

If you need further specific details or examples on any part of this system, feel free to ask!

# Disable

We use the `disabled` prop to disable the tab.

## Tab List

Tab 1
Tab 2
**Tab 3 (Disabled)**

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
        rx.tabs.trigger("Tab 3", value="tab3", disabled=True),
    ),
)
```

![](https://reflex.dev/docs/library/disclosure/tabs/#tabs-content)

# Tabs Content

Contains the content associated with each trigger.

[Styling](https://reflex.dev/docs/library/disclosure/tabs/#styling)

# Styling

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/disclosure/tabs/#value">

# Value

We use the `value` prop to assign a unique value that associates the content with a trigger.

```python
rx.tabs.root(
    rx.tabs.list(
        rx.tabs.trigger("Tab 1", value="tab1"),
        rx.tabs.trigger("Tab 2", value="tab2"),
    ),
    rx.tabs.content(rx.text("item on tab 1"), value="tab1"),
    rx.tabs.content(rx.text("item on tab 2"), value="tab2"),
    default_value="tab1",
    orientation="vertical",
)
```

Learn more about this in the [Reflex.dev documentation](https://reflex.dev/docs/library/disclosure/tabs/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/disclosure/tabs/#rx.tabs.root)

# rx.tabs.root
Set of content sections to be displayed one at a time.

## Tabs

- **Account**
- **Documents**
- **Settings**

## Properties

- `default_value`: str
- `value`: str
- `orientation`: "vertical" | "horizontal"
- `dir`: "ltr" | "rtl"
- `activation_mode`: "automatic" | "manual"

Each property is interactive.

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.tabs.list

Contains the triggers that sit alongside the active content.

## Account
- **Prop**: size
  - Type | Values: "1" | "2"
  - Default: 
  - Interactive: 

- **Prop**: loop
  - Type | Values: bool
  - Default: 
  - Interactive: false

## Documents
- **Prop**: size
  - Type | Values: "1" | "2"
  - Default: 
  - Interactive: 

- **Prop**: loop
  - Type | Values: bool
  - Default: 
  - Interactive: false

## Settings
- **Prop**: size
  - Type | Values: "1" | "2"
  - Default: 
  - Interactive: 

- **Prop**: loop
  - Type | Values: bool
  - Default: 
  - Interactive: false

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.tabs.trigger

The button that activates its associated content.

## Account Settings

*Prop: value*
Type: str
Default: 
Interactive: 

*Prop: disabled*
Type: bool
Default: 
Interactive: 
- False

*Prop: color_scheme*
Type: "tomato" | "red" | ...
Default: 
Interactive: 
- Tomato

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.tabs.content

Contains the content associated with each trigger.

## Account, Documents, Settings

### Account
- **Prop:** value
- **Type | Values:** str
- **Default:** None
- **Interactive:** No

### Documents
- **Prop:** value
- **Type | Values:** str
- **Default:** None
- **Interactive:** No

### Settings
- **Prop:** value
- **Type | Values:** str
- **Default:** None
- **Interactive:** No

- **Prop:** force_mount
- **Type | Values:** bool
- **Default:** None
- **Interactive:** 
  - false

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)