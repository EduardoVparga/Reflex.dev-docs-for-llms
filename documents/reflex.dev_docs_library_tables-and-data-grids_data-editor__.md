# Data Editor

A datagrid editor based on [Glide Data Grid](https://grid.glideapps.com/)

This component is introduced as an alternative to the [datatable](/docs/library/tables-and-data-grids/data-table/) to support editing the displayed data.

[Learn more about columns](https://reflex.dev/docs/library/tables-and-data-grids/data-editor/#columns)

# Columns

The columns definition should be a list of dict, each dict describing the associated columns. Property of a column dict:

* title: The text to display in the header of the column.
* id: An id for the column, if not defined, will default to a lower case of title
* width: The width of the column.
* type: The type of the columns, default to "str".

# Data

The `data` props of `rx.data_editor` accept a list of list, where each list represent a row of data to display in the table.

[Simple Example](https://reflex.dev/docs/library/tables-and-data-grids/data-editor/#simple-example)

# Simple Example

Here is a basic example of using the data_editor representing data with no interaction and no styling. Below we define the `columns` and the `data` which are taken in by the `rx.data_editor` component. When we define the `columns` we must define a `title` and a `type` for each column we create. The columns in the `data` must then match the defined `type` or errors will be thrown.

```python
columns: list[dict[str, str]] = [
    {
        "title": "Code",
        "type": "str",
    },
    {
        "title": "Value",
        "type": "int",
    },
    {
        "title": "Activated",
        "type": "bool",
    },
]
data: list[list[Any]] = [
    ["A", 1, True],
    ["B", 2, False],
    ["C", 3, False],
    ["D", 4, True],
    ["E", 5, True],
    ["F", 6, False],
]
```

```python
rx.data_editor(
    columns=columns,
    data=data,
)
```

# Interactive Example

Here we define a State, as shown below, that allows us to print the location of the cell as a heading when we click on it, using the `on_cell_clicked` event trigger. Check out all the other `event triggers` that you can use with datatable at the bottom of this page. We also define a `group` with a label `Data`. This groups all the columns with this `group` label under a larger group `Data` as seen in the table below.

<div class="rt-Box css-9tf9ac">
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">

# Cell clicked: 

## Columns

- **Title**: str
- **Name**:
  - Type: str
  - Group: Data
  - Width: 300px
- **Birth**:
  - Type: str
  - Group: Data
  - Width: 150px
- **Human**:
  - Type: bool
  - Group: Data
  - Width: 80px
- **House**: str
  - Group: Data
- **Wand**:
  - Type: str
  - Group: Data
  - Width: 250px
- **Patronus**: str
  - Group: Data
- **Blood status**:
  - Type: str
  - Group: Data
  - Width: 200px

## Data

| Title | Name | Birth | Human | House | Wand | Patronus | Blood status |
|-------|------|-------|-------|-------|------|----------|-------------|
| 1     | Harry James Potter | 31 July 1980 | True | Gryffindor | 11'  Holly  phoenix feather | Stag | Half-blood |
| 2     | Ronald Bilius Weasley | 1 March 1980 | True | Gryffindor | 12' Ash unicorn tail hair | Jack Russell terrier | Pure-blood |
| 3     | Hermione Jean Granger | 19 September, 1979 | True | Gryffindor | 10¾'  vine wood dragon heartstring | Otter | Muggle-born |
| 4     | Albus Percival Wulfric Brian Dumbledore | Late August 1881 | True | Gryffindor | 15' Elder Thestral tail hair core | Phoenix | Half-blood |
| 5     | Rubeus Hagrid | 6 December 1928 | False | Gryffindor | 16'  Oak unknown core | None | Part-Human (Half-giant) |
| 6     | Fred Weasley | 1 April, 1978 | True | Gryffindor | Unknown | Unknown | Pure-blood |

## Functions

```python
class DataEditorState_HP(rx.State):
    clicked_data: str = "Cell clicked: "
    
    cols: list[Any] = [
        {"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 300
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data",
            "width": 80
        },
        {"title": "House", "type": "str"},
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data"
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200
        }
    ]
    
    data = [
        ["1", "Harry James Potter", "31 July 1980", True, "Gryffindor", "11'  Holly  phoenix feather", "Stag", "Half-blood"],
        ["2", "Ronald Bilius Weasley", "1 March 1980", True, "Gryffindor", "12' Ash unicorn tail hair", "Jack Russell terrier", "Pure-blood"],
        ["3", "Hermione Jean Granger", "19 September, 1979", True, "Gryffindor", "10¾'  vine wood dragon heartstring", "Otter", "Muggle-born"],
        ["4", "Albus Percival Wulfric Brian Dumbledore", "Late August 1881", True, "Gryffindor", "15' Elder Thestral tail hair core", "Phoenix", "Half-blood"],
        ["5", "Rubeus Hagrid", "6 December 1928", False, "Gryffindor", "16'  Oak unknown core", "None", "Part-Human (Half-giant)"],
        ["6", "Fred Weasley", "1 April, 1978", True, "Gryffindor", "Unknown", "Unknown", "Pure-blood"]
    ]
    
    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)
    
    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: {pos}"
```

```python
rx.data_editor(
    columns=DataEditorState_HP.cols,
    data=DataEditorState_HP.data,
    on_cell_clicked=DataEditorState_HP.click_cell,
)
```

# Styling Example

Now let's style our datatable to make it look more aesthetic and easier to use. We must first import `DataEditorTheme` and then we can start setting our style props as seen below in `dark_theme`.

We then set these themes using `theme=DataEditorTheme(dark_theme)`. On top of the styling, we can also set some `props` to make some other aesthetic changes to our datatable. We have set the `row_height` to equal `50` so that the content is easier to read. We have also made the `smooth_scroll_x` and `smooth_scroll_y` equal `True` so that we can smoothly scroll along the columns and rows. Finally, we added `column_select=single`, where column select can take any of the following values `none`, `single` or `multiple`.

```python
from reflex.components.datadisplay.dataeditor import DataEditorTheme

dark_theme_snake_case = {
    "accent_color": "#8c96ff",
    "accent_light": "rgba(202, 206, 255, 0.253)",
    "text_dark": "#ffffff",
    "text_medium": "#b8b8b8",
    "text_light": "#a0a0a0",
    "text_bubble": "#ffffff",
    "bg_icon_header": "#b8b8b8",
    "fg_icon_header": "#000000",
    "text_header": "#a1a1a1",
    "text_header_selected": "#000000",
    "bg_cell": "#16161b",
    "bg_cell_medium": "#202027",
    "bg_header": "#212121",
    "bg_header_has_focus": "#474747",
    "bg_header_hovered": "#404040",
    "bg_bubble": "#212121",
    "bg_bubble_selected": "#000000",
    "bg_search_result": "#423c24",
    "border_color": "rgba(225,225,225,0.2)",
    "drilldown_border": "rgba(225,225,225,0.4)",
    "link_color": "#4F5DFF",
    "header_font_style": "bold 14px",
    "base_font_style": "13px",
    "font_family": "Inter, Roboto, -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Ubuntu, noto, arial, sans-serif",
}
```

```python
rx.data_editor(
    columns=DataEditorState_HP.cols,
    data=DataEditorState_HP.data,
    row_height=80,
    smooth_scroll_x=True,
    smooth_scroll_y=True,
    column_select="single",
    theme=DataEditorTheme(**dark_theme),
    height="30vh",
)
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/tables-and-data-grids/data-editor/#api-reference">Learn more about Data Editor</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/tables-and-data-grids/data-editor/#rx.data_editor)

# rx.data_editor

The DataEditor Component.

## Properties

- **rows**: `int`
- **columns**: `Sequence`
- **data**: `Sequence`
- **get_cell_content**: `str`
- **get_cells_for_selection**: `bool`
- **draw_focus_ring**: `bool`
- **fixed_shadow_x**: `bool`
- **fixed_shadow_y**: `bool`
- **freeze_columns**: `int`
- **group_header_height**: `int`
- **header_height**: `int`
- **max_column_auto_width**: `int`
- **max_column_width**: `int`
- **min_column_width**: `int`
- **row_height**: `int`
- **row_markers**: `"none" | "number" | ...`
- **row_marker_start_index**: `int`
- **row_marker_width**: `int`
- **smooth_scroll_x**: `bool`
- **smooth_scroll_y**: `bool`
- **vertical_border**: `bool`
- **column_select**: `"none" | "single" | ...`
- **prevent_diagonal_scrolling**: `bool`
- **overscroll_x**: `int`
- **overscroll_y**: `int`
- **scroll_offset_x**: `int`
- **scroll_offset_y**: `int`
- **theme**: `Union[DataEditorTheme, Dict]`

# Event Triggers

* [See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)

- `on_cell_activated`: Fired when a cell is activated.
- `on_cell_clicked`: Fired when a cell is clicked.
- `on_cell_context_menu`: Fired when a cell is right-clicked.
- `on_cell_edited`: Fired when a cell is edited.
- `on_group_header_clicked`: Fired when a group header is clicked.
- `on_group_header_context_menu`: Fired when a group header is right-clicked.
- `on_group_header_renamed`: Fired when a group header is renamed.
- `on_header_clicked`: Fired when a header is clicked.
- `on_header_context_menu`: Fired when a header is right-clicked.
- `on_header_menu_click`: Fired when a header menu item is clicked.
- `on_item_hovered`: Fired when an item is hovered.
- `on_delete`: Fired when a selection is deleted.
- `on_finished_editing`: Fired when editing is finished.
- `on_row_appended`: Fired when a row is appended.
- `on_selection_cleared`: Fired when the selection is cleared.
- `on_column_resize`: Fired when a column is resized.