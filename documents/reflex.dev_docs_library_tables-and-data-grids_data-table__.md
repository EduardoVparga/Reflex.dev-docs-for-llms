# Data Table

The data table component is a great way to display static data in a table format. You can pass in a pandas dataframe to the `data` prop to create the table.

In this example we will read data from a csv file, convert it to a pandas dataframe and display it in a data_table. We will also add a search, pagination, sorting to the data_table to make it more accessible.

If you want to add, edit or remove data in your app or deal with anything but static data then the `rx.table` might be a better fit for your use case.

```python
import pandas as pd

nba_data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
...
rx.data_table(
    data=nba_data[["Name", "Height", "Age"]],
    pagination=True,
    search=True,
    sort=True,
)
```

The example below shows how to create a data table from a list.

```python
class State(rx.State):
    data: List = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"],
    ]
    columns: List[str] = ["First Name", "Last Name"]

def index():
    return rx.data_table(
        data=State.data,
        columns=State.columns,
    )
```

For more information, visit the [documentation](https://reflex.dev/docs/library/tables-and-data-grids/data-table/#api-reference).

# API Reference

[API Reference](https://reflex.dev/docs/library/tables-and-data-grids/data-table/#rx.data_table)

# rx.data_table

A data table component.

## Props

- **Prop** | **Type | Values** | **Default**
  - `data` | Any | -
  - `columns` | Sequence | -
  - `search` | bool | False
  - `sort` | bool | False
  - `resizable` | bool | False
  - `pagination` | Union[bool, Dict] | None

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)