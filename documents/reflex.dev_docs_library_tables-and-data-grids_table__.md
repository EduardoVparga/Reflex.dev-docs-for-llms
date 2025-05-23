# Table
A semantic table for presenting tabular data.

If you just want to represent static data then the `rx.data_table` might be a better fit for your use case as it comes with in-built pagination, search and sorting. 

[View Example](https://reflex.dev/docs/library/tables-and-data-grids/table/#basic-example)

# Basic Example

## Basic Table
- **Full name**
  - Danilo Sousa
  - Zahra Ambessa
  - Jasper Eriks
- **Email**
  - danilo@example.com
  - zahra@example.com
  - jasper@example.com
- **Group**
  - Developer
  - Admin
  - Developer

```python
rx.table.root(
    rx.table.header(
        rx.table.row(
            rx.table.column_header_cell("Full name"),
            rx.table.column_header_cell("Email"),
            rx.table.column_header_cell("Group"),
        ),
    ),
    rx.table.body(
        rx.table.row(
            rx.table.row_header_cell("Danilo Sousa"),
            rx.table.cell("danilo@example.com"),
            rx.table.cell("Developer"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Zahra Ambessa"),
            rx.table.cell("zahra@example.com"),
            rx.table.cell("Admin"),
        ),
        rx.table.row(
            rx.table.row_header_cell("Jasper Eriks"),
            rx.table.cell("jasper@example.com"),
            rx.table.cell("Developer"),
        ),
    ),
    width="100%",
)
```

### Note
Set the table `width` to fit within its container and prevent it from overflowing.

# Showing State Data (using foreach)

Many times there is a need for the data we represent in our table to be dynamic. Dynamic data must be in `State`. Later we will show an example of how to access data from a database and how to load data from a source file.

In this example there is a `people` data structure in `State` that is iterated through using `rx.foreach`.

## Table Example

- **Full name**
- **Email**
- **Group**

Danilo Sousa | danilo@example.com | Developer
Zahra Ambessa | zahra@example.com | Admin
Jasper Eriks | jasper@example.com | Developer

```python
class TableForEachState(rx.State):
    people: list[list] = [
        ["Danilo Sousa", "danilo@example.com", "Developer"],
        ["Zahra Ambessa", "zahra@example.com", "Admin"],
        ["Jasper Eriks", "jasper@example.com", "Developer"],
    ]

def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )

def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Full name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Group"),
            )
        ),
        rx.table.body(
            rx.foreach(TableForEachState.people, show_person)
        ),
        width="100%",
    )
```

It is also possible to define a `class` such as `Person` below and then iterate through this data structure, as a `list[Person]`.

```python
import dataclasses

@dataclasses.dataclass
class Person:
    full_name: str
    email: str
    group: str
```

For more information on sorting and filtering (searching), see the [documentation](https://reflex.dev/docs/library/tables-and-data-grids/table/#sorting-and-filtering-(searching)).

# Sorting and Filtering (Searching)

In this example we show two approaches to sort and filter data:
- Using SQL-like operations for database-backed models (simulated)
- Using Python operations for in-memory data

Both approaches use the same UI components: `rx.select` for sorting and `rx.input` for filtering.

# Approach 1: Database Filtering and Sorting

For database-backed models, we typically use SQL queries with `select`, `where`, and `order_by`. In this example, we'll simulate this behavior with mock data.

Sort By: Name

Search here...

| Name       | Email              | Phone    | Address         |
|------------|--------------------|----------|-----------------|
| John Doe   | john@example.com   | 555-1234 | 123 Main St     |
| Jane Smith | jane@example.com   | 555-5678 | 456 Oak Ave     |
| Bob Johnson| bob@example.com    | 555-9012 | 789 Pine Rd     |
| Alice Brown| alice@example.com  | 555-3456 | 321 Maple Dr    |

```python
# Simulating database operations with mock data
class DatabaseTableState(rx.State):
    # Mock data to simulate database records
    users: list = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "555-1234",
            "address": "123 Main St"
        },
        {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "555-5678",
            "address": "456 Oak Ave"
        },
        {
            "name": "Bob Johnson",
            "email": "bob@example.com",
            "phone": "555-9012",
            "address": "789 Pine Rd"
        },
        {
            "name": "Alice Brown",
            "email": "alice@example.com",
            "phone": "555-3456",
            "address": "321 Maple Dr"
        }
    ]
    filtered_users: list[dict] = []
    sort_value = ""
    search_value = ""

    @rx.event
    def load_entries(self):
        """Simulate querying the database with filter and sort."""
        # Start with all users
        result = self.users.copy()

        # Apply filtering if search value exists
        if self.search_value != "":
            search_term = self.search_value.lower()
            result = [user for user in result if any(search_term in str(value).lower() for value in user.values())]

        # Apply sorting if sort column is selected
        if self.sort_value != "":
            result = sorted(result, key=lambda x: x[self.sort_value])

        self.filtered_users = result
        yield

    @rx.event
    def sort_values(self, sort_value):
        """Update sort value and reload data."""
        self.sort_value = sort_value
        yield self.load_entries()

    @rx.event
    def filter_values(self, search_value):
        """Update search value and reload data."""
        self.search_value = search_value
        yield self.load_entries()


def show_customer(user):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user["name"]),
        rx.table.cell(user["email"]),
        rx.table.cell(user["phone"]),
        rx.table.cell(user["address"])
    )


def database_table_example():
    return rx.vstack(
        rx.select(["name", "email", "phone", "address"], placeholder="Sort By: Name",
                  on_change=lambda value: DatabaseTableState.sort_values(value)),
        rx.input(placeholder="Search here...",
                 on_change=lambda value: DatabaseTableState.filter_values(value)),
        rx.table.root(
            rx.table.header(rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Phone"),
                rx.table.column_header_cell("Address")
            )),
            rx.table.body(rx.foreach(DatabaseTableState.filtered_users, show_customer)),
            on_mount=DatabaseTableState.load_entries,
            width="100%"
        ),
        width="100%"
    )
```

# Approach 2: In-Memory Filtering and Sorting

For in-memory data, we use Python operations like `sorted()` and list comprehensions.

The state variable `_people` is set to be a backend-only variable. This is done in case the variable is very large in order to reduce network traffic and improve performance.

When a `select` item is selected, the `on_change` event trigger is hooked up to the `set_sort_value` event handler. Every base var has a built-in event handler to set its value for convenience, called `set_VARNAME`.

`current_people` is an `rx.var(cache=True)`. It is a var that is only recomputed when the other state vars it depends on change. This ensures that `People` shown in the table are always up to date whenever they are searched or sorted.

## Python Code Example

```python
import dataclasses

@dataclasses.dataclass
class Person:
    full_name: str
    email: str
    group: str

class InMemoryTableState(rx.State):
    _people = [
        Person(full_name="Danilo Sousa", email="danilo@example.com", group="Developer"),
        Person(full_name="Zahra Ambessa", email="zahra@example.com", group="Admin"),
        Person(full_name="Jasper Eriks", email="zjasper@example.com", group="B-Developer"),
    ]

    sort_value = ""
    search_value = ""

    @rx.var(cache=True)
    def current_people(self) -> list[Person]:
        people = self._people

        if self.sort_value != "":
            people = sorted(
                people,
                key=lambda user: getattr(user, self.sort_value).lower(),
            )

        if self.search_value != "":
            people = [
                person
                for person in people
                if any(self.search_value.lower() in getattr(person, attr).lower() for attr in ["full_name", "email", "group"])
            ]

        return people

def show_person(person: Person):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person.full_name),
        rx.table.cell(person.email),
        rx.table.cell(person.group),
    )

def in_memory_table_example():
    return rx.vstack(
        rx.select(["full_name", "email", "group"], placeholder="Sort By: full_name", on_change=InMemoryTableState.set_sort_value),
        rx.input(placeholder="Search here...", on_change=InMemoryTableState.set_search_value),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Group"),
                ),
            ),
            rx.table.body(
                rx.foreach(InMemoryTableState.current_people, show_person),
            ),
            width="100%",
        ),
    )
```

## Example Table

- **Sort By: full_name**
- **Search here...**

| Full name       | Email             | Group   |
|-----------------|-------------------|---------|
| Danilo Sousa    | danilo@example.com| Developer|
| Zahra Ambessa   | zahra@example.com  | Admin   |
| Jasper Eriks    | zjasper@example.com| B-Developer|

# When to Use Each Approach

- **Database Approach**: Best for large datasets or when the data already exists in a database
- **In-Memory Approach**: Best for smaller datasets, prototyping, or when the data is static or loaded from an API

Both approaches provide the same user experience with filtering and sorting functionality.

# Database

The more common use case for building an `rx.table` is to use data from a database.

The code below shows how to load data from a database and place it in an `rx.table`.

[Loading Data into Table](https://reflex.dev/docs/library/tables-and-data-grids/table/#loading-data-into-table)

# Loading data into table

A `Customer` model is defined that inherits from `rx.Model`.

The `load_entries` event handler executes a query that is used to request information from a database table. This `load_entries` event handler is called on the `on_mount` event trigger of the `rx.table.root`.

If you want to load the data when the page in the app loads, you can set `on_load` in `app.add_page()` to equal this event handler, like `app.add_page(page_name, on_load=State.load_entries)`.

```python
class Customer(rx.Model, table=True):
    """The customer model."""
    
    name: str
    email: str
    phone: str
    address: str
```

```python
from sqlmodel import select

class DatabaseTableState(rx.State):
    users: list[Customer] = []

    @rx.event
    def load_entries(self):
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(Customer)).all()

def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )

def loading_data_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Phone"),
                rx.table.column_header_cell("Address"),
            )
        ),
        rx.table.body(
            rx.foreach(DatabaseTableState.users, show_customer)
        ),
        on_mount=DatabaseTableState.load_entries,
        width="100%",
    )
```

For more information and examples, you can visit the documentation on [filtering (searching) and sorting](https://reflex.dev/docs/library/tables-and-data-grids/table/#filtering-(searching)-and-sorting).

# Filtering (Searching) and Sorting

In this example we sort and filter the data.

For sorting the `rx.select` component is used. The data is sorted based on the attributes of the `Customer` class. When a select item is selected, as the `on_change` event trigger is hooked up to the `sort_values` event handler, the data is sorted based on the state variable `sort_value` attribute selected.

The sorting query gets the `sort_column` based on the state variable `sort_value`, it gets the order using the `asc` function from sql and finally uses the `order_by` function.

For filtering the `rx.input` component is used. The data is filtered based on the search query entered into the `rx.input` component. When a search query is entered, as the `on_change` event trigger is hooked up to the `filter_values` event handler, the data is filtered based on if the state variable `search_value` is present in any of the data in that specific `Customer`.

The `%` character before and after `search_value` makes it a wildcard pattern that matches any sequence of characters before or after the `search_value`. `query.where(...)` modifies the existing query to include a filtering condition. The `or_` operator is a logical OR operator that combines multiple conditions. The query will return results that match any of these conditions. `Customer.name.ilike(search_value)` checks if the `name` column of the `Customer` table matches the `search_value` pattern in a case-insensitive manner (`ilike` stands for "case-insensitive like").

```python
class Customer(rx.Model, table=True):
    """The customer model."""
    
    name: str
    email: str
    phone: str
    address: str
```

```python
from sqlmodel import select, asc, or_

class DatabaseTableState2(rx.State):
    users: list[Customer] = []
    sort_value = ""
    search_value = ""

    @rx.event
    def load_entries(self):
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)

            if self.search_value != "":
                search_value = f"%{self.search_value.lower()}%"
                query = query.where(
                    or_(
                        Customer.name.ilike(search_value),
                        Customer.email.ilike(search_value),
                        Customer.phone.ilike(search_value),
                        Customer.address.ilike(search_value)
                    )
                )

            if self.sort_value != "":
                sort_column = getattr(Customer, self.sort_value)
                order = asc(sort_column)
                query = query.order_by(order)

            self.users = session.exec(query).all()

    @rx.event
    def sort_values(self, sort_value):
        print(sort_value)
        self.sort_value = sort_value
        self.load_entries()

    @rx.event
    def filter_values(self, search_value):
        print(search_value)
        self.search_value = search_value
        self.load_entries()
```

```python
def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.phone),
        rx.table.cell(user.address),
    )

def loading_data_table_example2():
    return rx.vstack(
        rx.select(
            ["name", "email", "phone", "address"],
            placeholder="Sort By: Name",
            on_change=lambda value: DatabaseTableState2.sort_values(value),
        ),
        rx.input(
            placeholder="Search here...",
            on_change=lambda value: DatabaseTableState2.filter_values(value),
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                )
            ),
            rx.table.body(rx.foreach(DatabaseTableState2.users, show_customer)),
            on_mount=DatabaseTableState2.load_entries,
            width="100%",
        ),
        width="100%",
    )
```

# Pagination

Pagination is an important part of database management, especially when working with large datasets. It helps in enabling efficient data retrieval by breaking down results into manageable loads.

The purpose of this code is to retrieve a specific subset of rows from the `Customer` table based on the specified pagination parameters `offset` and `limit`.

- `query.offset(self.offset)` modifies the query to skip a certain number of rows before returning the results. The number of rows to skip is specified by `self.offset`.
- `query.limit(self.limit)` modifies the query to limit the number of rows returned. The maximum number of rows to return is specified by `self.limit`.

The pagination controls are as follows:

- **Prev**: Move to the previous page.
- **Next**: Move to the next page.

## Code Example

```python
from sqlmodel import select, func

class DatabaseTableState3(rx.State):
    users: list[Customer] = []
    
    total_items: int
    offset: int = 0
    limit: int = 3
    
    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1 + (1 if self.offset % self.limit else 0)

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return self.total_items // self.limit + (1 if self.total_items % self.limit else 0)

    @rx.event
    def prev_page(self):
        self.offset = max(self.offset - self.limit, 0)
        self.load_entries()

    @rx.event
    def next_page(self):
        if self.offset + self.limit < self.total_items:
            self.offset += self.limit
        self.load_entries()

    def _get_total_items(self, session):
        """Return the total number of items in the Customer table."""
        self.total_items = session.exec(select(func.count(Customer.id))).one()

    @rx.event
    def load_entries(self):
        """Get all users from the database."""
        with rx.session() as session:
            query = select(Customer)
            
            # Apply pagination
            query = query.offset(self.offset).limit(self.limit)

            self.users = session.exec(query).all()
            self._get_total_items(session)
```

## Function Definitions

- `show_customer(user: Customer)`: Show a customer in a table row.
- `loading_data_table_example3()`: A function that returns the main layout for displaying and navigating through paginated customers.

# More advanced examples

The real power of the `rx.table` comes where you are able to visualise, add and edit data live in your app. Check out these apps and code to see how this is done: 
- [https://customer-data-app.reflex.run](https://customer-data-app.reflex.run)
- [https://github.com/reflex-dev/reflex-examples/tree/main/customer_data_app](https://github.com/reflex-dev/reflex-examples/tree/main/customer_data_app) and code: [https://github.com/reflex-dev/data-viewer](https://github.com/reflex-dev/data-viewer).

# Download

Most users will want to download their data after they have got the subset that they would like in their table.

In this example there are buttons to download the data as a `json` and as a `csv`.

For the `json` download, `rx.download` is in the frontend code attached to the `on_click` event trigger for the button. This works because if the `Var` is not already a string, it will be converted to a string using `JSON.stringify`.

For the `csv` download, `rx.download` is in the backend code as an event_handler `download_csv_data`. There is also a helper function `_convert_to_csv` that converts the data in `self.users` to `csv` format.

There are buttons for downloading the data as JSON and CSV:

- Download as JSON
- Download as CSV

```python
import io
import csv
from sqlmodel import select

class TableDownloadState(rx.State):
    users: list[Customer] = []

    @rx.event
    def load_entries(self):
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(Customer)).all()

    def _convert_to_csv(self) -> str:
        """Convert the users data to CSV format."""

        # Make sure to load the entries first
        if not self.users:
            self.load_entries()

        # Define the CSV file header based on the Customer model's attributes
        fieldnames = list(Customer.__fields__)

        # Create a string buffer to hold the CSV data
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for user in self.users:
            writer.writerow(user.dict())

        # Get the CSV data as a string
        csv_data = output.getvalue()
        output.close()
        return csv_data

    @rx.event
    def download_csv_data(self):
        csv_data = self._convert_to_csv()
        return rx.download(
            data=csv_data,
            filename="data.csv",
        )

def show_customer(user: Customer):
    """Show a customer in a table row."""
    return rx.table.row(rx.table.cell(user.name), rx.table.cell(user.email), rx.table.cell(user.phone), rx.table.cell(user.address))

def download_data_table_example():
    return rx.vstack(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Phone"),
                    rx.table.column_header_cell("Address"),
                )
            ),
            rx.table.body(rx.foreach(TableDownloadState.users, show_customer)),
            width="100%",
            on_mount=TableDownloadState.load_entries,
        ),
        rx.hstack(
            rx.button(
                "Download as JSON",
                on_click=rx.download(
                    data=TableDownloadState.users,
                    filename="data.json",
                ),
            ),
            rx.button(
                "Download as CSV",
                on_click=TableDownloadState.download_csv_data,
            ),
            spacing="7",
            width="100%",
        ),
        width="100%",
        spacing="5",
    )
```

# Real World Example UI

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
<div class="rt-Flex rt-r-fd-column rt-r-gap-2 css-8atqhb"></div>
</div>
</div>

# Your Team

Invite and manage your team members

[Email Address](input field)

**Invite**
<button>Invite</button>

Danilo Sousa - [danilo@example.com](danilo@example.com) - Developer  
Zahra Ambessa - [zahra@example.com](zahra@example.com) - Admin  
Jasper Eriksson - [jasper@example.com](jasper@example.com) - Developer

```python
rx.flex(
    rx.heading("Your Team"),
    rx.text("Invite and manage your team members"),
    rx.flex(
        rx.input(placeholder="Email Address"),
        rx.button("Invite", justify="center", spacing="2")
    ),
    rx.table.root(
        rx.table.body(
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="DS")),
                rx.table.row_header_cell(rx.link("Danilo Sousa")),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Developer", align="center")
            ),
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="ZA")),
                rx.table.row_header_cell(rx.link("Zahra Ambessa")),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Admin", align="center")
            ),
            rx.table.row(
                rx.table.cell(rx.avatar(fallback="JE")),
                rx.table.row_header_cell(rx.link("Jasper Eriksson")),
                rx.table.cell("jasper@example.com"),
                rx.table.cell("Developer", align="center")
            )
        ),
        width="100%",
    ),
    width="100%",
    direction="column",
    spacing="2"
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/tables-and-data-grids/table/#rx.table.root)

# rx.table.root

A semantic table for presenting tabular data.

## Table of Users

| Full Name       | Email                | Group    |
|-----------------|----------------------|----------|
| Danilo Rosa     | danilo@example.com   | Developer|
| Zahra Ambessa   | zahra@example.com    | Admin    |

### Properties

| Prop           | Type | Default | Interactive |
|----------------|------|---------|-------------|
| size           | "1" | "2" | ...        | -          |
| variant        | "surface" | "ghost"     | surface     | -          |
| align          | "left" | "center" | ...        | left       |
| summary        | str  | -       |            |

Note: Some interactive elements and additional styling details are not represented in this Markdown format.

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.table.header
The header of the table defines column names and other non-data elements.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.table.row

A row containing table cells.

## Table of Names and Emails

Danilo Rosa | danilo@example.com, danilo@yahoo.com, danilo@gmail.com | Developer  
Zahra Ambessa | zahra@example.com | Admin

## Properties

Prop | Type | Default | Interactive  
---|---|---|---  
align | "start" | "center" | ... |  

- Start  
- Center  
- ...  

Default: None  
Interactive: Dropdown Menu

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.table.column_header_cell

A table cell that is semantically treated as a column header.

## Table 1

| Full Name | Email         | Group   |
|-----------|--------------|---------|
| Danilo Rosa | danilo@example.com | Developer |
| Zahra Ambessa | zahra@example.com | Admin     |

## Properties

| Prop               | Type | Values             | Default | Interactive |
|--------------------|------|--------------------|---------|------------|
| justify            | str  | "start" | "center" | ...       | -          |
| min_width          | str  |                    |         |            |
| max_width          | str  |                    |         |            |
| align              | str  | "left" | "center" | ...       | -          |
| col_span           | int  |                   |         |            |
| headers            | str  |                   |         |            |
| row_span           | int  |                   |         |            |
| scope              | str  |                   |         |            |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.table.body

The body of the table contains the data rows.

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.table.cell

A cell containing data.

## Table Data

| Full Name   | Email           | Group     |
|-------------|-----------------|-----------|
| Danilo Rosa | danilo@example.com | Developer |
| Zahra Ambessa | zahra@example.com | Admin     |

### Props

| Prop       | Type | Values                 | Default | Interactive |
|------------|------|------------------------|---------|-------------|
| justify    |      | "start" | "center" | ...        | -          | start     | <button>...</button> |
| min_width  | str  |                       |         |             |
| max_width  | str  |                       |         |             |
| align      |      | "left" | "center" | ...        | -          | left      | <button>...</button> |
| col_span   | int  |                       |         |             |
| headers    | str  |                       |         |             |
| row_span   | int  |                       |         |             |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

# rx.table.row_header_cell
A table cell that is semantically treated as a row header.

## Table

| Full Name | Email | Group |
| --- | --- | --- |
| Danilo Rosa | danilo@example.com | Developer |
| Zahra Ambessa | zahra@example.com | Admin |

### Properties

| Prop | Type | Default | Interactive |
| --- | --- | --- | --- |
| justify | "start" |  |  |
| min_width | str |  |  |
| max_width | str |  |  |
| align | "left" |  |  |
| col_span | int |  |  |
| headers | str |  |  |
| row_span | int |  |  |
| scope | str |  |  |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)