# State Utility Methods

The state object has several methods and attributes that return information about the current page, session, or state.

[Router Attributes](/docs/utility-methods/router-attributes/#router-attributes)

# Router Attributes

The `self.router` attribute has several sub-attributes that provide various information:

- **router.page**: data about the current page and route
  - **host**: The hostname and port serving the current page (frontend).
  - **path**: The path of the current page (for dynamic pages, this will contain the slug)
  - **raw_path**: The path of the page displayed in the browser (including params and dynamic values)
  - **full_path**: `path` with `host` prefixed
  - **full_raw_path**: `raw_path` with `host` prefixed
  - **params**: Dictionary of query params associated with the request

- **router.session**: data about the current session
  - **client_token**: UUID associated with the current tab's token. Each tab has a unique token.
  - **session_id**: The ID associated with the client's websocket connection. Each tab has a unique session ID.
  - **client_ip**: The IP address of the client. Many users may share the same IP address.

- **router.headers**: a selection of common headers associated with the websocket connection. These values can only change when the websocket is re-established (for example, during page refresh). All other headers are available in the dictionary `self.router_data.headers`.
  - **host**: The hostname and port serving the websocket (backend).

[Example Values on This Page](/docs/utility-methods/router-attributes/#example-values-on-this-page)

# Example Values on this Page

- **Name**: rx.State.router.page.host
  - Value: `<code></code>`

- **Name**: rx.State.router.page.path
  - Value: `<code></code>`

- **Name**: rx.State.router.page.raw_path
  - Value: `<code></code>`

- **Name**: rx.State.router.page.full_path
  - Value: `<code></code>`

- **Name**: rx.State.router.page.full_raw_path
  - Value: `<code></code>`

- **Name**: rx.State.router.page.params
  - Value: `<code>{}</code>`

- **Name**: rx.State.router.session.client_token
  - Value: `<code></code>`

- **Name**: rx.State.router.session.session_id
  - Value: `<code></code>`

- **Name**: rx.State.router.session.client_ip
  - Value: `<code></code>`

- **Name**: rx.State.router.headers.host
  - Value: `<code></code>`

- **Name**: rx.State.router.headers.user_agent
  - Value: `<code></code>`

- **Name**: rx.State.router.headers.to_string()
  - Value: `<code>{"host":"","origin":"","upgrade":"","connection":"","cookie":"","pragma":"","cache_control":"","user_agent":"","sec_websocket_version":"","sec_websocket_key":"","sec_websocket_extensions":"","accept_encoding":"","accept_language":"","raw_headers":{}}</code>`