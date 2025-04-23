# App

In Reflex Cloud an "app" (or "application" or "website") refers to a web application built using the Reflex framework, which can be deployed and managed within the Cloud platform.

You can deploy an app using the `reflex deploy` command.

There are many actions you can take in the Cloud UI to manage your app. Below are some of the most common actions you may want to take.

[Stopping an App](https://reflex.dev/docs/hosting/app-management/#stopping-an-app)

# Stopping an App

To stop an app follow the arrow in the image below and press on the `Stop app` button. Pausing an app will stop it from running and will not be accessible to users until you resume it. In addition, this will stop you being billed for your app.

![Stopping app](/stopping_app.webp)

# CLI Command to stop an app

This is the command you can use in your terminal to stop an app:

```sh
reflexctl app stop <app-name>
```

For more information, visit the official documentation: [Deleting an App](https://reflex.dev/docs/hosting/app-management/#deleting-an-app)

# Deleting an App

To delete an app click on the `Settings` tab in the Cloud UI on the app page.

Then click on the `Danger` tab as shown below.
![](https://yourdomain.com/deleting_app.webp)

Here there is a `Delete app` button. Pressing this button will delete the app and all of its data. This action is irreversible.

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
    <div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed">
    </div>
</div>

# CLI Command to delete an app

![Info](/images/info.svg)

## Instructions

To delete an app, use the following command:

```python
reflexctl app delete <app-name>
```

For more details, visit [Other App Settings](https://reflex.dev/docs/hosting/app-management/#other-app-settings)

# Other app settings

Clicking on the `Settings` tab in the Cloud UI on the app page also allows a user to change the `app name`, change the `app description` and check the `app id`.

The other app settings also allow users to edit and add secrets (environment variables) to the app. For more information on secrets, see the [Secrets (Environment Variables)](/docs/hosting/secrets-environment-vars/) page.