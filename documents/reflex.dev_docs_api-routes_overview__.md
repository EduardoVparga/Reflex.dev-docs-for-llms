# Backend API Routes

In addition to your frontend app, Reflex also uses a FastAPI backend to serve your app.

To add additional endpoints to the backend API, you can use `app.add_api_route` and add a route that returns JSON.

```python
async def api_test(item_id: int):
    return {"my_result": item_id}

app = rx.App()
app.api.add_api_route("/items/{item_id}", api_test)
```

Now you can access the endpoint at `localhost:8000/items/23` and get the result.

This is useful for creating a backend API that can be used for purposes other than your Reflex app.

# Reserved Routes

Some routes on the backend are reserved for the runtime of Reflex, and should not be overridden unless you know what you are doing.

[Learn More](https://reflex.dev/docs/api-routes/overview/#ping)

# Ping

You can use this route to check the health of the backend.
```
localhost:8000/ping/
```

The expected return is `"pong"`.

[Learn more about API routes](https://reflex.dev/docs/api-routes/overview/#event)

# Event

localhost:8000/_event: the frontend will use this route to notify the backend that an event occurred.

Overriding this route will break the event communication

[Learn more](https://reflex.dev/docs/api-routes/overview/#upload)

# Upload

This route is used for the upload of file when using `rx.upload()`:  
`localhost:8000/_upload`