# Image

The Image component can display an image given a `src` path as an argument. This could either be a local path from the assets folder or an external link.

![](logo.jpg)

```python
rx.image(src="/logo.jpg", width="100px", height="auto")
```

You can also pass a `PIL` image object as the `src`.

![](https://picsum.photos/id/1/200/300)

```python
from PIL import Image
import requests

class ImageState(rx.State):
    url: str = f"https://picsum.photos/id/1/200/300"
    image: Image.Image = Image.open(
        requests.get(url, stream=True).raw
    )

def image_pil_example():
    return rx.vstack(rx.image(src=ImageState.image))
```

# rx.image only accepts URLs and Pillow Images

## Instructions

This section is hidden by default. Click the button to expand it and view the content.

# How to let your user upload an image

How to let your user upload an image

# API Reference

[API Reference](https://reflex.dev/docs/library/media/image/#rx.image)

# rx.image

Display the img element.

## Props

- **Prop** | **Type | Values** | **Default**
  - `alt` | `str`
  - `cross_origin` | `"anonymous" | "use-credentials" | ...`
  - `decoding` | `"async" | "auto" | ...`
  - `loading` | `"eager" | "lazy"`
  - `referrer_policy` | `"" | "no-referrer" | ...`
  - `sizes` | `str`
  - `src` | `Any`
  - `src_set` | `str`
  - `use_map` | `str`

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)