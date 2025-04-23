# Regions

To scale your app you can choose different regions. Regions are different locations around the world where your app can be deployed.

To scale your app to multiple regions in the Cloud UI, click on the `Settings` tab in the Cloud UI on the app page, and then click on the `Regions` tab as shown below. Clicking on the `Add new region` button will allow you to scale your app to multiple regions.

The images below show all the regions that can be deployed in.
- ![](https://yourdomain.com/scaling_regions.webp)
- ![](https://yourdomain.com/regions_1.webp)
- ![](https://yourdomain.com/regions_2.webp)

For more information, you can visit [Selecting Regions to Deploy in the CLI](https://reflex.dev/docs/hosting/regions/#selecting-regions-to-deploy-in-the-cli).

# Selecting Regions to Deploy in the CLI

Below is an example of how to deploy your app in several regions:

```sh
reflex deploy --project f88b1574-f101-####-####-5f########## --region sjc --region iad
```

By default all apps are deloyed in `sjc` if no other regions are given. If you wish to deploy in another region or several regions you can pass the `--region` flag (`-r` also works) with the region code. Check out all the regions that we can deploy to below: [here](https://reflex.dev/docs/hosting/regions/#config-file)

# Config File

To create a `config.yml` file for your app run the command below:

```sh
reflex cloud config
```

This will create a yaml file similar to the one below where you can edit the app configuration:

```yaml
name: medo
description: ''
regions:
  sjc: 1
  lhr: 2
vmtype: c1m1
hostname: null
envfile: .env
project: null
packages:
- procps
```