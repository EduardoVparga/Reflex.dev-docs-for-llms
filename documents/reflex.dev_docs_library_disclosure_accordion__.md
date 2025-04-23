# Accordion

An accordion is a vertically stacked set of interactive headings that each reveal an associated section of content.
The accordion component is made up of `accordion`, which is the root of the component and takes in an `accordion.item`,
which contains all the contents of the collapsible section.

[Basic Example](https://reflex.dev/docs/library/disclosure/accordion/#basic-example)

# Basic Example

## Basic Example

### Basic Example

- Item 1
- Item 2
- Item 3

```python
# Python code example
def hello_world():
    print("Hello, world!")
```

- Item 4
- Item 5
- Item 6

# First Item

This is a collapsible content area. Currently, it is closed.

### Second Item
<button aria-controls="radix-:R3a8l6kml6:" aria-expanded="false">Second Item<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg></button>
<div aria-labelledby="radix-:R1a8l6kml6:" class="AccordionContent css-rz4evu" data-orientation="vertical" data-state="closed" hidden="" id="radix-:R3a8l6kml6:" role="region" style="--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);"></div>
</div>

Third item
- The third accordion item's content

First Item
- The first accordion item's content

Second Item
- The second accordion item's content

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
    ),
    width="300px"
)
```

Based on the provided documentation, here is a summary and explanation for the `Accordion` component:

### Overview

The `Accordion` component in Reflex UI allows you to create expandable sections where only one section can be expanded at a time. It provides an interactive way to manage multiple content sections that are shown or hidden based on user interaction.

### Properties

1. **value**: 
   - **Type**: `str`
   - **Description**: The value associated with the currently active accordion item.
   
2. **disabled**:
   - **Type**: `bool`
   - **Default**: `False`
   - **Description**: Whether the accordion header should be disabled.

3. **header**:
   - **Type**: `Union[Component, str]`
   - **Description**: The component or text to display as the header of the accordion item.
   
4. **content**:
   - **Type**: `Union[Component, str, NoneType]`
   - **Default**: `None`
   - **Description**: The content that is shown when the accordion is expanded. If set to `None`, no content will be displayed.

5. **color_scheme**:
   - **Type**: `"tomato" | "red" | ...`
   - **Description**: Customizes the color scheme of the accordion, which can include predefined colors or custom palette options.
   
6. **variant**:
   - **Type**: `"classic" | "soft" | ...`
   - **Description**: Determines the visual style of the accordion.

7. **as_child**:
   - **Type**: `bool`
   - **Default**: `False`
   - **Description**: Indicates whether the component should be rendered as a child of another component, affecting its layout and styling.

### Interactive Elements

- The accordion headers are interactive components that can be clicked to toggle the visibility of their associated content.
- The headers include an expand/collapse icon (`<svg>` element) that visually indicates the state (expanded or collapsed).

### Valid Children

The `Accordion` component expects one or more of these valid children:
- **AccordionHeader**: Defines the header text or component for each accordion item.
- **AccordionTrigger**: A clickable area within the header to toggle visibility.
- **AccordionContent**: The content that is shown when the accordion is expanded.

### Example Usage

Here's a basic example of using the `Accordion` component:

```python
import reflex as rx

def index():
    return rx.accordion(
        # First Accordion Item
        rx.accordion_item(
            rx.accordion_button("Item 1"),
            rx.accordion_panel(rx.text("Content for item 1")),
        ),
        # Second Accordion Item
        rx.accordion_item(
            rx.accordion_button("Item 2"),
            rx.accordion_panel(rx.text("Content for item 2")),
        ),
    )
```

### Event Triggers

- **value**: Changes when the user toggles an accordion item.
- Users can see and interact with these events via Reflex's event handling mechanisms.

This structure allows you to manage a flexible number of expandable sections within your application, providing a clean and interactive way for users to access content.

# Type

We use the `type` prop to determine whether multiple items can be opened at once. The allowed values for this prop are `single` and `multiple` where `single` will only open one item at a time. The default value for this prop is `single`.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div data-orientation="vertical" data-variant="classic">
      <div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>
    </div>
  </div>
</div>

# First Item

<button aria-controls="radix-:R36956kml6:" aria-expanded="false">First Item<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg></button>

## Content

This content is hidden and will be shown when the button is expanded.

Second Item<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="m6 9 6 6 6-6"></path></svg>

### Third item

The third accordion item's content

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content"
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content"
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content"
    ),
    collapsible=True,
    width="300px",
    type="multiple"
)
```

