# Var Operations

Var operations transform the placeholder representation of the value on the frontend and provide a way to perform basic operations on the Var without having to define a computed var.

Within your frontend components, you cannot use arbitrary Python functions on the state vars. For example, the following code will **not work**.

```python
class State(rx.State):
    number: int

def index():
    # This will be compiled before runtime, before `State.number` has a known value.
    # Since `float` is not a valid var operation, this will throw an error.
    rx.text(float(State.number))
```

This is because we compile the frontend to Javascript, but the value of `State.number` is only known at runtime.

In this example below we use a var operation to concatenate a `string` with a `var`, meaning we do not have to do in within state as a computed var.

# I just bought a bunch of DOGE

DOGE is going to the moon!

coins = ["BTC", "ETH", "LTC", "DOGE"]

class VarSelectState(rx.State):
    selected: str = "DOGE"

def var_operations_example():
    return rx.vstack(
        # Using a var operation to concatenate a string with a var.
        rx.heading("I just bought a bunch of " + VarSelectState.selected),
        # Using an f-string to interpolate a var.
        rx.text(f"{VarSelectState.selected} is going to the moon!"),
        rx.select(coins, value=VarSelectState.selected, on_change=VarSelectState.set_selected),
    )

# Vars support many common operations.

# Supported Operations

Var operations allow us to change vars on the front-end without having to create more computed vars on the back-end in the state.

Some simple examples are the `==` var operator, which is used to check if two vars are equal and the `to_string()` var operator, which is used to convert a var to a string.

Apple is my favorite fruit!
The selected fruit is not equal to the favorite fruit.

```python
fruits = ["Apple", "Banana", "Orange", "Mango"]
class EqualsState(rx.State):
    selected: str = "Apple"
    favorite: str = "Banana"

def var_equals_example():
    return rx.vstack(
        rx.text(EqualsState.favorite.to_string() + "is my favorite fruit!"),
        rx.select(fruits, value=EqualsState.selected, on_change=EqualsState.set_selected),
        rx.cond(
            EqualsState.selected == EqualsState.favorite,
            rx.text("The selected fruit is equal to the favorite fruit!"),
            rx.text("The selected fruit is not equal to the favorite fruit.")
        ),
    )
```

# Negate, Absolute and Length

The `-` operator is used to get the negative version of the var. The `abs()` operator is used to get the absolute value of the var. The `.length()` operator is used to get the length of a list var.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
            <!-- Content will be added here -->
        </div>
    </div>
</div>

# The number: 0

Negated:0
Absolute:0
Numbers seen:0

**Update**

```python
import random

class OperState(rx.State):
    number: int
    numbers_seen: list = []

    @rx.event
    def update(self):
        self.number = random.randint(-100, 100)
        self.numbers_seen.append(self.number)

def var_operation_example():
    return rx.vstack(
        rx.heading(f"The number: {OperState.number}", size="3"),
        rx.hstack(
            rx.text("Negated:", 
                    rx.badge(-OperState.number, variant="soft", color_scheme="green")),
            rx.text("Absolute:",
                    rx.badge(abs(OperState.number), variant="soft", color_scheme="blue")),
            rx.text(f"Numbers seen:",
                    rx.badge(len(OperState.numbers_seen()), variant="soft", color_scheme="red")),
        ),
        rx.button("Update", on_click=OperState.update),
    )
```

# Comparisons and Mathematical Operators

All of the comparison operators are used as expected in python. These include `==`, `!=`, `>`, `>=`, `<`, `<=`.

There are operators to add two vars `+`, subtract two vars `-`, multiply two vars `*` and raise a var to a power `pow()`.

