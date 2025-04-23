# Secrets (Environment Variables)

[Adding secrets through the CLI](https://reflex.dev/docs/hosting/secrets-environment-vars/#adding-secrets-through-the-cli)

# Adding Secrets through the CLI

Below is an example of how to use an environment variable file. You can pass the `--envfile` flag with the path to the env file. For example:

```sh
reflex deploy --project f88b1574-f101-####-####-5f########## --envfile .env
```

In this example the path to the file is `.env`.

If you prefer to pass the environment variables manually below is deployment command example:

```sh
reflex deploy --project f88b1574-f101-####-####-5f########## --env OPENAI_API_KEY=sk-proj-vD4i9t6U############################
```

They are passed after the `--env` flag as key value pairs.

To pass multiple environment variables, you can repeat the `--env` tag. i.e. `reflex deploy --project f88b1574-f101-####-####-5f########## --env KEY1=VALUE1 --env KEY2=VALUE`. The `--envfile` flag will override any envs set manually.

More information on Environment Variables

This is a link to adding secrets through the cloud UI: [Adding Secrets Through the Cloud UI](https://reflex.dev/docs/hosting/secrets-environment-vars/#adding-secrets-through-the-cloud-ui)

# Adding Secrets through the Cloud UI

To find the secrets tab, click on the `Settings` tab in the Cloud UI on the app page.

Then click on the `Secrets` tab as shown below.

From here you can add or edit your environment variables. You will need to restart your app for these changes to take effect.

This functionality in the UI can be disabled by an admin of the project.