[Link](https://reflex.dev/docs/library/disclosure/accordion/#default-value)

# Default Value

We use the `default_value` prop to specify which item should open by default. The value for this prop should be any of the unique values set by an `accordion.item`.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-row rt-r-gap-2">
      <div data-orientation="vertical" data-variant="classic">
        <div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>
      </div>
    </div>
  </div>
</div>

# First Item

---

## Notes

This item is currently open.

Second Item

The second accordion item's content

# Third item

The third accordion item's content

```python
rx.flex(
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content",
            value="item_1",
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content",
            value="item_2",
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content",
            value="item_3",
        ),
        width="300px",
        default_value="item_2",
    ),
    direction="row",
    spacing="2",
)
```

![Copy Code](https://reflex.dev/docs/library/disclosure/accordion/#collapsible)

# Collapsible

We use the `collapsible` prop to allow all items to close. If set to `False`, an opened item cannot be closed.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-row rt-r-gap-2">
      <div data-orientation="vertical" data-variant="classic">
        <div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>
      </div>
    </div>
  </div>
</div>

# First Item

--- 

## Additional Content
This section is currently hidden.

# Second Item

Second Item

# Third item

##Markdown Content Ends Here##

First Item

Second Item

# Second Item

Second Item

### Third item

The third accordion item's content

```python
rx.flex(
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=True,
        width="300px",
    ),
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=False,
        width="300px",
    ),
    direction="row",
    spacing="2",
)
```

<a href="https://reflex.dev/docs/library/disclosure/accordion/#disable" class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts">Disable</a>

The provided HTML snippet is a detailed documentation for an accordion component in Reflex, likely part of a UI library. Here's a summary and key points from this documentation:

### Accordion Component

#### Props Summary:
1. **value**:
   - Type: `str`
   - Description: The value that determines the currently active item.

2. **disabled**:
   - Type: `bool`
   - Default Value: `False`
   - Interactive: Check if you can interact with it (checkbox).

3. **header**:
   - Type: `Union[Component, str]`
   - Description: The header of the accordion item.

4. **content**:
   - Type: `Union[Component, str, NoneType]`
   - Default Value: `None` (Var.create(None))
   - Description: The content that is shown when the item is active.

5. **color_scheme**:
   - Type: `"tomato" | "red" | ...`
   - Description: Customizes the color scheme of the component.
   - Interactive: Dropdown to select a color.

6. **variant**:
   - Type: `"classic" | "soft" | ...`
   - Description: Changes the style variant of the accordion item.
   - Interactive: Dropdown to select a variant.

7. **as_child**:
   - Type: `bool`
   - Default Value: Not specified
   - Description: Whether to use this as a child component or not (checkbox).

#### Valid Children:
- `AccordionHeader`: Used for defining the header of each accordion item.
- `AccordionTrigger`: Used within headers for interactive elements.
- `AccordionContent`: The content that is shown when an accordion item is expanded.

### Event Triggers
The documentation also mentions event triggers, which can be accessed from [here](https://reflex.dev/docs/api-reference/event-triggers/).

### Example Usage:
Here's a simple example of how you might use the `Accordion` component:

```python
from reflex import App, create_state, State, component, html

class State(State):
    value: str = "first"

def first_accordion():
    return html.Accordion(
        header="First Item",
        content="This is the first item's content.",
        value=State.value,
    )

def second_accordion():
    return html.Accordion(
        header="Second Item",
        content="This is the second item's content.",
        value=State.value,
    )

def app():
    return html.Div([
        first_accordion(),
        second_accordion(),
    ])

# Create an app
App(state=State, component=app)
```

### Notes:
- The `value` prop should be used to control which accordion item is active.
- Use `header`, `content`, and other props as needed to customize each accordion item.
- The color scheme and variant can be customized using the provided dropdowns.

This documentation provides a comprehensive overview of how to use the Accordion component in Reflex, including its properties, children components, and event triggers.

### First Item

This item is currently closed.

### Second Item

This is a placeholder for the content that will be shown when the item is expanded.

### Third item
The third accordion item's content

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
    ),
    collapsible=True,
    width="300px",
    disabled=True,
)
```

For more information, see [Orientation](https://reflex.dev/docs/library/disclosure/accordion/#orientation)

# Orientation

We use `orientation` prop to set the orientation of the accordion to `vertical` or `horizontal`. By default, the orientation will be set to `vertical`. Note that, the orientation prop won't change the visual orientation but the functional orientation of the accordion. This means that for vertical orientation, the up and down arrow keys moves focus between the next or previous item, while for horizontal orientation, the left or right arrow keys moves focus between items.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div data-orientation="vertical" data-variant="classic">
            <div data-orientation="vertical" data-state="closed"></div>
        </div>
    </div>
</div>

First Item

Second Item

Second Item
----------

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
    ),
    collapsible=True,
    width="300px",
    orientation="vertical",
)
```

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div data-orientation="horizontal" data-variant="classic">
      <div class="AccordionItem css-6nv1z3" data-orientation="horizontal" data-state="closed">
        <!-- Content will be rendered here -->
      </div>
    </div>
  </div>
</div>

First Item
  -

Second Item<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="m6 9 6 6 6-6"></path></svg>

Second Item

Third item
- The third accordion item's content

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
    ),
    collapsible=True,
    width="300px",
    orientation="horizontal",
)
```

[View Documentation](https://reflex.dev/docs/library/disclosure/accordion/#variant)

# Variant

## Python Code Example

```python
# Example Python code
print("Hello, World!")
```

<div class="rt-Flex rt-r-fd-row rt-r-gap-2">
<div class="css-4oibea" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed">
```