```python
import random

class CompState(rx.State):
    number_1: int
    number_2: int

    @rx.event
    def update():
        self.number_1 = random.randint(-10, 10)
        self.number_2 = random.randint(-10, 10)

def var_comparison_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Integer 1"),
                    rx.table.column_header_cell("Integer 2"),
                    rx.table.column_header_cell("Operation"),
                    rx.table.column_header_cell("Outcome"),
                )
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 == Int 2"),
                    rx.table.cell(str(CompState.number_1 == CompState.number_2)),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 != Int 2"),
                    rx.table.cell(str(CompState.number_1 != CompState.number_2)),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 > Int 2"),
                    rx.table.cell(str(CompState.number_1 > CompState.number_2)),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 >= Int 2"),
                    rx.table.cell(str(CompState.number_1 >= CompState.number_2)),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 < Int 2 "),
                    rx.table.cell(str(CompState.number_1 < CompState.number_2)),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 <= Int 2"),
                    rx.table.cell(str(CompState.number_1 <= CompState.number_2)),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 + Int 2"),
                    rx.table.cell(f"{CompState.number_1 + CompState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 - Int 2"),
                    rx.table.cell(f"{CompState.number_1 - CompState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("Int 1 * Int 2"),
                    rx.table.cell(f"{CompState.number_1 * CompState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(CompState.number_1),
                    rx.table.cell(CompState.number_2),
                    rx.table.cell("pow(Int 1, Int2)"),
                    rx.table.cell(f"{pow(CompState.number_1, CompState.number_2)}"),
                ),
            ),
            width="100%",
        ),
        rx.button("Update", on_click=CompState.update),
    )
```

# True Division, Floor Division and Remainder

The operator `/` represents true division. The operator `//` represents floor division. The operator `%` represents the remainder of the division.

Integer 1 | Integer 2 | Operation | Outcome
--- | --- | --- | ---
3.5 | 1.4 | Int 1 / Int 2 | 2.5
3.5 | 1.4 | Int 1 // Int 2 | 2
3.5 | 1.4 | Int 1 % Int 2 | 0.7000000000000002

```python
import random

class DivState(rx.State):
    number_1: float = 3.5
    number_2: float = 1.4

    @rx.event
    def update(self):
        self.number_1 = round(random.uniform(5.1, 9.9), 2)
        self.number_2 = round(random.uniform(0.1, 4.9), 2)

def var_div_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Integer 1"),
                    rx.table.column_header_cell("Integer 2"),
                    rx.table.column_header_cell("Operation"),
                    rx.table.column_header_cell("Outcome"),
                )
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(DivState.number_1),
                    rx.table.cell(DivState.number_2),
                    rx.table.cell("Int 1 / Int 2"),
                    rx.table.cell(f"{DivState.number_1 / DivState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(DivState.number_1),
                    rx.table.cell(DivState.number_2),
                    rx.table.cell("Int 1 // Int 2"),
                    rx.table.cell(f"{DivState.number_1 // DivState.number_2}"),
                ),
                rx.table.row(
                    rx.table.row_header_cell(DivState.number_1),
                    rx.table.cell(DivState.number_2),
                    rx.table.cell("Int 1 % Int 2"),
                    rx.table.cell(f"{DivState.number_1 % DivState.number_2}"),
                ),
            ),
            width="100%",
        ),
        rx.button("Update", on_click=DivState.update),
    )
```

# And, Or and Not

In Reflex the `&` operator represents the logical AND when used in the front end. This means that it returns true only when both conditions are true simultaneously.
The `|` operator represents the logical OR when used in the front end. This means that it returns true when either one or both conditions are true.
The `~` operator is used to invert a var. It is used on a var of type `bool` and is equivalent to the `not` operator.

- Var 1: True
- Var 2: True

Operation: Logical AND (&)

Outcome: True

---

- Var 1: True
- Var 2: True

Operation: Logical OR (|)

Outcome: True

---

- Var 1: True
- Var 2: True

Operation: The invert of Var 1 (~)

Outcome: False

```python
import random

class LogicState(rx.State):
    var_1: bool = True
    var_2: bool = True

    @rx.event
    def update(self):
        self.var_1 = random.choice([True, False])
        self.var_2 = random.choice([True, False])

def var_logical_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Var 1"),
                    rx.table.column_header_cell("Var 2"),
                    rx.table.column_header_cell("Operation"),
                    rx.table.column_header_cell("Outcome")
                )
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell(LogicState.var_1.to_string()),
                    rx.table.cell(LogicState.var_2.to_string()),
                    rx.table.cell("Logical AND (&)"),
                    rx.table.cell((LogicState.var_1 & LogicState.var_2).to_string())
                ),
                rx.table.row(
                    rx.table.row_header_cell(LogicState.var_1.to_string()),
                    rx.table.cell(LogicState.var_2.to_string()),
                    rx.table.cell("Logical OR (|)"),
                    rx.table.cell((LogicState.var_1 | LogicState.var_2).to_string())
                ),
                rx.table.row(
                    rx.table.row_header_cell(LogicState.var_1.to_string()),
                    rx.table.cell(LogicState.var_2.to_string()),
                    rx.table.cell("The invert of Var 1 (~)"),
                    rx.table.cell((~LogicState.var_1).to_string())
                )
            ),
            width="100%"
        ),
        rx.button("Update", on_click=LogicState.update)
    )
```

