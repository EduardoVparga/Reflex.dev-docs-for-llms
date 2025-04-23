# Events Overview

Events are composed of two parts: Event Triggers and Event Handlers.

## Event Handlers

Event Handlers are how the State of a Reflex application is updated. They are triggered by user interactions with the UI, such as clicking a button or hovering over an element. Events can also be triggered by the page loading or by other events.

## Event triggers

Event triggers are component props that create an event to be sent to an event handler.
Each component supports a set of event triggers. They are described in each [component's documentation](/docs/library/) in the event trigger section.

[Example](https://reflex.dev/docs/events/events-overview/#example)

# Example

Lets take a look at an example below. Try mousing over the heading to change the word.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full"></div>
</div>

# Welcome

```python
class WordCycleState(rx.State):
    # The words to cycle through.
    text: list[str] = ["Welcome", "to", "Reflex", "!"]

    # The index of the current word.
    index: int = 0

    @rx.event
    def next_word(self):
        self.index = (self.index + 1) % len(self.text)

    @rx.var
    def get_text(self) -> str:
        return self.text[self.index]
```

```python
def event_triggers_example():
    return rx.heading(
        WordCycleState.get_text,
        on_mouse_over=WordCycleState.next_word,
        color="green",
    )
```

In this example, the heading component has the **event trigger**, `on_mouse_over`. Whenever the user hovers over the heading, the `next_word` **event handler** will be called to cycle the word. Once the handler returns, the UI will be updated to reflect the new state.

Adding the `@rx.event` decorator above the event handler is strongly recommended. This decorator enables proper static type checking, which ensures event handlers receive the correct number and types of arguments.

[Link](https://reflex.dev/docs/events/events-overview/#what's-in-this-section?)

# What's in this section?

In the event section of the documentation, you will explore the different types of events supported by Reflex, along with the different ways to call them.