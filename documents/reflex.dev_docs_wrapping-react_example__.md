# Complex Example

In this more complex example we will be wrapping `reactflow` a library for building node based applications like flow charts, diagrams, graphs, etc. 

[Learn More](/docs/wrapping-react/example/#import)

# Import

Let's start by importing the library [reactflow](https://www.npmjs.com/package/reactflow). Let's make a separate file called `reactflow.py` and add the following code:

```python
import refex as rx
from typing import Any, Dict, List, Union

class ReactFlowLib(rx.Component):
    """A component that wraps a react flow lib."""
    
    library = "reactflow"

    def _get_custom_code(self) -> str:
        return """import 'reactflow/dist/style.css';
        """
```

Notice we also use the `_get_custom_code` method to import the css file that is needed for the styling of the library.

[Learn more](/docs/wrapping-react/example/#components)

# Components

For this tutorial we will wrap three components from Reactflow: `ReactFlow`, `Background`, and `Controls`. Lets start with the `ReactFlow` component.

Here we will define the `tag` and the `vars` that we will need to use the component.

For this tutorial we will define `EventHandler` props `on_nodes_change` and `on_connect`, but you can find all the events that the component triggers in the [reactflow docs](https://reactflow.dev/docs/api/react-flow-props/#onnodeschange).

```python
import reflex as rx
from typing import Any, Dict, List, Union

class ReactFlowLib(rx.Component):
    ...

class ReactFlow(ReactFlowLib):
    tag = "ReactFlow"
    
    nodes: rx.Var[List[Dict[str, Any]]]
    
    edges: rx.Var[List[Dict[str, Any]]]
    
    fit_view: rx.Var[bool]
    
    nodes_draggable: rx.Var[bool]
    
    nodes_connectable: rx.Var[bool]
    
    nodes_focusable: rx.Var[bool]
    
    on_nodes_change: rx.EventHandler[lambda e0: [e0]]
    
    on_connect: rx.EventHandler[lambda e0: [e0]]

```

Now lets add the `Background` and `Controls` components. We will also create the components using the `create` method so that we can use them in our app.

```python
import reflex as rx
from typing import Any, Dict, List, Union

class ReactFlowLib(rx.Component):
    ...

class ReactFlow(ReactFlowLib):
    ...

class Background(ReactFlowLib):
    tag = "Background"
    
    color: rx.Var[str]
    
    gap: rx.Var[int]
    
    size: rx.Var[int]
    
    variant: rx.Var[str]

class Controls(ReactFlowLib):
    tag = "Controls"

react_flow = ReactFlow.create
background = Background.create
controls = Controls.create
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="/docs/wrapping-react/example/#building-the-app">

This code snippet provides a comprehensive example of how to create an interactive flowchart using the `react-flow` library in Python with the `react-python-component` framework. Below is a breakdown of each major component and feature:

### 1. **State Management**
The state management is handled by `react-python-component`, which allows you to define reactive properties that can be used within your React components.

```python
from react import *
import react_flow

app = App()
```

### 2. **Defining the State**
You define initial data for nodes and edges:

```python
State = rx.State({
    "nodes": [
        {"data": {"id": "1", "label": "150"}, "position": {"x": 250, "y": 25}},
        {"data": {"id": "2", "label": "25"}, "position": {"x": 100, "y": 125}},
        {"data": {"id": "3", "label": "5"}, "position": {"x": 250, "y": 250}}
    ],
    "edges": [
        {"source": "1", "target": "2"},
        {"source": "2", "target": "3"}
    ]
})
```

### 3. **Event Handlers**
You define event handlers for adding and clearing nodes:

```python
@react.component
def index():
    def add_random_node(e):
        node = {
            "data": {"id": str(len(State.nodes) + 1), "label": str(random.randint(0, 100))},
            "position": {"x": random.randint(50, 250), "y": random.randint(50, 250)}
        }
        State.nodes.append(node)

    def clear_graph(e):
        State.nodes = []
        State.edges = []

    return (
        react_flow(
            background(),
            controls(),
            nodes_draggable=True,
            nodes_connectable=True,
            on_connect=lambda e: State.on_connect(e),
            on_nodes_change=lambda e: State.on_nodes_change(e),
            nodes=State.nodes,
            edges=State.edges,
            fit_view=True
        ),
        react.hstack(
            react.button("Clear graph", on_click=clear_graph, width="100%"),
            react.button("Add node", on_click=add_random_node, width="100%")
        ),
        height="30em",
        width="100%"
    )

app.add_page(index)
```

### 4. **UI Components**
You use the `react_flow` component to render the flowchart and add buttons for interacting with it:

- **react_flow**: This is the main component that handles drawing nodes, edges, and interaction.
- **react.hstack**: Used to create a horizontal layout of buttons.

### 5. **Interactive Features**
- **Nodes and Edges**: You can drag and connect nodes using the `nodes_draggable` and `nodes_connectable` props.
- **Add Node Button**: Clicking this button adds a random node at a random position.
- **Clear Graph Button**: Clicking this button clears all nodes and edges.

### 6. **Running the Application**
The final step is to run the application:

```python
if __name__ == "__main__":
    app.run()
```

### Summary
This code sets up a basic flowchart editor that allows you to add, connect, and clear nodes using Python and `react-python-component`. The use of state management ensures that changes to the nodes and edges are reactive and update dynamically. This example is a great starting point for building more complex interactive applications with React in Python.