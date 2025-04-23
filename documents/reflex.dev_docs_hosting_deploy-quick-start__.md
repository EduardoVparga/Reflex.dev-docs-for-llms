# Reflex Cloud - Quick Start

So far, we have been running our apps locally on our own machines.
But what if we want to share our apps with the world? This is where
the hosting service comes in.

[Quick Start](https://reflex.dev/docs/hosting/deploy-quick-start/#quick-start)

# Quick Start

Reflex’s hosting service makes it easy to deploy your apps without worrying about configuring the infrastructure.

[Deploy Quick Start](https://reflex.dev/docs/hosting/deploy-quick-start/#prerequisites)

# Prerequisites

Hosting service requires `reflex>=0.6.6`.

This tutorial assumes you have successfully run `reflex init` and `reflex run` your app.

Also make sure you have a `requirements.txt` file at the top level app directory that contains all your python dependencies! (To create a `requirements.txt` file, run `pip freeze > requirements.txt`.)

[Authentication](https://reflex.dev/docs/hosting/deploy-quick-start/#authentication)

# Authentication

First run the command below to login / signup to your Reflex Cloud account: (command line)

```sh
reflex login
```

You will be redirected to your browser where you can authenticate through Github or Gmail.

[Login via Web UI](https://reflex.dev/docs/hosting/deploy-quick-start/#web-ui)

# Web UI

Once you are at this URL and you have successfully authenticated, click on the one project you have in your workspace. You should get a screen like this:

![](cloud_project_page.png)

This screen shows the login command and the deploy command. As we are already logged in, we can skip the login command.

[Learn More](https://reflex.dev/docs/hosting/deploy-quick-start/#deployment)

# Deployment

Now you can start deploying your app.

In your cloud UI copy the `reflex deploy` command similar to the one shown below.
```sh
reflex deploy --project 2a432b8f-2605-4753-####-####0cd1####
```

In your project directory (where you would normally run `reflex run`) paste this command. The command is by default interactive. It asks you a few questions for information required for the deployment.

1. The first question will compare your `requirements.txt` to your python environment and if they are different then it will ask you if you want to update your `requirements.txt` or to continue with the current one. If they are identical this question will not appear. To create a `requirements.txt` file, run `pip freeze > requirements.txt`.
2. The second question will search for a deployed app with the name of your current app, if it does not find one then it will ask if you wish to proceed in deploying your new app.
3. The third question is optional and will ask you for an app description.

That’s it! You should receive some feedback on the progress of your deployment and in a few minutes your app should be up. 🎉

Once your code is uploaded, the hosting service will start the deployment. After a complete upload, exiting from the command **does not** affect the deployment process. The command prints a message when you can safely close it without affecting the deployment.

If you go back to the Cloud UI you should be able to see your deployed app and other useful app information.

# Setup a Cloud Config File

<div aria-labelledby="radix-:R5d6kml6:" class="AccordionContent css-14qn398" data-orientation="vertical" data-state="closed" hidden="" id="radix-:Rdd6kml6:" role="region" style="--radix-accordion-content-height: var(--radix-collapsible-content-height); --radix-accordion-content-width: var(--radix-collapsible-content-width);"></div>

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed">

# Moving around the Cloud UI

Moving around the Cloud UI is straightforward. This section will guide you through navigating the interface effectively.

--- 

## Instructions

### Accessing Information Panels

To access information panels, click on the info icon next to the relevant section. An info panel will pop up with detailed instructions or additional information.

### Navigating the Interface

- **Click on sections**: Clicking on different sections of the Cloud UI will take you to related pages or provide more details.
- **Expand and collapse content**: Use the chevron icons to expand or collapse sections for better organization and quick access to information.

---

## Next Steps

Continue exploring the various features and functionalities within the Cloud UI. Each section is designed to help you manage your cloud resources efficiently.

--- 

### Note

If you encounter any issues, refer to the troubleshooting guide available in the Help Center.

# All flag values are saved between runs