# Installation

Reflex requires Python 3.8+. 

<div class="css-10ddbmu" data-orientation="vertical" data-variant="classic"><div class="AccordionItem css-tzz23y" data-orientation="vertical" data-state="closed"></div></div>

# Video: Installation

Installation instructions are available at [Reflex.dev](https://reflex.dev/docs/getting-started/installation/#virtual-environment).

# Virtual Environment

We **highly recommend** creating a virtual environment for your project.

*venv* is the standard option. *conda* and *poetry* are some alternatives.

[Install Reflex on Your System](https://reflex.dev/docs/getting-started/installation/)

# Install Reflex on your system

macOS/Linux

Windows

[Install on macOS/Linux](https://reflex.dev/docs/getting-started/installation/#install-on-macos/linux)

# Install on macOS/Linux

We will go with [venv] here.

[venv]: https://docs.python.org/3/library/venv.html

[Reflex Dev Installation Prerequisites]: https://reflex.dev/docs/getting-started/installation/#prerequisites

# Prerequisites

macOS (Apple Silicon) users should install [Rosetta 2](https://support.apple.com/en-us/HT211861). Run this command:

```
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```

[Create the project directory](https://reflex.dev/docs/getting-started/installation/)

# Create the project directory

Replace `my_app_name` with your project name. Switch to the new directory.

```sh
mkdir my_app_name
cd my_app_name
```

[![Copy](./assets/copy-icon.svg)](./assets/copy-code.sh)

<a href="https://reflex.dev/docs/getting-started/installation/#setup-virtual-environment">Next: Setup Virtual Environment</a>

# Setup virtual environment

```python
python3 -m venv .venv
source .venv/bin/activate
```

## Instructions
1. Run the command `python3 -m venv .venv` to create a virtual environment.
2. Run `source .venv/bin/activate` to activate the virtual environment.

# Getting `No module named venv`?

If you encounter the error message "Getting `<code>No module named venv</code>`?", it might be due to a missing or incorrectly installed Python virtual environment. Make sure you have created and activated a virtual environment before running your Reflex application.

To resolve this issue, follow these steps:

1. Install Python if it is not already installed on your system.
2. Create a virtual environment using the command:
   ```sh
   python -m venv myenv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source myenv/bin/activate
     ```
4. Install the Reflex package within the activated virtual environment:
   ```sh
   pip install reflex
   ```

If you continue to experience issues, refer to the official [Reflex documentation](https://reflex.dev/docs/getting-started/installation/) for more detailed instructions and troubleshooting tips.

# Install Reflex package

Reflex is available as a [pip](https://pypi.org/project/pip/) package.

```shiki one-dark-pro
pip install reflex
```

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed"></div>
</div>

### Getting `command not found: pip`?

This typically means that the Python package manager `pip` is not installed or not added to your system's PATH. To resolve this, you can install `pip` by following these steps:

1. Download the get-pip.py script:
   ```sh
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   ```

2. Run the script using Python:
   ```sh
   python get-pip.py
   ```

After running these commands, `pip` should be installed and ready to use in your terminal.

# Initialize the project

```python
reflex init
```

## Instructions

Click to copy code:

```python
reflex init
```

# Error `command not found: reflex` Mac / Linux

The command will return four template options to choose from as shown below.

Initializing the web directory.
Get started with a template:
0) blank (https://blank-template.reflex.run) - A minimal template
1) dashboard (https://dashboard-new.reflex.run/) - A dashboard with tables and graphs
2) sales (https://sales-new.reflex.run/) - An app to manage sales and customers
3) ai_image_gen (https://ai-image-gen.reflex.run/) - An app to generate images using AI
4) ci_template (https://cijob.reflex.run/) - A template for continuous integration
5) api_admin_panel (https://api-admin-panel.reflex.run/) - An admin panel for an api.
6) nba (https://nba-new.reflex.run/) - A data visualization app for NBA data.
7) customer_data_app (https://customer-data-app.reflex.run/) - An app to manage customer data.
Which template would you like to use? (0):

From here select a template.

[![Copy](./path/to/copy-icon.png)](https://reflex.dev/docs/getting-started/installation/#run-the-app)

# Run the App

Run it in development mode:
```sh
reflex run
```

Your app runs at [http://localhost:3000](http://localhost:3000).

Reflex prints logs to the terminal. To increase log verbosity to help with debugging, use the `--loglevel` flag:
```sh
reflex run --loglevel debug
```

Reflex will hot reload any code changes in real time when running in development mode. Your code edits will show up on [http://localhost:3000](http://localhost:3000) automatically.