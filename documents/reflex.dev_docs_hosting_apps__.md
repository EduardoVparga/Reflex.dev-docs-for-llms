# apps scale

Scale an application by changing the VM type or adding/removing regions.

### Usage:
```sh
$ reflex cloud apps scale [OPTIONS] [APP_ID]
```

### Arguments:
- `[APP_ID]`: The ID of the app.

### Options:
- `--app-name TEXT`: The name of the app.
- `--vm-type TEXT`: The virtual machine type to scale to.
- `-r, --regions TEXT`: Region to scale the app to.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `--scale-type TEXT`: The type of scaling.
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps status

Retrieve the status of a specific deployment.

**Usage**

```sh
$ reflex cloud apps status [OPTIONS] DEPLOYMENT_ID
```

**Arguments**

- `DEPLOYMENT_ID`: The ID of the deployment.  [required]

**Options**

- `--watch / --no-watch`: Whether to continuously watch the status.  [default: no-watch]
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps start

Start a stopped application.

**Usage**
```sh
$ reflex cloud apps start [OPTIONS] [APP_ID]
```

**Arguments**
- `[APP_ID]`: The ID of the application.

**Options**
- `--app-name TEXT`: The name of the application.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps stop
Stop a running application.

**Usage**
```sh
$ reflex cloud apps stop [OPTIONS] [APP_ID]
```

**Arguments**
- `[APP_ID]`: The ID of the application.

**Options**
- `--app-name TEXT`: The name of the application.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps delete

Delete an application.

**Usage**
```sh
$ reflex cloud apps delete [OPTIONS] [APP_ID]
```

**Arguments**
- `[APP_ID]`: The ID of the application.

**Options**
- `--app-name TEXT`: The name of the application.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps logs
Retrieve logs for a given application.

**Usage**
```sh
$ reflex cloud apps logs [OPTIONS] [APP_ID]
```

**Arguments**
- `[APP_ID]`: The ID of the application. If no app_id is provided start/end must both be provided.

**Options**
- `--app-name TEXT`: The name of the application.
- `--token TEXT`: The authentication token.
- `--offset INTEGER`: The offset in seconds from the current time.
- `--start INTEGER`: The start time in Unix epoch format.
- `--end INTEGER`: The end time in Unix epoch format.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps history
Retrieve the deployment history for a given application.

**Usage**
```sh
$ reflex cloud apps history [OPTIONS] [APP_ID]
```

**Arguments**
- `[APP_ID]`: The ID of the application.

**Options**
- `--app-name TEXT`: The name of the application.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in json format.
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps build-logs

Retrieve the build logs for a specific deployment.

**Usage**

```sh
$ reflex cloud apps build-logs [OPTIONS] DEPLOYMENT_ID
```

**Arguments**
- `DEPLOYMENT_ID`: The ID of the deployment.  [required]

**Options**
- `--token TEXT`: The authentication token.
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# apps list

List all the hosted deployments of the authenticated user. Will exit if unable to list deployments.

**Usage**

```sh
$ reflex cloud apps list [OPTIONS]
```

**Options**

- `--project TEXT`: The project ID to filter deployments.
- `--project-name TEXT`: The name of the project.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in JSON format.
- `--interactive / --no-interactive`: Whether to list configuration options and ask for confirmation.  [default: interactive]
- `--help`: Show this message and exit.