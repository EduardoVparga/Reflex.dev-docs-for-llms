# Interactive Tutorial: AI Chat App

This tutorial will walk you through building an AI chat app with Reflex. This app is fairly complex, but don't worry - we'll break it down into small steps.

You can find the full source code for this app [here](https://github.com/reflex-dev/reflex-chat).

[What You'll Learn](https://reflex.dev/docs/getting-started/chatapp-tutorial/#what-youll-learn)

# What You'll Learn

In this tutorial you'll learn how to:
- Install `reflex` and set up your development environment.
- Create components to define and style your UI.
- Use state to add interactivity to your app.
- Deploy your app to share with others.

# Setting up Your Project

## Setting up Your Project

<div class="css-10ddbmu" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-tzz23y" data-orientation="vertical" data-state="closed">

We will start by creating a new project and setting up our development environment. First, create a new directory for your project and navigate to it.

```sh
~ $ mkdir chatapp
~ $ cd chatapp
```

Next, we will create a virtual environment for our project. This is optional, but recommended. In this example, we will use `venv` to create our virtual environment.

```sh
chatapp $ python3 -m venv venv
$ source venv/bin/activate
```

Now, we will install Reflex and create a new project. This will create a new directory structure in our project directory.

**Note:** When prompted to select a template, choose option 0 for a blank project.

```sh
chatapp $ pip install reflex
chatapp $ reflex init
────────────────────────────────── Initializing chatapp ───────────────────────────────────
Success: Initialized chatapp
chatapp $ ls
assets         chatapp         rxconfig.py     venv
```

You can run the template app to make sure everything is working.

```sh
chatapp $ reflex run
─────────────────────────────────── Starting Reflex App ───────────────────────────────────
Compiling: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 1/1 0:00:00
────────────────────────────────────── App Running ───────────────────────────────────────
App running at: http://localhost:3000
```

You should see your app running at [http://localhost:3000](http://localhost:3000).

Reflex also starts the backend server which handles all the state management and communication with the frontend. You can test the backend server is running by navigating to [http://localhost:8000/ping](http://localhost:8000/ping).

Now that we have our project set up, in the next section we will start building our app!

# Basic Frontend

Let's start with defining the frontend for our chat app. In Reflex, the frontend can be broken down into independent, reusable components. See the [components docs](/docs/components/props/) for more information.

[Display a question and answer](https://reflex.dev/docs/getting-started/chatapp-tutorial/#display-a-question-and-answer)

# Display A Question And Answer

We will modify the `index` function in `chatapp/chatapp.py` file to return a component that displays a single question and answer.

## What is Reflex?
A way to build web apps in pure Python!

```python
import reflex as rx

def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right"
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left"
        )
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
```

Components can be nested inside each other to create complex layouts. Here we create a parent container that contains two boxes for the question and answer.

We also add some basic styling to the components. Components take in keyword arguments, called [props](/docs/components/props/), that modify the appearance and functionality of the component. We use the `text_align` prop to align the text to the left and right.

# Reusing Components

Now that we have a component that displays a single question and answer, we can reuse it to display multiple questions and answers. We will move the component to a separate function `question_answer` and call it from the `index` function.

## Questions and Answers

- **What is Reflex?**
  - A way to build web apps in pure Python!
- **What can I make with it?**
  - Anything from a simple website to a complex web app!

```python
def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )

def index() -> rx.Component:
    return rx.container(chat())
```

<a href="https://reflex.dev/docs/getting-started/chatapp-tutorial/#chat-input">Learn more</a>

# Chat Input

Now we want a way for the user to input a question. For this, we will use the [input](/docs/library/forms/input/) component to have the user add text and a [button](/docs/library/forms/button/) component to submit the question.

[Ask a question]
[Submit]

- What is Reflex?
  - A way to build web apps in pure Python!
- What can I make with it?
  - Anything from a simple website to a complex web app!

```python
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask a question"),
        rx.button("Ask")
    )

def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar()
    )
```

[Copy Code]

# Styling

Let's add some styling to the app. More information on styling can be found in the [styling docs](/docs/styling/overview). To keep our code clean, we will move the styling to a separate file `chatapp/style.py`.

```python
import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)

answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

input_style = dict(
    border_width="1px",
    padding="0.5em",
    box_shadow=shadow,
    width="350px",
)

button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)
```

We will import the styles in `chatapp.py` and use them in the components. At this point, the app should look like this:

```html
<div class="flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div>
        <div class="text-xl">What is Reflex?</div>
        <div>A way to build web apps in pure Python!</div>
    </div>
    <div>
        <div class="text-xl">What can I make with it?</div>
        <div>Anything from a simple website to a complex web app!</div>
    </div>
    <div>
        <input placeholder="Ask a question" />
        <button>Ask</button>
    </div>
</div>

```

The app is looking good, but it's not very useful yet! In the next section, we will add some functionality to the app.

# State

Now let’s make the chat app interactive by adding state. The state is where we define all the variables that can change in the app and all the functions that can modify them. You can learn more about state in the [state docs](/docs/state/overview/).

[Defining State](https://reflex.dev/docs/getting-started/chatapp-tutorial/#defining-state)

# Defining State

We will create a new file called `state.py` in the `chatapp` directory. Our state will keep track of the current question being asked and the chat history. We will also define an event handler `answer` which will process the current question and add the answer to the chat history.

```python
import reflex as rx

class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    @rx.event
    def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))
```

[Go to Getting Started Tutorial](https://reflex.dev/docs/getting-started/chatapp-tutorial/#binding-state-to-components)

# Binding State to Components

Now we can import the state in `chatapp.py` and reference it in our frontend components. We will modify the `chat` component to use the state instead of the current fixed questions and answers.

```python
from chatapp.state import State

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            style=input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=button_style,
        ),
    )
```

Normal Python `for` loops don't work for iterating over state vars because these values can change and aren't known at compile time. Instead, we use the `foreach` component to iterate over the chat history.

We also bind the input's `on_change` event to the `set_question` event handler, which will update the `question` state var while the user types in the input. We bind the button's `on_click` event to the `answer` event handler, which will process the question and add the answer to the chat history. The `set_question` event handler is a built-in implicitly defined event handler. Every base var has one. Learn more in the [events docs](/docs/events/setters/) under the Setters section.

[Clearing the Input](https://reflex.dev/docs/getting-started/chatapp-tutorial/#clearing-the-input)

# Clearing the Input

Currently the input doesn't clear after the user clicks the button. We can fix this by binding the value of the input to `question`, with `value=State.question`, and clear it when we run the event handler for `answer`, with `self.question = ''`.

```python
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=button_style,
        ),
    )
```

```python
@rx.event
def answer(self):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((self.question, answer))
    self.question = ""
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/getting-started/chatapp-tutorial/#streaming-text">Continue Reading</a>

# Streaming Text

Normally state updates are sent to the frontend when an event handler returns. However, we want to stream the text from the chatbot as it is generated. We can do this by yielding from the event handler. See the [yield events docs](/docs/events/yield-events/) for more info.

[Ask a question](#) input:

- Input: Ask a question
- Button: Ask

```python
# state.py
import asyncio

...

async def answer(self):
    # Our chatbot is not very smart right now...
    answer = "I don't know!"
    self.chat_history.append((self.question, ""))

    # Clear the question input.
    self.question = ""
    # Yield here to clear the frontend input before continuing.
    yield

    for i in range(len(answer)):
        # Pause to show the streaming effect.
        await asyncio.sleep(0.1)
        # Add one letter at a time to the output.
        self.chat_history[-1] = (
            self.chat_history[-1][0],
            answer[:i + 1],
        )
        yield
```

In the next section, we will finish our chatbot by adding AI!

# Final App

We will use OpenAI's API to give our chatbot some intelligence.

[Configure the OpenAI API Key](https://reflex.dev/docs/getting-started/chatapp-tutorial/#configure-the-openai-api-key)

# Configure the OpenAI API Key

Ensure you have an active OpenAI subscription. Save your API key as an environment variable named `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Install the `openai` pypi package:

```bash
pip install openai
```

# Using the API

We need to modify our event handler to send a request to the API.

```python
import os
from openai import AsyncOpenAI

@rx.event
async def answer(self):
    # Our chatbot has some brains now!
    client = AsyncOpenAI(
        api_key=os.environ["OPENAI_API_KEY"]
    )

    session = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": self.question}
        ],
        stop=None,
        temperature=0.7,
        stream=True
    )

    # Add to the answer as the chatbot responds.
    answer = ""
    self.chat_history.append((self.question, answer))

    # Clear the question input.
    self.question = ""
    # Yield here to clear the frontend input before continuing.
    yield

    async for item in session:
        if hasattr(item.choices[0].delta, "content"):
            if item.choices[0].delta.content is None:
                # presence of 'None' indicates the end of the response
                break
            answer += item.choices[0].delta.content
            self.chat_history[-1] = (self.chat_history[-1][0], answer)
            yield
```

Finally, we have our chatbot!

# Final Code

We wrote all our code in three files, which you can find below.

```python
import reflex as rx
from chatapp import style
from chatapp.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style), 
            text_align="right"
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left"
        ),
        margin_y="1em"
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(State.chat_history, lambda messages: qa(messages[0], messages[1]))
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style
        )
    )

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(), 
            action_bar(),
            align="center"
        )
    )

app = rx.App()
app.add_page(index)
```

```python
import os
from openai import AsyncOpenAI

import reflex as rx

class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    async def answer(self):
        client = AsyncOpenAI(
            api_key=os.environ["OPENAI_API_KEY"]
        )
        session = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": self.question}],
            stop=None,
            temperature=0.7,
            stream=True
        )

        answer = ""
        self.chat_history.append((self.question, answer))

        self.question = ""
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield
```

```python
import reflex as rx

shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block"
)

question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4)
)

answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8)
)

input_style = dict(
    border_width="1px",
    padding="0.5em",
    box_shadow=shadow,
    width="350px"
)

button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow
)
```

# Next Steps

Congratulations! You have built your first chatbot. From here, you can read through the rest of the documentations to learn about Reflex in more detail. The best way to learn is to build something, so try to build your own app using this as a starting point!

[Continue Reading](https://reflex.dev/docs/getting-started/chatapp-tutorial/#one-more-thing)

# One More Thing

With our hosting service, you can deploy this app with a single command within minutes. Check out our [Hosting Quick Start](/docs/hosting/deploy-quick-start/).