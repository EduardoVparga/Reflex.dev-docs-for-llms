# App

The main Reflex app that encapsulates the backend and frontend.

Every Reflex app needs an app defined in its main module.

```python
import reflex as rx

# Define state and pages
...

app = rx.App(
    # Set global level style.
    style={...},
    # Set the top level theme.
    theme=rx.theme(accent_color="blue"),
)
```

![](https://reflex.dev/docs/api-reference/app/#methods)

# Methods

## Signature
- `frontend_exception_handler(exception: 'Exception') -> 'None'`
  - Default frontend exception handler function.

- `backend_exception_handler(exception: 'Exception') -> 'EventSpec'`
  - Default backend exception handler function.

- `add_page(self, component: 'Component | ComponentCallable | None' = None, route: 'str | None' = None, title: 'str | Var | None' = None, description: 'str | Var | None' = None, image: 'str' = 'favicon.ico', on_load: 'EventType[()] | None' = None, meta: 'list[dict[str, str]]' = [], context: 'dict[str, Any] | None' = None)`
  - Add a page to the app.
    If the component is a callable, by default the route is the name of the
    function. Otherwise, a route must be provided.

- `get_load_events(self, route: 'str') -> 'list[IndividualEventType[()]]'`
  - Get the load events for a route.

- `add_custom_404_page(self, component: 'Component | ComponentCallable | None' = None, title: 'str' = '404 - Not Found', image: 'str' = 'favicon.ico', description: 'str' = 'The page was not found', on_load: 'EventType[()] | None' = None, meta: 'list[dict[str, str]]' = [])`
  - Define a custom 404 page for any url having no match.
    If there is no page defined on 'index' route, add the 404 page to it.
    If there is no global catchall defined, add the 404 page with a catchall.

- `add_all_routes_endpoint(self)`
  - Add an endpoint to the app that returns all the routes.

- `modify_state(self, token: 'str') -> 'AsyncIterator[BaseState]'`
  - Modify the state out of band.