# Rendering Iterables

Recall again from the [basics](/docs/getting-started/basics/) that we cannot use Python `for` loops when referencing state vars in Reflex. Instead, use the `rx.foreach` component to render components from a collection of data.

Three buttons are displayed below:

- Red
- Green
- Blue

```python
class IterState(rx.State):
    color: list[str] = ["red", "green", "blue"]

def colored_box(color: str):
    return rx.button(color, background_color=color)

def dynamic_buttons():
    return rx.vstack(
        rx.foreach(IterState.color, colored_box),
    )
```

Here's the same example using a lambda function.

```python
def dynamic_buttons():
    return rx.vstack(
        rx.foreach(
            IterState.color,
            lambda color: colored_box(color),
        ),
    )
```

You can also use lambda functions directly with components without defining a separate function.

```python
def dynamic_buttons():
    return rx.vstack(
        rx.foreach(
            IterState.color,
            lambda color: rx.button(
                color, background_color=color
            ),
        ),
    )
```

In this first simple example we iterate through a `list` of colors and render a dynamic number of buttons.

The first argument of the `rx.foreach` function is the state var that you want to iterate through. The second argument is a function that takes in an item from the data and returns a component. In this case, the `colored_box` function takes in a color and returns a button with that color.

[Back to Components & Rendering Iterables](https://reflex.dev/docs/components/rendering-iterables/#for-vs-foreach)

# For vs Foreach

<div class="rt-Box css-1r9jlsz"><div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"><div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-7r3j43">

# Regular For Loop
Use when iterating over constants.

Thank you for providing this detailed explanation on using `foreach` in Reflex to render lists and iterables. Let's break down the key points and provide a summary of how to use `foreach` effectively with different data structures.

### Key Points:

1. **Rendering Simple Lists**:
   - Use `foreach` to iterate over simple lists like integers or strings.
   ```python
   return rx.foreach(range(5), lambda i: rx.text(f"Item {i}"))
   ```

2. **Rendering Dictionaries and Named Tuples**:
   - Use `foreach` with a dictionary where the keys and values are rendered separately.
   ```python
   from typing import NamedTuple

   @dataclasses.dataclass
   class Item(NamedTuple):
       name: str
       quantity: int

   items = [Item("Apple", 5), Item("Banana", 3)]
   
   return rx.foreach(items, lambda item: rx.text(f"{item.name} x{item.quantity}"))
   ```

3. **Rendering Nested Data Structures**:
   - Use `foreach` to handle nested lists or dictionaries.
   ```python
   from typing import List

   class ColorChart(NamedTuple):
       primary_color: str
       secondary_colors: List[str]

   color_chart = [
       ColorChart("purple", ["red", "blue"]),
       ColorChart("orange", ["yellow", "red"]),
       ColorChart("green", ["blue", "yellow"])
   ]

   def display_colors(color: Tuple[str, List[str]]):
       return rx.vstack(
           rx.text(color[0], color=color[0]),
           rx.hstack(*[rx.box(rx.text(c), bg=c) for c in color[1]])
       )

   return rx.foreach(color_chart, display_colors)
   ```

4. **Using `foreach` with `cond`**:
   - Use conditional rendering within a `foreach`.
   ```python
   from typing import List

   class Item:
       def __init__(self, name: str, is_packed: bool):
           self.name = name
           self.is_packed = is_packed

   items = [Item("Space suit", True), Item("Helmet", True), Item("Back Pack", False)]

   def render_item(item: rx.Var[Item]):
       return rx.cond(
           item.is_packed,
           rx.list.item(f"{item.name} ✔"),
           rx.list.item(item.name)
       )

   return rx.vstack(
       rx.text("Sammy's Packing List"),
       rx.list(*[render_item(i) for i in items])
   )
   ```

### Summary:

- **Simplicity**: `foreach` is straightforward and easy to use for rendering lists.
- **Flexibility**: It can handle simple, complex, nested data structures, and even dictionaries with custom rendering logic.
- **Conditional Rendering**: Combine `foreach` with `cond` for more dynamic rendering.

These examples should help you effectively utilize the `foreach` function in Reflex to render various types of iterables and lists. If you have any specific scenarios or questions, feel free to ask!

# Regular For Loop
Use when iterating over constants.

# Foreach

Use when iterating over state vars.

The above example could have been written using a regular Python `for` loop, since the data is constant.

However, as soon as you need the data to be dynamic, you must use `rx.foreach`.

## Static Buttons

- red
- green
- blue

## Dynamic Buttons Using `rx.foreach`

- red
- green
- blue

### Add a Color

Add a color: [Add]

```python
class DynamicIterState(rx.State):
    color: list[str] = ["red", "green", "blue"]

    def add_color(self, form_data):
        self.color.append(form_data["color"])

def dynamic_buttons_foreach():
    return rx.vstack(
        rx.foreach(DynamicIterState.color, colored_box),
        rx.form(
            rx.input(name="color", placeholder="Add a color"),
            rx.button("Add"),
            on_submit=DynamicIterState.add_color,
        ),
    )
```

[Documentation](https://reflex.dev/docs/components/rendering-iterables/#render-function)

# Render Function

The function to render each item can be defined either as a separate function or as a lambda function. In the example below, we define the function `colored_box` separately and pass it to the `rx.foreach` function.

```python
class IterState2(rx.State):
    color: list[str] = ["red", "green", "blue"]

def colored_box(color: rx.Var[str]):
    return rx.button(color, background_color=color)

def dynamic_buttons2():
    return rx.vstack(
        rx.foreach(IterState2.color, colored_box),
    )
```

Notice that the type annotation for the `color` parameter in the `colored_box` function is `rx.Var[str]` (rather than just `str`). This is because the `rx.foreach` function passes the item as a `Var` object, which is a wrapper around the actual value. This is what allows us to compile the frontend without knowing the actual value of the state var (which is only known at runtime).

[Read more about rendering iterables in Reflex](https://reflex.dev/docs/components/rendering-iterables/#enumerating-iterables)

# Enumerating Iterables

The function can also take an index as a second argument, meaning that we can enumerate through data as shown in the example below.

1. red
2. green
3. blue

```python
class IterIndexState(rx.State):
    color: list[str] = ["red", "green", "blue"]

def create_button(color: rx.Var[str], index: int):
    return rx.box(
        rx.button(f"{index + 1}. {color}", padding_y="0.5em"),
    )

def enumerate_foreach():
    return rx.vstack(rx.foreach(IterIndexState.color, create_button))
```

Here's the same example using a lambda function.

```python
def enumerate_foreach():
    return rx.vstack(
        rx.foreach(
            IterIndexState.color,
            lambda color, index: create_button(color, index),
        ),
    )
```

[More on Rendering Iterables](https://reflex.dev/docs/components/rendering-iterables/#iterating-dictionaries)

# Iterating Dictionaries

We can iterate through a `dict` using a `foreach`. When the dict is passed through to the function that renders each item, it is presented as a list of key-value pairs `[("sky", "blue"), ("balloon", "red"), ("grass", "green")]`.

## Example Code

```python
class SimpleDictIterState(rx.State):
    color_chart: dict[str, str] = {
        "sky": "blue",
        "balloon": "red",
        "grass": "green",
    }

def display_color(color: list):
    # color is presented as a list key-value pairs [("sky", "blue"), ("balloon", "red"), ("grass", "green")]
    return rx.box(rx.text(color[0]), bg=color[1], padding_x="1.5em")

def dict_foreach():
    return rx.grid(
        rx.foreach(
            SimpleDictIterState.color_chart,
            display_color,
        ),
        columns="3",
    )
```

The example code defines a dictionary `color_chart` and uses the `rx.foreach` function to iterate over it, rendering each key-value pair as a colored text box.

# Dict Type Annotation.

## Nested Examples

[Link to Nested Examples](https://reflex.dev/docs/components/rendering-iterables/#nested-examples)

# Nested examples

`rx.foreach` can be used with nested state vars. Here we use nested `foreach` components to render the nested state vars. The `rx.foreach(project["technologies"], get_badge)` inside of the `project_item` function, renders the `dict` values which are of type `list`. The `rx.box(rx.foreach(NestedStateFE.projects, project_item))` inside of the `projects_example` function renders each `dict` inside of the overall state var `projects`.

```python
class NestedStateFE(rx.State):
    projects: list[dict[str, list[str]]] = [
        {
            "technologies": ["Next.js", "Prisma", "Tailwind", "Google Cloud", "Docker", "MySQL"],
        },
        {
            "technologies": ["Python", "Flask", "Google Cloud", "Docker"],
        },
    ]

def get_badge(technology: rx.Var[str]) -> rx.Component:
    return rx.badge(
        technology, variant="soft", color_scheme="green"
    )

def project_item(project: rx.Var[dict[str, list[str]]]) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.foreach(project["technologies"], get_badge)
        ),
    )

def projects_example() -> rx.Component:
    return rx.box(
        rx.foreach(NestedStateFE.projects, project_item)
    )
```

If you want an example where not all of the values in the dict are the same type then check out the example on [var operations using foreach](/docs/vars/var-operations/).

Here is a further example of how to use `foreach` with a nested data structure.

```python
class NestedDictIterState(rx.State):
    color_chart: dict[str, list[str]] = {
        "purple": ["red", "blue"],
        "orange": ["yellow", "red"],
        "green": ["blue", "yellow"],
    }

def display_colors(color: rx.Var[tuple[str, list[str]]) -> rx.Component:
    return rx.vstack(
        rx.text(color[0], color=color[0]),
        rx.hstack(
            rx.foreach(
                color[1],
                lambda x: rx.box(rx.text(x, color="black"), bg=x),
            ),
        ),
    )

def nested_dict_foreach() -> rx.Component:
    return rx.grid(
        rx.foreach(
            NestedDictIterState.color_chart,
            display_colors,
        ),
        columns="3",
    )
```

For more details on using `foreach` with cond, you can refer to the documentation [here](https://reflex.dev/docs/components/rendering-iterables/#foreach-with-cond).

# Foreach with Cond

We can also use `foreach` with the `cond` component.

In this example we define the function `render_item`. This function takes in an `item`, uses the `cond` to check if the item `is_packed`. If it is packed it returns the `item_name` with a `✔` next to it, and if not then it just returns the `item_name`. We use the `foreach` to iterate over all of the items in the `to_do_list` using the `render_item` function.

Sammy's Packing List
- Space suit ✔
- Helmet ✔
- Back Pack

```python
import dataclasses


@dataclasses.dataclass
class ToDoListItem:
    item_name: str
    is_packed: bool


class ForeachCondState(rx.State):
    to_do_list = [
        ToDoListItem(item_name="Space suit", is_packed=True),
        ToDoListItem(item_name="Helmet", is_packed=True),
        ToDoListItem(item_name="Back Pack", is_packed=False),
    ]


def render_item(item: rx.Var[ToDoListItem]):
    return rx.cond(
        item.is_packed,
        rx.list.item(item.item_name + " ✔"),
        rx.list.item(item.item_name),
    )


def packing_list():
    return rx.vstack(
        rx.text("Sammy's Packing List"),
        rx.list(
            rx.foreach(ForeachCondState.to_do_list, render_item)
        ),
    )
```