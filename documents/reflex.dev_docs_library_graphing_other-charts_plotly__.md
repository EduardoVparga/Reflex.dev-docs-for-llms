# Plotly

Plotly is a graphing library that can be used to create interactive graphs. Use the `rx.plotly` component to wrap Plotly as a component for use in your web page. Checkout [Plotly](https://plotly.com/graphing-libraries/) for more information.

When integrating Plotly graphs into your UI code, note that the method for displaying the graph differs from a regular Python script. Instead of using `fig.show()`, use `rx.plotly(data=fig)` within your UI code to ensure the graph is properly rendered and displayed within the user interface

[Learn More](https://reflex.dev/docs/library/graphing/other-charts/plotly/#basic-example)

# Basic Example

Let's create a line graph of life expectancy in Canada.

```python
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(
    df,
    x="year",
    y="lifeExp",
    title="Life expectancy in Canada"
)

def line_chart():
    return rx.center(rx.plotly(data=fig))
```

[![Copy code](http://www.example.com/copy.svg)](https://reflex.dev/docs/library/graphing/other-charts/plotly/#3d-graphing-example)

# 3D graphing example

Let's create a 3D surface plot of Mount Bruno. This is a slightly more complicated example, but it wraps in Reflex using the same method. In fact, you can wrap any figure using the same approach.

```python
import plotly.graph_objects as go
import pandas as pd

z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")

fig = go.Figure(data=[go.Surface(z=z_data.values)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
fig.update_layout(scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64), margin=dict(l=65, r=50, b=65, t=90))

def mountain_surface():
    return rx.center(rx.plotly(data=fig))
```

[View the code on Reflex.dev](https://reflex.dev/docs/library/graphing/other-charts/plotly/#plot-as-state-var)

The provided code demonstrates how to create a dynamic line chart using Plotly in Reflex. The `PlotlyState` class manages the state of the DataFrame and the Plotly figure, allowing the chart to update based on user input from a dropdown menu.

### Key Components:

1. **Imports:**
   - Import necessary libraries:
     ```python
     import plotly.express as px
     import plotly.graph_objects as go
     import pandas as pd
     ```

2. **PlotlyState Class:**
   - Define a state class to manage the DataFrame and Plotly figure.
   - Methods within the class (`create_figure` and `set_selected_country`) update the data and the figure based on user input.

3. **Creating the Figure:**
   - The `create_figure` method initializes the DataFrame with Canadian life expectancy data and creates a line chart using Plotly Express.
   ```python
   @rx.event
   def create_figure(self):
       self.df = px.data.gapminder().query("country=='Canada'")
       self.figure = px.line(
           self.df,
           x="year",
           y="lifeExp",
           title="Life expectancy in Canada"
       )
   ```

4. **Updating the Figure:**
   - The `set_selected_country` method updates the DataFrame and the figure based on the selected country.
   ```python
   @rx.event
   def set_selected_country(self, country):
       self.df = px.data.gapminder().query(f"country=='{country}'")
       self.figure = px.line(
           self.df,
           x="year",
           y="lifeExp",
           title=f"Life expectancy in {country}"
       )
   ```

5. **UI Layout:**
   - The `line_chart_with_state` function sets up the UI:
     - A dropdown menu to select a country.
     - A Plotly chart that updates based on the selected country.
     ```python
     def line_chart_with_state():
         return rx.vstack(
             rx.select(
                 ["China", "France", "United Kingdom", "United States", "Canada"],
                 default_value="Canada",
                 on_change=PlotlyState.set_selected_country,
             ),
             rx.plotly(data=PlotlyState.figure, on_mount=PlotlyState.create_figure),
         )
     ```

### How It Works:
1. **Dropdown Menu:**
   - A dropdown menu allows the user to select a country.
   - The `on_change` event triggers the `set_selected_country` method in the state class.

2. **Plotly Figure:**
   - The `rx.plotly` component displays the Plotly figure.
   - When the `create_figure` method is called (either on mount or through user interaction), it updates the figure with the selected country's data.

### Example Output:
- Initially, the chart shows the life expectancy of Canada over the years.
- Selecting a different country from the dropdown will update the chart to show that country’s life expectancy data.

This setup is useful for creating dynamic visualizations where the underlying data and layout can be updated based on user input. The state management ensures that the UI remains responsive and up-to-date with the selected options.

# Adding Styles and Layouts

Use `update_layout()` method to update the layout of your chart. Checkout [Plotly Layouts](https://plotly.com/python/reference/layout/) for all layouts props.

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed"></div>
</div>

# Note that the width and height props are not recommended to ensure the plot remains size responsive to its container. The size of plot will be determined by it's outer container.

## Life expectancy in Canada

year | lifeExp  
---|---
1960 | 72.53488372093023
1970 | 75.06789473684211
1980 | 75.585562440678
1990 | 76.29258824561404
2000 | 77.39556774193548

```python
df = px.data.gapminder().query("country=='Canada'")
fig_1 = px.line(df, x="year", y="lifeExp", title="Life expectancy in Canada")
fig_1.update_layout(title_x=0.5,
                    plot_bgcolor="#c3d7f7",
                    paper_bgcolor="rgba(128, 128, 128, 0.1)",
                    showlegend=True,
                    title_font_family="Open Sans",
                    title_font_size=25)

def add_styles():
    return rx.center(rx.plotly(data=fig_1), width="100%", height="100%")
```

# API Reference

[API Reference](https://reflex.dev/docs/library/graphing/other-charts/plotly/#rx.plotly)

# rx.plotly

Display a plotly graph.

## Prop | Type | Default
- **Prop** | **Type | Values** | **Default**
- `data` | Figure | 
- `layout` | Dict[Any, Any] | 
- `template` | Template | 
- `config` | Dict[Any, Any] | 
- `use_resize_handler` | bool | LiteralVar.create(True)

# Event Triggers

*See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)*

- **on_click**: Fired when the plot is clicked.
- **on_after_plot**: Fired after the plot is redrawn.
- **on_animated**: Fired after the plot was animated.
- **on_animating_frame**: Fired while animating a single frame (does not currently pass data through).
- **on_animation_interrupted**: Fired when an animation is interrupted (to start a new animation for example).
- **on_autosize**: Fired when the plot is responsively sized.
- **on_before_hover**: Fired whenever mouse moves over a plot.
- **on_button_clicked**: Fired when a plotly UI button is clicked.
- **on_deselect**: Fired when a selection is cleared (via double click).
- **on_hover**: Fired when a plot element is hovered over.
- **on_relayout**: Fired after the plot is laid out (zoom, pan, etc).
- **on_relayouting**: Fired while the plot is being laid out.
- **on_restyle**: Fired after the plot style is changed.
- **on_redraw**: Fired after the plot is redrawn.
- **on_selected**: Fired after selecting plot elements.
- **on_selecting**: Fired while dragging a selection.
- **on_transitioning**: Fired while an animation is occurring.
- **on_transition_interrupted**: Fired when a transition is stopped early.
- **on_unhover**: Fired when a hovered element is no longer hovered.