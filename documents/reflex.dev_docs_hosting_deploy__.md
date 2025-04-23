# deploy

Deploy the app to the Reflex hosting service.

**Usage**:
```sh
$ reflex deploy [OPTIONS]
```

**Options**:
- `--app-name TEXT`: The name of the App to deploy under.
- `--app-id TEXT`: The ID of the App to deploy over.
- `-r, --region TEXT`: The regions to deploy to. Run `reflex cloud regions` For multiple envs, repeat this option, e.g. --region sjc --region iad
- `--env TEXT`: The environment variables to set: `<key>=<value>`. For multiple envs, repeat this option, e.g. --env k1=v2 --env k2=v2.
- `--vmtype TEXT`: Vm type id. Run `reflex cloud vmtypes` to get options.
- `--hostname TEXT`: The hostname of the frontend.
- `--interactive / --no-interactive`: Whether to list configuration options and ask for confirmation.
- `--envfile TEXT`: The path to an env file to use. Will override any envs set manually.
- `--loglevel [debug|default|info|warning|error|critical]`: The log level to use.
- `--project TEXT`: project id to deploy to
- `--project-name TEXT`: The name of the project to deploy to.
- `--token TEXT`: token to use for auth
- `--config TEXT`: path to the config file
- `--help`: Show this message and exit.