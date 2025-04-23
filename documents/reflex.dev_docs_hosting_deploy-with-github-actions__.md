# Deploy with Github Actions

This GitHub Action simplifies the deployment of Reflex applications to Reflex Cloud. It handles setting up the environment, installing the Reflex CLI, and deploying your app with minimal configuration.

This action requires `reflex>=0.6.6`

**Features:**
- Deploy Reflex apps directly from your GitHub repository to Reflex Cloud.
- Supports subdirectory-based app structures.
- Securely uses authentication tokens via GitHub Secrets.

[Learn more](https://reflex.dev/docs/hosting/deploy-with-github-actions/#usage)

# Usage

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/hosting/deploy-with-github-actions/#add-the-action-to-your-workflow">

# Add the Action to Your Workflow

Create a `.github/workflows/deploy.yml` file in your repository and add the following:

```yaml
name: Deploy Reflex App

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Reflex Cloud
        uses: reflex-dev/reflex-deploy-action@v1
        with:
          auth_token: ${{ secrets.REFLEX_PROJECT_ID }}
          project_id: ${{ secrets.REFLEX_PROJECT_ID }}
          app_directory: "my-app-folder" # Optional, defaults to root
          extra_args: "--env THIRD_PARTY_APIKEY=***" # Optional
          python_version: "3.12" # Optional
```

For more information on setting up your secrets, [click here](https://reflex.dev/docs/hosting/deploy-with-github-actions/#set-up-your-secrets)

# Set Up Your Secrets

Store your Reflex authentication token securely in your repository's secrets:

1. Go to your GitHub repository.
2. Navigate to Settings > Secrets and variables > Actions > New repository secret.
3. Create new secrets for `REFLEX_AUTH_TOKEN` and `REFLEX_PROJECT_ID`.

(Create a `REFLEX_AUTH_TOKEN` in the tokens tab of your UI, check out these [docs](/docs/hosting/tokens/#tokens).

The `REFLEX_PROJECT_ID` can be found in the UI when you click on the How to deploy button on the top right when inside a project and copy the ID after the `--project` flag.)

[Learn more about deploying with GitHub Actions](https://reflex.dev/docs/hosting/deploy-with-github-actions/#inputs)

# Inputs

Reflex authentication token stored in GitHub Secrets.
The ID of the project you want to deploy to.
The directory containing your Reflex app.
Additional arguments to pass to the `reflex deploy` command.
The Python version to use for the deployment environment.

- **auth_token**
  - Description: Reflex authentication token stored in GitHub Secrets.
  - Required: true
  - Default: N/A

- **project_id**
  - Description: The ID of the project you want to deploy to.
  - Required: true
  - Default: N/A

- **app_directory**
  - Description: The directory containing your Reflex app.
  - Required: false
  - Default: . (root)

- **extra_args**
  - Description: Additional arguments to pass to the `reflex deploy` command.
  - Required: false
  - Default: N/A

- **python_version**
  - Description: The Python version to use for the deployment environment.
  - Required: false
  - Default: 3.9