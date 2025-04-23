# Audio

The audio component can display an audio given an src path as an argument. This could either be a local path from the assets folder or an external link.

```python
rx.audio(
    url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
    width="400px",
    height="32px",
)
```

If we had a local file in the `assets` folder named `test.mp3`, we could set `url="/test.mp3"` to view the audio file.

# How to let your user upload an audio file

To allow users to upload an audio file, you can use the `Radix` library in Reflex. Here is a basic example:

```python
import reflex as rx

def index():
    return rx.button(
        "Upload Audio File",
        color_scheme="violet",
        on_click=rx.upload_audio,
    )

app = rx.App(state=index)
```

For more detailed API reference and examples, you can visit the official Reflex documentation [here](https://reflex.dev/docs/library/media/audio/#api-reference).

# API Reference

[API Reference](https://reflex.dev/docs/library/media/audio/#rx.audio)

# rx.audio

Audio component share with Video component.

## Props

- **Prop** | **Type | Values** | **Default**
- `url` | str | 
- `playing` | bool | Var.create(True)
- `loop` | bool | 
- `controls` | bool | Var.create(True)
- `light` | bool | 
- `volume` | float | 
- `muted` | bool | 
- `width` | str | 
- `height` | str |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

## Trigger | Description
- `on_ready` - Called when media is loaded and ready to play. If playing is set to true, media will play immediately.
- `on_start` - Called when media starts playing.
- `on_play` - Called when media starts or resumes playing after pausing or buffering.
- `on_progress` - Callback containing played and loaded progress as a fraction, and playedSeconds and loadedSeconds in seconds. eg { played: 0.12, playedSeconds: 11.3, loaded: 0.34, loadedSeconds: 16.7 }
- `on_duration` - Callback containing duration of the media, in seconds.
- `on_pause` - Called when media is paused.
- `on_buffer` - Called when media starts buffering.
- `on_buffer_end` - Called when media has finished buffering. Works for files, YouTube and Facebook.
- `on_seek` - Called when media seeks with seconds parameter.
- `on_playback_rate_change` - Called when playback rate of the player changed. Only supported by YouTube, Vimeo (if enabled), Wistia, and file paths.
- `on_playback_quality_change` - Called when playback quality of the player changed. Only supported by YouTube (if enabled).
- `on_ended` - Called when media finishes playing. Does not fire when loop is set to true.
- `on_error` - Called when an error occurs whilst attempting to play media.
- `on_click_preview` - Called when user clicks the light mode preview.
- `on_enable_pip` - Called when picture-in-picture mode is enabled.
- `on_disable_pip` - Called when picture-in-picture mode is disabled.