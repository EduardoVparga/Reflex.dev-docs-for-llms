# Tutorial: Data Dashboard

During this tutorial you will build a small data dashboard, where you can input data and it will be rendered in table and a graph. This tutorial does not assume any existing Reflex knowledge, but we do recommend checking out the quick [Basics Guide](/docs/getting-started/basics/) first.

The techniques you’ll learn in the tutorial are fundamental to building any Reflex app, and fully understanding it will give you a deep understanding of Reflex.

This tutorial is divided into several sections:

- Setup for the Tutorial: A starting point to follow the tutorial
- Overview: The fundamentals of Reflex UI (components and props)
- Showing Dynamic Data: How to use State to render data that will change in your app.
- Add Data to your App: Using a Form to let a user add data to your app and introduce event handlers.
- Plotting Data in a Graph: How to use Reflex's graphing components.
- Final Cleanup and Conclusion: How to further customize your app and add some extra styling to it.

[What are you building?](https://reflex.dev/docs/getting-started/dashboard-tutorial/#what-are-you-building?)

# What are you building?

In this tutorial, you are building an interactive data dashboard with Reflex.

You can see what the finished app and code will look like here:

- [Add User](#add-user)
- [User Table](#user-table)
- [Gender Graph](#gender-graph)

## Add User

![Add User Button](https://reflex.dev/docs/getting-started/dashboard-tutorial/assets/add-user-button.png)

## User Table

| Name       | Email               | Gender |
|------------|---------------------|--------|
| Danilo Sousa | danilo@example.com  | Male   |
| Zahra Ambessa | zahra@example.com   | Female |

## Gender Graph

![Gender Graph](https://reflex.dev/docs/getting-started/dashboard-tutorial/assets/gender-graph.png)

```python
import reflex as rx
from collections import Counter


class User(rx.Base):
    """The user model."""
    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()

    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)

        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]


def show_user(user: User):
    """Show a user in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon(size=26, name="plus"),
                rx.text("Add User", size="4"),
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Add New User"),
            rx.dialog.description("Fill the form with the user's info"),
            rx.form(
                rx.flex(
                    rx.input(placeholder="User Name", name="name", required=True),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                    ),
                    rx.select(["Male", "Female"], placeholder="male", name="gender"),
                    rx.flex(
                        rx.dialog.close(rx.button("Cancel", variant="soft", color_scheme="gray")),
                        rx.dialog.close(
                            rx.button(
                                "Submit",
                                type="submit",
                            )
                        ),
                        spacing="3",
                        justify="end",
                        direction="column",
                        spacing="4",
                    ),
                ),
                on_submit=State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )


def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(data_key="value", stroke=rx.color("accent", 9), fill=rx.color("accent", 8)),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )


def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                )
            ),
            rx.table.body(rx.foreach(State.users, show_user)),
            variant="surface",
            size="3",
            width="100%",
        ),
        graph(),
        align="center",
        width="100%",
    )


app = rx.App(
    theme=rx.theme(radius="full", accent_color="grass"),
)

app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
    on_load=State.transform_data,
)
```

Don't worry if you don't understand the code above, in this tutorial we are going to walk you through the whole thing step by step.

# Setup for the tutorial

Check out the [installation docs](/docs/getting-started/installation/) to get Reflex set up on your machine. Follow these to create a folder called `dashboard_tutorial`, which you will `cd` into and `pip install reflex`.

We will choose template `0` when we run `reflex init` to get the blank template. Finally run `reflex run` to start the app and confirm everything is set up correctly.

[Continue to Overview](https://reflex.dev/docs/getting-started/dashboard-tutorial/#overview)

# Overview

Now that you’re set up, let’s get an overview of Reflex!

[Inspecting the starter code](https://reflex.dev/docs/getting-started/dashboard-tutorial/)

# Inspecting the starter code

Within our `dashboard_tutorial` folder, there is a `rxconfig.py` file that contains the configuration for our Reflex app. (Check out the [config docs](/docs/advanced-onboarding/configuration/) for more information)

There is also an `assets` folder where static files such as images and stylesheets can be placed to be referenced within your app. ([asset docs](/docs/assets/overview/) for more information)

Most importantly there is a folder also called `dashboard_tutorial` which contains all the code for your app. Inside of this folder there is a file named `dashboard_tutorial.py`. To begin this tutorial we will delete all the code in this file so that we can start from scratch and explain every step as we go.

The first thing we need to do is import `reflex`. Once we have done this we can create a component, which is a reusable piece of user interface code. Components are used to render, manage, and update the UI elements in your application.

Let's look at the example below. Here we have a function called `index` that returns a `text` component (an in-built Reflex UI component) that displays the text "Hello World!".

Next we define our app using `app = rx.App()` and add the component we just defined (`index`) to a page using `app.add_page(index)`. The function name (in this example `index`) which defines the component, must be what we pass into the `add_page`. The definition of the app and adding a component to a page are required for every Reflex app.

```python
import reflex as rx

def index() -> rx.Component:
    return rx.text("Hello World!")

app = rx.App()
app.add_page(index)
```

This code will render a page with the text "Hello World!" when you run your app like below:

Hello World!

# For the rest of the tutorial, `app=rx.App()` and `app.add_page` will be implied and not shown in the code snippets.

For more details, see [Creating a Table](https://reflex.dev/docs/getting-started/dashboard-tutorial/#creating-a-table) in the documentation.

# Creating a table

Let's create a new component that will render a table. We will use the `table` component to do this. The `table` component has a `root`, which takes in a `header` and a `body`, which in turn take in `row` components. The `row` component takes in `cell` components which are the actual data that will be displayed in the table.

```python
def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
    )
```

Components in Reflex have `props`, which can be used to customize the component and are passed in as keyword arguments to the component function. The `rx.table.root` component has for example the `variant` and `size` props, which customize the table as seen below.

```python
def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
        ),
        variant="surface",
        size="3",
    )
```

For more information, see the [Reflex documentation](https://reflex.dev/docs/getting-started/dashboard-tutorial/#showing-dynamic-data-(state)).

# Showing dynamic data (State)

Up until this point all the data we are showing in the app is static. This is not very useful for a data dashboard. We need to be able to show dynamic data that can be added to and updated.

This is where `State` comes in. `State` is a Python class that stores variables that can change when the app is running, as well as the functions that can change those variables.

To define a state class, subclass `rx.State` and define fields that store the state of your app. The state variables (vars) should have a type annotation, and can be initialized with a default value. Check out the [basics](/docs/getting-started/basics/) section for a simple example of how state works.

In the example below we define a `State` class called `State` that has a variable called `users` that is a list of lists of strings. Each list in the `users` list represents a user and contains their name, email and gender.

```python
class State(rx.State):
    users: list[list[str]] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]
```

To iterate over a state var that is a list, we use the [rx.foreach](/docs/components/rendering-iterables/) function to render a list of components. The `rx.foreach` component takes an `iterable` (list, tuple or dict) and a `function` that renders each item in the `iterable`.

# Why can we not just splat this in a `for` loop

Here the render function is `show_user` which takes in a single user and returns a `table.row` component that displays the users name, email and gender.

Danilo Sousa | danilo@example.com | Male  
Zahra Ambessa | zahra@example.com | Female  

```python
class State(rx.State):
    users: list[list[str]] = [
        ["Danilo Sousa", "danilo@example.com", "Male"],
        ["Zahra Ambessa", "zahra@example.com", "Female"],
    ]

def show_user(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(State.users, show_user),
        ),
        variant="surface",
        size="3",
    )
```

As you can see the output above looks the same as before, except now the data is no longer static and can change with user input to the app.

[Reflex.dev Docs](https://reflex.dev/docs/getting-started/dashboard-tutorial/#using-a-proper-class-structure-for-our-data)

# Using a proper class structure for our data

So far our data has been defined in a list of lists, where the data is accessed by index i.e. `user[0]`, `user[1]`. This is not very maintainable as our app gets bigger.

A better way to structure our data in Reflex is to use a class to represent a user. This way we can access the data using attributes i.e. `user.name`, `user.email`.

In Reflex when we create these classes to showcase our data, the class must inherit from `rx.Base`.

`rx.Base` is also necessary if we want to have a state var that is an iterable with different types. For example if we wanted to have `age` as an `int` we would have to use `rx.base` as we could not do this with a state var defined as `list[list[str]]`.

The `show_user` render function is also updated to access the data by named attributes, instead of indexing.

Name | Email | Gender
--- | --- | ---
Danilo Sousa | danilo@example.com | Male
Zahra Ambessa | zahra@example.com | Female

```python
class User(rx.Base):
    """The user model."""
    
    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(
            name="Danilo Sousa",
            email="danilo@example.com",
            gender="Male",
        ),
        User(
            name="Zahra Ambessa",
            email="zahra@example.com",
            gender="Female",
        ),
    ]


def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )


def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            )
        ),
        rx.table.body(
            rx.foreach(State.users, show_user),
        ),
        variant="surface",
        size="3",
    )
```

Next let's add a form to the app so we can add new users to the table.

Great job so far! You've successfully created a form that allows users to add new entries, and these entries are displayed in a table. Let's go through the key components of your code:

### Key Components

1. **Form Definition (`form` function):**
   - The `form` function uses `rx.form` to create a form with fields for name, email, and gender.
   - It includes an input field for each attribute (name, email) and a select dropdown for the gender.
   - A submit button is also included.

2. **Form Submission Handling:**
   - The `on_submit` parameter of the `rx.form` function points to the `add_user` method in the state class.
   - This method appends new user data to the list of users in the state.

3. **Displaying User Data (`index` function):**
   - The `index` function renders both the form and a table that displays all existing users.
   - It uses `rx.foreach` to iterate over the `users` list and display each user using the `show_user` function.

### Full Code Recap

Here is your full code again for reference:

```python
class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))

def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def form():
    return rx.form(
        rx.vstack(
            rx.input(placeholder="User Name", name="name", required=True),
            rx.input(placeholder="user@reflex.dev", name="email"),
            rx.select(["Male", "Female"], placeholder="Male", name="gender"),
            rx.button("Submit", type="submit"),
        ),
        on_submit=State.add_user,
        reset_on_submit=True,
    )

def index() -> rx.Component:
    return rx.vstack(
        form(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                )
            ),
            rx.table.body(rx.foreach(State.users, show_user)),
            variant="surface",
            size="3",
        ),
    )

# Render the app
if __name__ == "__main__":
    rx.app(state=State)
```

### Improvements and Next Steps

1. **Styling:**
   - You might want to add some CSS or use a framework like Tailwind CSS to improve the appearance of your form and table.

2. **Validation:**
   - Add validation for inputs (e.g., checking if email is valid, name is not empty).

3. **Error Handling:**
   - Implement error handling for cases where data might be invalid before submission.

4. **State Management:**
   - Consider using a more advanced state management solution like `rx.Observable` or `rx.Store`.

5. **Enhanced UI:**
   - Add more features such as editing and deleting existing users, sorting the table, etc.

Feel free to ask if you have any specific questions about the code or need further assistance with implementing these improvements!

It looks like you've successfully integrated a form for adding users into your Reflex application. The form appears as a dialog when the user clicks on an "Add User" button, allowing them to input new user details such as name, email, and gender.

Here's a brief summary of what your code does:

1. **User Model**: Defines a `User` class with properties for name, email, and gender.
2. **State Class**: Manages the state of the application, including a list of users.
3. **Add User Function**: Handles the addition of new user data to the state when the form is submitted.
4. **Show User Function**: Generates a table row for each user in the state.
5. **Add Customer Button Component**: Creates a dialog form for adding new users.
6. **Index Component**: Displays the add button and the user list table.

### Key Components

#### `User` Class
```python
class User:
    """The user model."""
    
    name: str
    email: str
    gender: str
```

#### `State` Class
```python
class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female")
    ]
    
    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
```

#### `add_customer_button` Function
```python
def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        # Dialog content...
    )
```

#### `index` Component
```python
def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            # Table header and body...
        ),
    )
```

### Enhancements

1. **Validation**: You might want to add validation for the form inputs (e.g., ensuring the email is valid).
2. **Error Handling**: Handle cases where the form submission fails.
3. **Styling**: Customize the look of your components using Reflex's styling capabilities.

If you have any specific questions or need further enhancements, feel free to ask!

# Plotting Data in a Graph

The last part of this tutorial is to plot the user data in a graph. We will use Reflex's built-in graphing library recharts to plot the number of users of each gender.

[Continue reading](https://reflex.dev/docs/getting-started/dashboard-tutorial/#transforming-the-data-for-the-graph)

# Transforming the Data for the Graph

The graphing components in Reflex expect to take in a list of dictionaries. Each dictionary represents a data point on the graph and contains the x and y values. We will create a new event handler in the state called `transform_data` to transform the user data into the format that the graphing components expect. We must also create a new state variable called `users_for_graph` to store the transformed data, which will be used to render the graph.

```python
from collections import Counter

class State(rx.State):
    users: list[User] = []
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()

    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)

        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]
```

As we can see above the `transform_data` event handler uses the `Counter` class from the `collections` module to count the number of users of each gender. We then create a list of dictionaries from this which we set to the state var `users_for_graph`.

Finally we can see that whenever we add a new user through submitting the form and running the `add_user` event handler, we call the `transform_data` event handler to update the `users_for_graph` state variable.

[Return to Dashboard Tutorial](https://reflex.dev/docs/getting-started/dashboard-tutorial/#rendering-the-graph)

# Rendering the graph

We use the `rx.recharts.bar_chart` component to render the graph. We pass through the state variable for our graphing data as `data=State.users_for_graph`. We also pass in a `rx.recharts.bar` component which represents the bars on the graph. The `rx.recharts.bar` component takes in the `data_key` prop which is the key in the data dictionary that represents the y value of the bar. The `stroke` and `fill` props are used to set the color of the bars.

The `rx.recharts.bar_chart` component also takes in `rx.recharts.x_axis` and `rx.recharts.y_axis` components which represent the x and y axes of the graph. The `data_key` prop of the `rx.recharts.x_axis` component is set to the key in the data dictionary that represents the x value of the bar. Finally we add `width` and `height` props to set the size of the graph.

```python
def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )
```

Finally we add this `graph()` component to our `index()` component so that the graph is rendered on the page. The code for the full app with the graph included is below. If you try this out you will see that the graph updates whenever you add a new user to the table.

```python
from collections import Counter

class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female"),
    ]
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()

    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)

        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]
```

```python
def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon(size=26, icon="plus"),
                text("Add User", size=4),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Add New User"),
            rx.dialog.description("Fill the form with the user's info"),
            rx.form(
                rx.flex(
                    rx.input(placeholder="User Name", name="name", required=True),
                    rx.input(
                        placeholder="user@reflex.dev",
                        name="email",
                    ),
                    rx.select(["Male", "Female"], placeholder="male", name="gender"),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.dialog.close(
                            rx.button("Submit", type="submit"),
                        ),
                        spacing=3,
                        justify="end",
                    ),
                    direction="column",
                    spacing=4,
                ),
                on_submit=State.add_user,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )
```

```python
def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250,
    )
```

```python
def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender"),
                ),
            ),
            rx.table.body(rx.foreach(State.users, show_user)),
            variant="surface",
            size=3,
        ),
        graph(),
    )
```

One thing you may have noticed about your app is that the graph does not appear initially when you run the app, and that you must add a user to the table for it to first appear. This occurs because the `transform_data` event handler is only called when a user is added to the table. In the next section we will explore a solution to this.

# Final Cleanup

[Link](https://reflex.dev/docs/getting-started/dashboard-tutorial/#revisiting-app.add_page)

# Revisiting app.add_page

At the beginning of this tutorial we mentioned that the `app.add_page` function is required for every Reflex app. This function is used to add a component to a page.

The `app.add_page` currently looks like this `app.add_page(index)`. We could change the route that the page renders on by setting the `route` prop such as `route="/custom-route"`, this would change the route to `http://localhost:3000/custom-route` for this page.

We can also set a `title` to be shown in the browser tab and a `description` as shown in search results.

To solve the problem we had above about our graph not loading when the page loads, we can use `on_load` inside of `app.add_page` to call the `transform_data` event handler when the page loads. This would look like `on_load=State.transform_data`. Below see what our `app.add_page` would look like with some of the changes above added.

- Add User
  - Danilo Sousa | danilo@example.com | Male
  - Zahra Ambessa | zahra@example.com | Female

```python
app.add_page(
    index,
    title="Customer Data App",
    description="A simple app to manage customer data.",
    on_load=State.transform_data,
)
```

[Go to Reflex documentation](https://reflex.dev/docs/getting-started/dashboard-tutorial/#revisiting-app=rx.app/)

# Revisiting app=rx.App()

At the beginning of the tutorial we also mentioned that we defined our app using `app=rx.App()`. We can also pass in some props to the `rx.App` component to customize the app.

The most important one is `theme` which allows you to customize the look and feel of the app. The `theme` prop takes in an `rx.theme` component which has several props that can be set.

The `radius` prop sets the global radius value for the app that is inherited by all components that have a `radius` prop. It can be overwritten locally for a specific component by manually setting the `radius` prop.

The `accent_color` prop sets the accent color of the app. Check out other options for the accent color [here](/docs/library/other/theme/).

To see other props that can be set at the app level check out this [documentation](docs.styling.theming.path)

```python
app = rx.App(
    theme=rx.theme(radius="full", accent_color="grass"),
)
```

Unfortunately in this tutorial here we cannot actually apply this to the live example on the page, but if you copy and paste the code below into a reflex app locally you can see it in action.

[Learn More](https://reflex.dev/docs/getting-started/dashboard-tutorial/#conclusion)

# Conclusion

Finally let's make some final styling updates to our app. We will add some hover styling to the table rows and center the table inside the `show_user` with `style={"_hover": {"bg": rx.color("gray", 3)}}, align="center"`.

In addition, we will add some `width="100%"` and `align="center"` to the `index()` component to center the items on the page and ensure they stretch the full width of the page.

Check out the full code and interactive app below:

- A table to display user data
- A form to add new users to the table
- A dialog to showcase the form
- A graph to visualize the user data

In addition to the above we have:
- Explored state to allow you to show dynamic data that changes over time
- Explored events to allow you to make your app interactive and respond to user actions
- Added styling to the app to make it look better

```python
import reflex as rx
from collections import Counter

class User(rx.Base):
    """The user model."""
    name: str
    email: str
    gender: str

class State(rx.State):
    users: list[User] = [
        User(name="Danilo Sousa", email="danilo@example.com", gender="Male"),
        User(name="Zahra Ambessa", email="zahra@example.com", gender="Female")
    ]
    users_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        self.transform_data()

    def transform_data(self):
        """Transform user gender group data into a format suitable for visualization in graphs."""
        # Count users of each gender group
        gender_counts = Counter(user.gender for user in self.users)

        # Transform into list of dict so it can be used in the graph
        self.users_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]

def show_user(user: User):
    """Show a user in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender, style={"_hover": {"bg": rx.color("gray", 3)}}, align="center"),
    )

def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26), rx.text("Add User", size="4"))
        ),
        rx.dialog.content(
            rx.dialog.title("Add New User"),
            rx.dialog.description("Fill the form with the user's info"),
            rx.form(
                rx.flex(
                    rx.input(placeholder="User Name", name="name", required=True),
                    rx.input(placeholder="user@reflex.dev", name="email"),
                    rx.select(["Male", "Female"], placeholder="male", name="gender"),
                    rx.flex(
                        rx.dialog.close(rx.button("Cancel", variant="soft", color_scheme="gray")),
                        rx.dialog.close(rx.button("Submit", type="submit")),
                        spacing="3",
                        justify="end"
                    ),
                    direction="column",
                    spacing="4"
                ),
                on_submit=State.add_user,
                reset_on_submit=False
            )
        )
    )

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(data_key="value", stroke=rx.color("accent", 9), fill=rx.color("accent", 8)),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.users_for_graph,
        width="100%",
        height=250
    )

def index() -> rx.Component:
    return rx.vstack(
        add_customer_button(),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Gender")
                )
            ),
            rx.table.body(rx.foreach(State.users, show_user)),
            variant="surface",
            size="3",
            width="100%"
        ),
        graph(),
        align="center",
        width="100%"
    )

app = rx.App(theme=rx.theme(radius="full", accent_color="grass"))
app.add_page(index, title="Customer Data App", description="A simple app to manage customer data.", on_load=State.transform_data)
```

And that is it for your first dashboard tutorial.

# Advanced Section (Hooking this up to a Database)
Coming Soon!