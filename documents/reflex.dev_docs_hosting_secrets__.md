# secrets list

Retrieve secrets for a given application.

**Usage**
```sh
$ reflex cloud secrets list [OPTIONS] APP_ID
```

**Arguments**
- `APP_ID`: The ID of the application.  [required]

**Options**
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-j, --json`: Whether to output the result in JSON format.
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# secrets delete

Delete a secret for a given application.

**Usage**:
```sh
$ reflex cloud secrets delete [OPTIONS] APP_ID KEY
```

**Arguments**:
- `APP_ID`: The ID of the application.  [required]
- `KEY`: The key of the secret to delete.  [required]

**Options**:
- `--token TEXT`: The authentication token.
- `--reboot`: Automatically reboot your site with the new secrets
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.

# secrets update

Update secrets for a given application.

**Usage**
```sh
$ reflex cloud secrets update [OPTIONS] APP_ID
```

**Arguments**
- `APP_ID`: The ID of the application.  [required]

**Options**
- `--envfile TEXT`: The path to an env file to use. Will override any envs set manually.
- `--env TEXT`: The environment variables to set: `<key>=<value>`. Required if envfile is not specified. For multiple envs, repeat this option, e.g. --env k1=v2 --env k2=v2.
- `--reboot`: Automatically reboot your site with the new secrets
- `--token TEXT`: The authentication token.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.  [default: info]
- `-i, --interactive`: Whether to use interactive mode.  [default: True]
- `--help`: Show this message and exit.