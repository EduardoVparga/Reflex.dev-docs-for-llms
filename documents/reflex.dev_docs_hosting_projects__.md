# project list

Retrieve a list of projects.

**Usage**:  
```sh
$ reflex cloud project list [OPTIONS]
```

**Options**:  
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in json format.
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# project create
Create a new project.

**Usage**:
```sh
$ reflex cloud project create [OPTIONS] NAME
```

**Arguments**:
- `NAME`: The name of the project.  [required]

**Options**:
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in json format.
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# project select

Select a project.

**Usage**:  
```sh
$ reflex cloud project select [OPTIONS] [PROJECT_ID]
```

**Arguments**:  
- `[PROJECT_ID]`: The project ID to select.

**Options**:  
- `--project-name TEXT`: The name of the project.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `--interactive / --no-interactive`: Whether to list configuration options and ask for confirmation.  [default: interactive]
- `--help`: Show this message and exit.

# project invite

Invite a user to a project.

**Usage:**
```sh
$ reflex cloud project invite [OPTIONS] ROLE USER
```

**Arguments:**
- `ROLE`: The role ID to assign to the user.  [required]
- `USER`: The user ID to invite.  [required]

**Options:**
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

[Go to project role permissions documentation](https://reflex.dev/docs/hosting/projects/#project-role-permissions)

# project role-permissions

Retrieve the permissions for a specific role in a project.

**Usage**

```sh
$ reflex cloud project role-permissions [OPTIONS] ROLE_ID
```

**Arguments**

- `ROLE_ID`: The ID of the role.  [required]

**Options**

- `--project-id TEXT`: The ID of the project. If not provided, the selected project will be used. If no project is selected, it throws an error.
- `--project-name TEXT`: The name of the project.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in json format.
- `--interactive / --no-interactive`: Whether to list configuration options and ask for confirmation.  [default: interactive]
- `--help`: Show this message and exit.

# project users

Retrieve the users for a project.

**Usage**

```sh
$ reflex cloud project users [OPTIONS]
```

**Options**

- `--project-id TEXT`: The ID of the project. If not provided, the selected project will be used. If no project is selected, it throws an error.
- `--project-name TEXT`: The name of the project.
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in json format.
- `--interactive / --no-interactive`: Whether to list configuration options and ask for confirmation.  [default: interactive]
- `--help`: Show this message and exit.