# Contains, Reverse and Join

The 'in' operator is not supported for Var types, we must use the `Var.contains()` instead. When we use `contains`, the var must be of type: `dict`, `list`, `tuple` or `str`. `contains` checks if a var contains the object that we pass to it as an argument.

We use the `reverse` operation to reverse a list var. The var must be of type `list`.

Finally we use the `join` operation to join a list var into a string.

# List 1: 1,2,3,4,6
List 1 Contains 3: true

# List 2: 7,8,9,10
Reverse List 2: 10,9,8,7

# List 3: p,y,t,h,o,n

List 3 Joins: python

```python
class ListsState(rx.State):
    list_1: list = [1, 2, 3, 4, 6]
    list_2: list = [7, 8, 9, 10]
    list_3: list = ["p", "y", "t", "h", "o", "n"]

def var_list_example():
    return rx.hstack(
        rx.vstack(
            rx.heading(f"List 1: {ListsState.list_1}", size="3"),
            rx.text(f"List 1 Contains 3: {ListsState.list_1.contains(3)}")
        ),
        rx.vstack(
            rx.heading(f"List 2: {ListsState.list_2}", size="3"),
            rx.text(f"Reverse List 2: {ListsState.list_2.reverse()}")
        ),
        rx.vstack(
            rx.heading(f"List 3: {ListsState.list_3}", size="3"),
            rx.text(f"List 3 Joins: {ListsState.list_3.join()}")
        )
    )
```

# Lower, Upper, Split

The `lower` operator converts a string var to lowercase. The `upper` operator converts a string var to uppercase. The `split` operator splits a string var into a list.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
            <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
        </div>
    </div>
</div>

# List 1: PYTHON is FUN
List 1 Lower Case: python is fun

# List 2: react is hard

List 2 Upper Case: REACT IS HARD

Split String 2: r,e,a,c,t, ,i,s, ,h,a,r,d

```python
class StringState(rx.State):
    string_1: str = "PYTHON is FUN"
    string_2: str = "react is hard"

def var_string_example():
    return rx.hstack(
        rx.vstack(
            rx.heading(f"List 1: {StringState.string_1}", size="3"),
            rx.text(f"List 1 Lower Case: {StringState.string_1.lower()}"),
        ),
        rx.vstack(
            rx.heading(f"List 2: {StringState.string_2}", size="3"),
            rx.text(f"List 2 Upper Case: {StringState.string_2.upper()}"),
            rx.text(f"Split String 2: {StringState.string_2.split()}")
        )
    )
```

# Get Item (Indexing)
Indexing is only supported for strings, lists, tuples, dicts, and dataframes. To index into a state var strict type annotations are required.

```python
class GetItemState1(rx.State):
    list_1: list = [50, 10, 20]

def get_item_error_1():
    return rx.progress(value=GetItemState1.list_1[0])
```

In the code above you would expect to index into the first index of the `list_1` state var. In fact the code above throws the error: `Invalid var passed for prop value, expected type <class 'int'>, got value of type typing.Any.` This is because the type of the items inside the list have not been clearly defined in the state. To fix this you change the `list_1` definition to `list_1: list[int] = [50, 10, 20]`

```python
class GetItemState1(rx.State):
    list_1: list[int] = [50, 10, 20]

def get_item_error_1():
    return rx.progress(value=GetItemState1.list_1[0])
```

