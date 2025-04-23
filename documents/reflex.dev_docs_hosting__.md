# Self Hosting

We recommend using `reflex deploy`, but if this does not fit your use case then you can also host your apps yourself.

Clone your code to a server and install the requirements.

[API URL](https://reflex.dev/docs/getting-started/installation/)

# API URL

Edit your `rxconfig.py` file and set `api_url` to the publicly accessible IP address or hostname of your server, with the port :8000 at the end. Setting this correctly is essential for the frontend to interact with the backend state.

For example if your server is at `app.example.com`, your config would look like this:

```python
config = rx.Config(
    app_name="your_app_name",
    api_url="http://app.example.com:8000",
)
```

It is also possible to set the environment variable `API_URL` at run time or export time to retain the default for local development.

# Production Mode

Then run your app in production mode:

```python
# Run the app in production mode
```

Production mode creates an optimized build of your app. By default, the static frontend of the app (HTML, Javascript, CSS) will be exposed on port `3000` and the backend (event handlers) will be listening on port `8000`.

# Reverse Proxy and Websockets

Reverse Proxy and Websockets

--- 

[Reflex.dev Docs: Hosting Self-Hosting](https://reflex.dev/docs/hosting/self-hosting/#exporting-a-static-build)

# Exporting a Static Build

Exporting a static build of the frontend allows the app to be served using a static hosting provider, like Netlify or Github Pages. Be sure `api_url` is set to an accessible backend URL when the frontend is exported.

```bash
This will create a `frontend.zip` file with your app's minified HTML, Javascript, and CSS build that can be uploaded to your static hosting service.
```

It also creates a `backend.zip` file with your app's backend python code to upload to your server and run.

You can export only the frontend or backend by passing in the `--frontend-only` or `--backend-only` flags.

It is also possible to export the components without zipping. To do this, use the `--no-zip` parameter. This provides the frontend in the `.web/_static/` directory and the backend can be found in the root directory of the project.

[Learn more about self-hosting with Reflex Container Service](https://reflex.dev/docs/hosting/self-hosting/#reflex-container-service)

# Reflex Container Service

Another option is to run your Reflex service in a container. For this purpose, a `Dockerfile` and additional documentation is available in the Reflex project in the directory `docker-example`.

For the build of the container image it is necessary to edit the `rxconfig.py` and add the `requirements.txt` to your project folder. The following changes are necessary in `rxconfig.py`:

```python
config = rx.Config(
    app_name="app",
    api_url="http://app.example.com:8000",
)
```

Notice that the `api_url` should be set to the externally accessible hostname or IP, as the client browser must be able to connect to it directly to establish interactivity.

You can find the `requirements.txt` in the `docker-example` folder of the project too.

The project structure should look like this:

```plaintext
```

After all changes have been made, the container image can now be created as follows.

```bash
```

Finally, you can start your Reflex container service as follows.

```bash
```

For more information, see [Remove Reflex Branding from Your Self-Hosted App](https://reflex.dev/docs/hosting/self-hosting/#remove-reflex-branding-from-your-self-hosted-app)

# Remove Reflex branding from your self-hosted app

To remove the Reflex branding, such as the "Built with Reflex" badge, from your self-hosted app, you must add 
```python
show_built_with_reflex=False
```
to the 
```python
rx.Config()
```
in the `rxconfig.py` file.

A paid [team plan](/pricing) is required to remove the Reflex branding for self-hosted apps.