# First Item

##

### Second Item
Second Item

Third item

<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="m6 9 6 6 6-6"></path></svg>

---

<python code example>
```python
# Python code example
print("Hello, World!")
```
```

### First Item

This is a collapsible item. Click to expand or collapse the content.

<div aria-labelledby="radix-:R9ib16kml6:" class="AccordionContent css-rz4evu" data-orientation="vertical" data-state="closed" hidden="" id="radix-:Rpib16kml6:" role="region" style="--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);"></div>

# Second Item

Second Item

# Third item

<div aria-labelledby="radix-:Rbib16kml6:" class="AccordionContent css-rz4evu" data-orientation="vertical" data-state="closed" hidden="" id="radix-:Rrib16kml6:" role="region" style="--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);"></div>

<div class="css-4oibea" data-orientation="vertical" data-variant="outline">
    <div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed">

### First Item

First Item

# Second Item

Second Item

# Third item

This is the content of the third item. It is hidden by default.

# First Item

## Content
This content is currently hidden.

# Second Item

Second Item

Third item<button aria-controls="radix-:Rrkb16kml6:" aria-expanded="false" type="button">Third item<svg class="lucide lucide-chevron-down AccordionChevron" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg></button>

<div aria-labelledby="radix-:Rbkb16kml6:" role="region" hidden="">
</div>
</div>

# First Item

## Content Here
(No content provided in the HTML)

# Second Item

Second Item

```python
rx.flex(
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=True,
        variant="classic"
    ),
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=True,
        variant="soft"
    ),
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=True,
        variant="outline"
    ),
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=True,
        variant="surface"
    ),
    rx.accordion.root(
        rx.accordion.item(
            header="First Item",
            content="The first accordion item's content"
        ),
        rx.accordion.item(
            header="Second Item",
            content="The second accordion item's content"
        ),
        rx.accordion.item(
            header="Third item",
            content="The third accordion item's content"
        ),
        collapsible=True,
        variant="ghost"
    ),
    direction="row",
    spacing="2"
)
```

# Color Scheme

We use the `color_scheme` prop to assign a specific color to the accordion background, ignoring the global theme.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-row rt-r-gap-2">
      <div data-accent-color="grass" data-orientation="vertical" data-variant="classic">
        <div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>
      </div>
    </div>
  </div>
</div>

First Item

---

Second Item

<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="m6 9 6 6 6-6"></path></svg>

<div aria-labelledby="radix-:R59bd6kml6:" class="AccordionContent css-rz4evu" data-orientation="vertical" data-state="closed" hidden="" id="radix-:Rd9bd6kml6:" role="region" style="--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);"></div>

<div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed">

# Third item

Third item

# First Item

##

# Second Item

Second Item

Third item
The third accordion item's content

First Item
The first accordion item's content

Second Item
The second accordion item's content

```python
rx.flex(
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(header="Second Item", content="The second accordion item's content"),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        width="300px",
        color_scheme="grass",
    ),
    rx.accordion.root(
        rx.accordion.item(header="First Item", content="The first accordion item's content"),
        rx.accordion.item(header="Second Item", content="The second accordion item's content"),
        rx.accordion.item(header="Third item", content="The third accordion item's content"),
        collapsible=True,
        width="300px",
        color_scheme="green",
    ),
    direction="row",
    spacing="2",
)
```

[Link](https://reflex.dev/docs/library/disclosure/accordion/#value)

The provided content is a detailed documentation for a component in a web or software application, likely built using Reflex (or a similar framework). The component being described is an `Accordion`, which is a UI element that allows users to toggle the visibility of content by clicking on a header.

### Key Points:

1. **Accordion Component**:
   - **Purpose**: Allows users to expand and collapse content sections.
   - **Usage Example**: 
     ```python
     from reflex import types as t

     Accordion(
         value="item2",
         disabled=False,
         header="Item 1 Header",
         content="This is the content for item 1.",
         color_scheme="tomato",
         variant="classic"
     )
     ```

2. **Props**:
   - **value**: A string that determines which accordion item is expanded by default.
   - **disabled**: A boolean indicating whether the accordion can be interacted with.
   - **header**: The content of the accordion header, which can be either a string or a component.
   - **content**: The content to display when the accordion is open. Can also be a string or `None`.
   - **color_scheme**: A color for styling, with options like "tomato", "red", etc.
   - **variant**: Different styles or variants of the accordion (e.g., "classic", "soft").
   - **as_child**: A boolean indicating whether to render the component as a child.

3. **Valid Children**:
   - `AccordionHeader`: The header content.
   - `AccordionTrigger`: The interactive part that toggles the accordion.
   - `AccordionContent`: The content that expands or collapses.

4. **Event Triggers**:
   - No specific event triggers are listed, but common events like toggle might be available.

### Example Usage:

Here's an example of how you might use the `Accordion` component in Reflex:

```python
from reflex import types as t

