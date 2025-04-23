# Avatar

The Avatar component is used to represent a user, and display their profile pictures or fallback texts such as initials.

[Basic Example](https://reflex.dev/docs/library/data-display/avatar/)

# Basic Example

To create an avatar component with an image, pass the image URL as the `src` prop.

- **Image Avatar**
  ```python
  rx.avatar(src="/logo.jpg")
  ```

To display a text such as initials, set the `fallback` prop without passing the `src` prop.

- **Text Avatar**
  ```python
  rx.avatar(fallback="RX")
  ```

# Styling

- **solid**
- **soft**
- **Accent**

  RX

  RX

- **Gray**

  RX

  RX

- **Gray (High Contrast)**

  RX

  RX

<button style="background-color: tomato;">
  tomato
  <svg aria-hidden="true" fill="currentcolor" height="9" viewBox="0 0 9 9" width="9">
    <path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path>
  </svg>
</button>

[Learn More](https://reflex.dev/docs/library/data-display/avatar/#size)

# Size

The `size` prop controls the size and spacing of the avatar. The acceptable size is from `"1"` to `"9"`, with `"3"` being the default.

- `"1"`
- `"2"`
- `"3"`
- `"4"`
- `"5"`
- `"6"`
- `"7"`
- `"8"`

Here's an example of how to use it:

```python
rx.flex(
    rx.avatar(src="/logo.jpg", fallback="RX", size="1"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="2"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
    rx.avatar(src="/logo.jpg", fallback="RX"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="4"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="5"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="6"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="7"),
    rx.avatar(src="/logo.jpg", fallback="RX", size="8"),
    spacing="1",
)
```

For more information, you can visit the [Reflex Avatar documentation](https://reflex.dev/docs/library/data-display/avatar/#variant).

# Variant

The `variant` prop controls the visual style of the avatar fallback text. The variant can be `"solid"` or `"soft"`. The default is `"soft"`.

## Examples

RX | RX | RX

```python
rx.flex(
    rx.avatar(fallback="RX", variant="solid"),
    rx.avatar(fallback="RX", variant="soft"),
    rx.avatar(fallback="RX"),
    spacing="2",
)
```

For more details, see [Color Scheme](https://reflex.dev/docs/library/data-display/avatar/#color-scheme)

# Color Scheme

The `color_scheme` prop sets a specific color to the fallback text, ignoring the global theme.

```python
rx.flex(
    rx.avatar(fallback="RX", color_scheme="indigo"),
    rx.avatar(fallback="RX", color_scheme="cyan"),
    rx.avatar(fallback="RX", color_scheme="orange"),
    rx.avatar(fallback="RX", color_scheme="crimson"),
    spacing="2",
)
```

[Copy Code](#)

# High Contrast

The `high_contrast` prop increases color contrast of the fallback text with the background.

```python
rx.grid(
    rx.avatar(fallback="RX", variant="solid"),
    rx.avatar(fallback="RX", variant="solid", high_contrast=True),
    rx.avatar(fallback="RX", variant="soft"),
    rx.avatar(fallback="RX", variant="soft", high_contrast=True),
    rows="2",
    spacing="2",
    flow="column",
)
```

For more details, [visit the documentation](https://reflex.dev/docs/library/data-display/avatar/#radius)

# Radius

The `radius` prop sets specific radius value, ignoring the global theme. It can take values `"none"` | `"small"` | `"medium"` | `"large"` | `"full"`.

```python
rx.grid(
    rx.avatar(src="/logo.jpg", fallback="RX", radius="none"),
    rx.avatar(fallback="RX", radius="none"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="small"),
    rx.avatar(fallback="RX", radius="small"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="medium"),
    rx.avatar(fallback="RX", radius="medium"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="large"),
    rx.avatar(fallback="RX", radius="large"),
    rx.avatar(src="/logo.jpg", fallback="RX", radius="full"),
    rx.avatar(fallback="RX", radius="full"),
    rows="2",
    spacing="2",
    flow="column"
)
```

[Learn more about avatar fallback](https://reflex.dev/docs/library/data-display/avatar/#fallback)

# Fallback

The `fallback` prop indicates the rendered text when the `src` cannot be loaded.

## Example Code

```python
rx.flex(
    rx.avatar(fallback="RX"),
    rx.avatar(fallback="PC"),
    spacing="2",
)
```

For more details, you can visit [Final Example](https://reflex.dev/docs/library/data-display/avatar/#final-example)

# Final Example

As part of a user profile page, the Avatar component is used to display the user's profile picture, with the fallback text showing the user's initials. Text components displays the user's full name and username handle and a Button component shows the edit profile button.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <span class="rt-reset rt-AvatarRoot rt-r-size-9 rt-variant-soft" data-accent-color="">
      <img class="rt-AvatarImage" src="/logo.jpg"/>
    </span>
    <p class="rt-Text rt-r-size-4 rt-r-weight-bold">Reflex User</p>
    <p class="rt-Text" data-accent-color="gray">@reflexuser</p>
    <button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="indigo">Edit Profile</button>
  </div>
</div>

```python
rx.flex(
    rx.avatar(src="/logo.jpg", fallback="RU", size="9"),
    rx.text("Reflex User", weight="bold", size="4"),
    rx.text("@reflexuser", color_scheme="gray"),
    rx.button(
        "Edit Profile",
        color_scheme="indigo",
        variant="solid"
    ),
    direction="column",
    spacing="1"
)
```

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/avatar/#rx.avatar)

# rx.avatar

An image element with a fallback for representing the user.

## Example

```html
<div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack">
        <span class="rt-reset rt-AvatarRoot rt-r-size-1 rt-variant-solid" data-accent-color="tomato" data-radius="none">
            <img class="rt-AvatarImage" src="/logo.jpg"/>
        </span>
        <span class="rt-reset rt-AvatarRoot rt-r-size-1 rt-variant-solid" data-accent-color="tomato" data-radius="none">
            <span class="rt-AvatarFallback rt-two-letters">RX</span>
        </span>
    </div>
</div>
```

## Properties

| Prop      | Type | Values                      | Default | Interactive |
|-----------|------|----------------------------|---------|------------|
| variant   | "solid" | "soft"                     |         |            |
| size      | "1"  | "2", ...                   |         |            |
| color_scheme | "tomato" | "red", ...                 |         |            |
| high_contrast | bool              |                            | false   |            |
| radius    | "none" | "small", ...               |         |            |
| src       | str                           |         |            |
| fallback  | str                           |         |            |

Note: This table includes only the properties and their descriptions. The actual implementation details are not included in this Markdown conversion.

# Event Triggers
See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)