![](https://path-to-your-image.png)

For more information on using state variables with `foreach`, see the documentation.

# Using with Foreach

Errors frequently occur when using indexing and `foreach`.

```python
class ProjectsState(rx.State):
    projects: List[dict] = [
        {
            "technologies": [
                "Next.js",
                "Prisma",
                "Tailwind",
                "Google Cloud",
                "Docker",
                "MySQL"
            ]
        },
        {
            "technologies": [
                "Python",
                "Flask",
                "Google Cloud",
                "Docker"
            ]
        }
    ]

def get_badge(technology: str) -> rx.Component:
    return rx.badge(
        technology, variant="soft", color_scheme="green"
    )

def project_item(project: dict):
    return rx.box(
        rx.hstack(
            rx.foreach(project["technologies"], get_badge)
        )
    )

def failing_projects_example() -> rx.Component:
    return rx.box(
        rx.foreach(ProjectsState.projects, project_item)
    )
```

The code above throws the error `TypeError: Could not foreach over var of type Any. (If you are trying to foreach over a state var, add a type annotation to the var.)`

We must change `projects: list[dict]` → `projects: list[dict[str, list]]` because while projects is annotated, the item in project["technologies"] is not.

```python
class ProjectsState(rx.State):
    projects: List[dict[str, list]] = [
        {
            "technologies": [
                "Next.js",
                "Prisma",
                "Tailwind",
                "Google Cloud",
                "Docker",
                "MySQL"
            ]
        },
        {
            "technologies": [
                "Python",
                "Flask",
                "Google Cloud",
                "Docker"
            ]
        }
    ]

def projects_example() -> rx.Component:
    def get_badge(technology: str) -> rx.Component:
        return rx.badge(
            technology, variant="soft", color_scheme="green"
        )

    def project_item(project: dict) -> rx.Component:
        return rx.box(
            rx.hstack(
                rx.foreach(project["technologies"], get_badge)
            )
        )

    return rx.box(
        rx.foreach(ProjectsState.projects, project_item)
    )
```

Setting the type of `actresses` to be `actresses: list[dict[str,str]]` would fail as it cannot be understood that the value for the pages key is actually a list.

```python
import dataclasses

@dataclasses.dataclass
class ActressType:
    actress_name: str
    age: int
    pages: List[dict[str, str]]

class MultiDataTypeState(rx.State):
    """The app state."""
    
    actresses: List[ActressType] = [
        ActressType(
            actress_name="Ariana Grande",
            age=30,
            pages=[
                {"url": "arianagrande.com"},
                {"url": "https://es.wikipedia.org/wiki/Ariana_Grande"}
            ]
        ),
        ActressType(
            actress_name="Gal Gadot",
            age=38,
            pages=[
                {"url": "http://www.galgadot.com/"},
                {"url": "https://es.wikipedia.org/wiki/Gal_Gadot"}
            ]
        )
    ]

def actresses_example() -> rx.Component:
    def showpage(page: dict[str, str]):
        return rx.vstack(
            rx.text(page["url"])
        )

    def showlist(item: ActressType):
        return rx.vstack(
            rx.hstack(
                rx.text(item.actress_name),
                rx.text(item.age)
            ),
            rx.foreach(item.pages, showpage)
        )

    return rx.box(
        rx.foreach(MultiDataTypeState.actresses, showlist)
    )
```

The previous example had only a single type for each of the dictionaries keys and values. For complex multi-type data, you need to use a dataclass, as shown below.

Ariana Grande
30

arianagrande.com
https://es.wikipedia.org/wiki/Ariana_Grande

Gal Gadot
38

http://www.galgadot.com/
https://es.wikipedia.org/wiki/Gal_Gadot

# Combine Multiple Var Operations

You can also combine multiple var operations together, as seen in the next example.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"></div>
    </div>
</div>

# The number is 0
Even

```python
import random

class VarNumberState(rx.State):
    number: int
    
    @rx.event
    def update(self):
        self.number = random.randint(0, 100)

def var_number_example():
    return rx.vstack(
        rx.heading(f"The number is {VarNumberState.number}", size="5"),
        # Var operations can be composed for more complex expressions.
        rx.cond(
            VarNumberState.number % 2 == 0,
            rx.text("Even", color="green"),
            rx.text("Odd", color="red"),
        ),
        rx.button("Update", on_click=VarNumberState.update),
    )
```

We could have made a computed var that returns the parity of `number`, but it can be simpler just to use a var operation instead.

Var operations may be generally chained to make compound expressions, however some complex transformations not supported by var operations must use computed vars to calculate the value on the backend.