# Define a simple header and content function
def accordion_header():
    return "Item 1 Header"

def accordion_content():
    return "This is the content for item 1."

# Use the Accordion component
accordion = Accordion(
    value="item2",  # Default open to 'item2'
    disabled=False,
    header=accordion_header,  # Using a function as the header
    content=Var.create(accordion_content),  # Content is created dynamically
    color_scheme="tomato",
    variant="classic"
)

print(accordion)
```

### Summary:
- The `Accordion` component in this documentation allows for creating expandable and collapsible sections.
- It provides options to customize the appearance, behavior, and content of these sections.
- Valid children include components that define the header, trigger mechanism, and content.

This documentation is useful for developers who need to integrate accordion functionality into their web or software applications using Reflex.

# Is it accessible?
Test button

<div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>

Is it unstyled?

<button aria-controls="radix-:R6labp6kml6:" aria-expanded="false" type="button">Is it unstyled?<svg class="lucide lucide-chevron-down AccordionChevron css-svt5ra" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg></button>

<div aria-labelledby="radix-:R2labp6kml6:" data-orientation="vertical" data-state="closed" hidden="" id="radix-:R6labp6kml6:" role="region"></div>
<div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed">

# Is it finished?
It's still in beta, but it's ready to use in production.

---

## Is it accessible?
Test button

---

## Is it unstyled?
Yes. It's unstyled by default, giving you freedom over the look and feel.

---

The app state is:
```python
class AccordionState(rx.State):
    """The app state."""
    
    value: str = "item_1"
    item_selected: str
    
    @rx.event
    def change_value(self, value):
        self.value = value
        self.item_selected = f"{value} selected"

def index() -> rx.Component:
    return rx.theme(
        rx.container(
            rx.text(AccordionState.item_selected),
            rx.flex(
                rx.accordion.root(
                    rx.accordion.item(
                        header="Is it accessible?",
                        content=rx.button("Test button"),
                        value="item_1",
                    ),
                    rx.accordion.item(
                        header="Is it unstyled?",
                        content="Yes. It's unstyled by default, giving you freedom over the look and feel.",
                        value="item_2",
                    ),
                    rx.accordion.item(
                        header="Is it finished?",
                        content="It's still in beta, but it's ready to use in production.",
                        value="item_3",
                    ),
                    collapsible=True,
                    width="300px",
                    value=AccordionState.value,
                    on_value_change=lambda value: AccordionState.change_value(value),
                ),
                direction="column",
                spacing="2",
            ),
            padding="2em",
            text_align="center",
        )
    )
