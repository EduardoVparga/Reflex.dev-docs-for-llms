# Video

The video component can display a video given an src path as an argument. This could either be a local path from the assets folder or an external link.

## Example Video Embed

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" data-gtm-yt-inspected-8="true" frameborder="0" height="100%" id="widget2" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/9bZkp7q19f0?autoplay=0&amp;mute=0&amp;controls=1&amp;origin=https%3A%2F%2Freflex.dev&amp;playsinline=1&amp;showinfo=0&amp;rel=0&amp;iv_load_policy=3&amp;modestbranding=1&amp;enablejsapi=1&amp;widgetid=1&amp;forigin=https%3A%2F%2Freflex.dev%2Fdocs%2Flibrary%2Fmedia%2Fvideo%2F&amp;aoriginsup=0&amp;vf=6" title="PSY - GANGNAM STYLE(강남스타일) M/V" width="100%"></iframe>

### Example Code

```python
rx.video(
    url="https://www.youtube.com/embed/9bZkp7q19f0",
    width="400px",
    height="auto",
)
```

If we had a local file in the `assets` folder named `test.mp4`, we could set `url="/test.mp4"` to view the video.

# How to let your user upload a video

Learn how to allow users to upload videos in Reflex.

[Read more →](https://reflex.dev/docs/library/media/video/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/media/video/#rx.video)

# rx.video

Video component share with audio component.

- **Prop**: `url`  
  - Type | Values: `str`  
  - Default: 
- **Prop**: `playing`  
  - Type | Values: `bool`  
  - Default: 
- **Prop**: `loop`  
  - Type | Values: `bool`  
  - Default: 
- **Prop**: `controls`  
  - Type | Values: `bool`  
  - Default: `Var.create(True)`
- **Prop**: `light`  
  - Type | Values: `bool`  
  - Default: 
- **Prop**: `volume`  
  - Type | Values: `float`  
  - Default: 
- **Prop**: `muted`  
  - Type | Values: `bool`  
  - Default: 
- **Prop**: `width`  
  - Type | Values: `str`  
  - Default: 
- **Prop**: `height`  
  - Type | Values: `str`  
  - Default:

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **on_ready**
  Called when media is loaded and ready to play. If playing is set to true, media will play immediately.

- **on_start**
  Called when media starts playing.

- **on_play**
  Called when media starts or resumes playing after pausing or buffering.

- **on_progress**
  Callback containing played and loaded progress as a fraction, and playedSeconds and loadedSeconds in seconds. eg { played: 0.12, playedSeconds: 11.3, loaded: 0.34, loadedSeconds: 16.7 }

- **on_duration**
  Callback containing duration of the media, in seconds.

- **on_pause**
  Called when media is paused.

- **on_buffer**
  Called when media starts buffering.

- **on_buffer_end**
  Called when media has finished buffering. Works for files, YouTube and Facebook.

- **on_seek**
  Called when media seeks with seconds parameter.

- **on_playback_rate_change**
  Called when playback rate of the player changed. Only supported by YouTube, Vimeo (if enabled), Wistia, and file paths.

- **on_playback_quality_change**
  Called when playback quality of the player changed. Only supported by YouTube (if enabled).

- **on_ended**
  Called when media finishes playing. Does not fire when loop is set to true.

- **on_error**
  Called when an error occurs whilst attempting to play media.

- **on_click_preview**
  Called when user clicks the light mode preview.

- **on_enable_pip**
  Called when picture-in-picture mode is enabled.

- **on_disable_pip**
  Called when picture-in-picture mode is disabled.