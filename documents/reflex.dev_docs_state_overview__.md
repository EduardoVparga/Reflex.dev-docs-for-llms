# State

State allows us to create interactive apps that can respond to user input. It defines the variables that can change over time, and the functions that can modify them.

<div class="css-10ddbmu" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-tzz23y" data-orientation="vertical" data-state="closed"></div>
</div>

# Video: State Overview

## State Basics

# State Basics

You can define state by creating a class that inherits from `rx.State`:

```python
import reflex as rx

class State(rx.State):
    """Define your app state here."""
```

A state class is made up of two parts: vars and event handlers.

- **Vars** are variables in your app that can change over time.
- **Event handlers** are functions that modify these vars in response to events.

These are the main concepts to understand how state works in Reflex:

<div class="rt-Grid rt-r-gtc-2 rt-r-gap-2 css-9tf9ac">
  <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-7r3j43"></div>
</div>

# Base Var
- Any variable in your app that can change over time.
- Defined as a field in a `State` class
- Can only be modified by event handlers.

<div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-7r3j43"></div>

# Computed Var
Vars that change automatically based on other vars.
Defined as functions using the `@rx.var` decorator.
Cannot be set by event handlers, are always recomputed when the state changes.

# Event Trigger
A user interaction that triggers an event, such as a button click.
Defined as special component props, such as `on_click`.
Can be used to trigger event handlers.

# Event Handlers

Functions that update the state in response to events.
Defined as methods in the `State` class.
Can be called by event triggers, or by other event handlers.

# Example

Here is a example of how to use state within a Reflex app.
Click the text to change its color.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full"></div>
</div>

# Welcome to Reflex!

The base vars are `colors` and `index`. They are the only vars in the app that may be directly modified within event handlers.

There is a single computed var, `color`, that is a function of the base vars. It will be computed automatically whenever the base vars change.

The heading component links its `on_click` event to the `ExampleState.next_color` event handler, which increments the color index.

# With Reflex, you never have to write an API.

# State vs. Instance?

State vs. Instance?

Cannot print a State var.

# Client States

Each user who opens your app has a unique ID and their own copy of the state.
This means that each user can interact with the app and modify the state
independently of other users.

Because Reflex internally creates a new instance of the state for each user, your code should
never directly initialize a state class.

- Try opening an app in multiple tabs to see how the state changes independently.

All user state is stored on the server, and all event handlers are executed on
the server. Reflex uses websockets to send events to the server, and to send
state updates back to the client.

# Helper Methods

Similar to backend vars, any method defined in a State class that begins with an underscore `_` is considered a helper method. Such methods are not usable as event triggers, but may be called from other event handler methods within the state.

Functionality that should only be available on the backend, such as an authenticated action, should use helper methods to ensure it is not accidentally or maliciously triggered by the client.