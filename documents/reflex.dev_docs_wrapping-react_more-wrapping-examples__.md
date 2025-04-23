# More React Libraries

[More Wrapping Examples](/docs/wrapping-react/more-wrapping-examples/#ag-charts)

# AG Charts

Here we wrap the AG Charts library from the NPM package [ag-charts-react](https://www.npmjs.com/package/ag-charts-react).

In the react code below, we can see the first 2 lines are importing React and ReactDOM. This can be ignored when wrapping your component.

We import the `AgCharts` component from the `ag-charts-react` library on line 5. In Reflex this is wrapped by `library = "ag-charts-react"` and `tag = "AgCharts"`.

Line 7 defines a functional React component, which on line 26 returns `AgCharts`, similar in the Reflex code to using the `chart` component.

Line 9 uses the `useState` hook to create a state variable `chartOptions` and its setter function `setChartOptions`. The initial state variable is of type dict and has two key value pairs `data` and `series`.

When we see `useState` in React code, it correlates to state variables in your State. As you can see in our Reflex code we have a state variable `chart_options` which is a dictionary, like in our React code.

Moving to line 26, the `AgCharts` has a prop `options`. In order to use this in Reflex we must wrap this prop with `options: rx.Var[dict]` in the `AgCharts` component.

Lines 31 and 32 are rendering the component inside the root element. This can be ignored when wrapping a component as it is done in Reflex by creating an `index` function and adding it to the app.

## React Code

```python
import React, { useState } from 'react'
import ReactDOM from 'react-dom/client'

// React Chart Component
import { AgCharts } from 'ag-charts-react'

const ChartExample = () => {
    // Chart Options: Control & configure the chart
    const [chartOptions, setChartOptions] = useState({
        // Data: Data to be displayed in the chart
        data: [
            { month: 'Jan', avgTemp: 2.3, iceCreamSales: 162000 },
            { month: 'Mar', avgTemp: 6.3, iceCreamSales: 302000 },
            { month: 'May', avgTemp: 16.2, iceCreamSales: 800000 },
            { month: 'Jul', avgTemp: 22.8, iceCreamSales: 1254000 },
            { month: 'Sep', avgTemp: 14.5, iceCreamSales: 950000 },
            { month: 'Nov', avgTemp: 8.9, iceCreamSales: 200000 }
        ],
        // Series: Defines which chart type and data to use
        series: [{ type: 'bar', xKey: 'month', yKey: 'iceCreamSales' }]
    });

    return (
        // AgCharts component with options passed as prop
        <AgCharts options={chartOptions} />
    );
}

// Render component inside root element
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<ChartExample />);
```

## Reflex Code

```python
library = "ag-charts-react"
tag = "AgCharts"

chart_options: rx.Var[dict] = {
    data: [
        { month: 'Jan', avgTemp: 2.3, iceCreamSales: 162000 },
        { month: 'Mar', avgTemp: 6.3, iceCreamSales: 302000 },
        { month: 'May', avgTemp: 16.2, iceCreamSales: 800000 },
        { month: 'Jul', avgTemp: 22.8, iceCreamSales: 1254000 },
        { month: 'Sep', avgTemp: 14.5, iceCreamSales: 950000 },
        { month: 'Nov', avgTemp: 8.9, iceCreamSales: 200000 }
    ],
    series: [{ type: 'bar', xKey: 'month', yKey: 'iceCreamSales' }]
}

def chart() -> AgCharts:
    return tag(options=chart_options)
```

# React Leaflet

In this example we are wrapping the React Leaflet library from the NPM package [react-leaflet](https://www.npmjs.com/package/react-leaflet).

On line 1 we import the `dynamic` function from Next.js and on line 21 we set `ssr: false`. Lines 4 and 6 use the `dynamic` function to import the `MapContainer` and `TileLayer` components from the `react-leaflet` library. This is used to dynamically import the `MapContainer` and `TileLayer` components from the `react-leaflet` library. This is done in Reflex by using the `NoSSRComponent` class when defining the component. There is more information of when this is needed on the [Dynamic Imports](/docs/wrapping-react/guide/) section of this page.

It mentions in the documentation that it is necessary to include the Leaflet CSS file, which is added on line 2 in the React code below. This can be done in Reflex by using the `add_imports` method in the `MapContainer` component. We can add a relative path from within the React library or a full URL to the CSS file.

Line 4 defines a functional React component, which on line 8 returns the `MapContainer` which is done in the Reflex code using the `map_container` component.

The `MapContainer` component has props `center`, `zoom`, `scrollWheelZoom`, which we wrap in the `MapContainer` component in the Reflex code. We ignore the `style` prop as it is a reserved name in Reflex. We can use the `rename_props` method to change the name of the prop, as we will see in the React PDF Renderer example, but in this case we just ignore it and add the `width` and `height` props as css in Reflex.

The `TileLayer` component has a prop `url` which we wrap in the `TileLayer` component in the Reflex code.

Lines 24 and 25 defines and exports a React functional component named `Home` which returns the `MapComponent` component. This can be ignored in the Reflex code when wrapping the component as we return the `map_container` component in the `index` function.

- [React Code](#react-code)
- [Reflex Code](#reflex-code)

## React Code

```javascript
1 | import dynamic from "next/dynamic";
2 | import "leaflet/dist/leaflet.css";
3 |
4 | const MapComponent = dynamic(() => {
5 |   return import("react-leaflet").then(({ MapContainer, TileLayer }) => {
6 |     return () => (
7 |       <MapContainer
8 |         center={[51.505, -0.09]}
9 |         zoom={13}
10|         scrollWheelZoom={true}
11|         style={{ height: "50vh", width: "100%" }}
12|       >
13|         <TileLayer
14|           url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
15|         />
16|       </MapContainer>
17|     );
18|   });
19| }, { ssr: false });

20 | export default function Home() {
21 |   return <MapComponent />;
22 | }
```

## Reflex Code

This section is ignored in the Reflex code when wrapping the component.

# React PDF Renderer

In this example we are wrapping the React renderer for creating PDF files on the browser and server from the NPM package [@react-pdf/renderer](https://www.npmjs.com/package/@react-pdf/renderer).

This example is similar to the previous examples, and again Dynamic Imports are required for this library. This is done in Reflex by using the `NoSSRComponent` class when defining the component. There is more information on why this is needed on the `Dynamic Imports` section of this [page](/docs/wrapping-react/guide/).

The main difference with this example is that the `style` prop, used on lines 20, 21 and 24 in React code, is a reserved name in Reflex so can not be wrapped. A different name must be used when wrapping this prop and then this name must be changed back to the original with the `rename_props` method. In this example we name the prop `theme` in our Reflex code and then change it back to `style` with the `rename_props` method in both the `Page` and `View` components.

# List of reserved names in Reflex

## React Code

```jsx
import ReactDOM from 'react-dom';
import { Document, Page, Text, View, StyleSheet, PDFViewer } from '@react-pdf/renderer';

// Create styles
const styles = StyleSheet.create({
  page: {
    flexDirection: 'row',
    backgroundColor: '#E4E4E4',
  },
  section: {
    margin: 10,
    padding: 10,
    flexGrow: 1,
  },
});

// Create Document Component
const MyDocument = () => (
  <Document>
    <Page size="A4" style={styles.page}>
      <View style={styles.section}>
        <Text>Section #1</Text>
      </View>
      <View style={styles.section}>
        <Text>Section #2</Text>
      </View>
    </Page>
  </Document>
);

const App = () => (
  <PDFViewer>
    <MyDocument />
  </PDFViewer>
);

ReactDOM.render(<App />, document.getElementById('root'));
```