```

# AccordionItem

The accordion item contains all the parts of a collapsible section.

[Learn more](https://reflex.dev/docs/library/disclosure/accordion/#styling)

# Styling

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/disclosure/accordion/#value">

# Value

## Python Code Example
```python
# This is a placeholder for the actual python code example
```

## Nested Box
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
  <div data-orientation="vertical" data-variant="classic">
    <div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>
  </div>
</div>

First Item
  -

Second Item[.Second Item](#)
---

### Third item

The third accordion item's content

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
        value="item_1",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
        value="item_2",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
        value="item_3",
    ),
    collapsible=True,
    width="300px",
)
```

![Copy Code](/lucide/copy.svg)

# Disable

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div data-accent-color="blue" data-orientation="vertical" data-variant="classic">
      <div data-disabled="" data-orientation="vertical" data-state="closed"></div>
    </div>
  </div>
</div>

First Item

This item is closed.

# Second Item

Second Item

### Third Item

<svg class="lucide lucide-chevron-down AccordionChevron" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24"></svg>

```python
rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
        disabled=True,
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
    ),
    collapsible=True,
    width="300px",
    color_scheme="blue",
)
```

[Reflex Dev Docs](https://reflex.dev/docs/library/disclosure/accordion/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/disclosure/accordion/#rx.accordion.root)

# rx.accordion.root
An accordion component.

<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="css-1g0rqxq" data-accent-color="tomato" data-orientation="vertical" data-radius="none" data-variant="classic">
<div class="AccordionItem css-6nv1z3" data-orientation="vertical" data-state="closed"></div>
</div>

# First Item

## Content Placeholder

### Second Item
Second Item

### Third item

<svg class="lucide lucide-chevron-down AccordionChevron" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24">...</svg>

---

- **Prop**: type
  - **Type | Values**: "single" | "multiple"
  - **Default**: None
  - **Interactive**: 
    - <button>single</button>

- **Prop**: value
  - **Type | Values**: Union[str, Sequence]
  - **Default**: None

- **Prop**: default_value
  - **Type | Values**: Union[str, Sequence]
  - **Default**: None

- **Prop**: collapsible
  - **Type | Values**: bool
  - **Default**: 
    - <label><button>false</button></label>

- **Prop**: disabled
  - **Type | Values**: bool
  - **Default**: 
    - <label><button>false</button></label>

- **Prop**: dir
  - **Type | Values**: "ltr" | "rtl"
  - **Default**: 
    - <button>ltr</button>

- **Prop**: orientation
  - **Type | Values**: "vertical" | "horizontal"
  - **Default**: 
    - <button>vertical</button>

- **Prop**: radius
  - **Type | Values**: "none" | "small" | ...
  - **Default**: 
    - <button>none</button>

- **Prop**: duration
  - **Type | Values**: int
  - **Default**: LiteralVar.create(DEFAULT_ANIMATION_DURATION)

- **Prop**: easing
  - **Type | Values**: str
  - **Default**: LiteralVar.create(DEFAULT_ANIMATION_EASING)

- **Prop**: show_dividers
  - **Type | Values**: bool
  - **Default**: 
    - <label><button>false</button></label>

- **Prop**: color_scheme
  - **Type | Values**: "tomato" | "red" | ... or <svg class="lucide lucide-palette">...</svg>
  - **Default**: 
    - <div>
      <button>tomato</button>
    </div>

- **Prop**: variant
  - **Type | Values**: "classic" | "soft" | ...
  - **Default**: 
    - <button>classic</button>

- **Prop**: as_child
  - **Type | Values**: bool
  - **Default**: None

# Valid Children
- AccordionHeader
- AccordionTrigger
- AccordionContent

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.accordion.item

An accordion component.

<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">

<div class="AccordionItem css-6nv1z3" colorscheme="tomato" data-accent-color="tomato" data-orientation="vertical" data-state="closed" data-variant="classic" variant="classic"></div>

</div>

# First Item

## Content Placeholder

# Second Item

Second Item

# Third item

*Prop* | *Type | Values* | *Default* | *Interactive*
---|---|---|---
value | str |  | 
disabled | bool |  | <label> false </label>
header | Union[Component, str] |  | 
content | Union[Component, str, NoneType] | Var.create(None) | 
color_scheme | "tomato" | "red" | ... | tomato
variant | "classic" | "soft" | ... | classic
as_child | bool |  |

# Valid Children
- AccordionHeader
- AccordionTrigger
- AccordionContent

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)