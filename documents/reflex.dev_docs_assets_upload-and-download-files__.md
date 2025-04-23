# Files

In addition to any assets you ship with your app, many web apps will often need to receive or send files, whether you want to share media, allow users to import their data, or export some backend data.

In this section, we will cover all you need to know for manipulating files in Reflex.

[Download](https://reflex.dev/docs/assets/upload-and-download-files/#download)

# Download

If you want to let the users of your app download files from your server to their computer, Reflex offers you two ways. 

[Learn more](https://reflex.dev/docs/assets/upload-and-download-files/#with-a-regular-link)

# With a regular link

For some basic usage, simply providing the path to your resource in a `rx.link` will work, and clicking the link will download or display the resource.

[Download](/reflex_banner.png)

```python
rx.link("Download", href="/reflex_banner.png")
```

<a href="https://reflex.dev/docs/assets/upload-and-download-files/#with-">...</a>

# With

Using the `rx.download` event will always prompt the browser to download the file, even if it could be displayed in the browser.

The `rx.download` event also allows the download to be triggered from another backend event handler.

- Download:
  - **Code Example:**
    ```python
    rx.button(
        "Download",
        on_click=rx.download(url="/reflex_banner.png"),
    )
    ```

- Download and Rename:
  - **Code Example:**
    ```python
    rx.button(
        "Download and Rename",
        on_click=rx.download(
            url="/reflex_banner.png",
            filename="different_name_logo.png",
        ),
    )
    ```

If the data to download is not already available at a known URL, pass the `data` directly to the `rx.download` event from the backend.

- Download Random Numbers:
  - **Code Example:**
    ```python
    import random

    class DownloadState(rx.State):
        @rx.event
        def download_random_data(self):
            return rx.download(
                data=",".join([str(random.randint(0, 100)) for _ in range(10)]),
                filename="random_numbers.csv",
            )

    def download_random_data_button():
        return rx.button(
            "Download random numbers",
            on_click=DownloadState.download_random_data,
        )
    ```

The `data` arg accepts `str` or `bytes` data, a `data:` URI, `PIL.Image`, or any state Var. If the Var is not already a string, it will be converted to a string using `JSON.stringify`. This allows complex state structures to be offered as JSON downloads.

Reference page for `rx.download`: [here](https://reflex.dev/docs/api-reference/special-events/#rx.download)

# Upload

Uploading files to your server let your users interact with your app in a different way than just filling forms to provide data.

The component `rx.upload` let your users upload files on the server.

Here is a basic example of how it is used:

```python
def index():
    return rx.fragment(
        rx.upload(rx.text("Upload files"), rx.icon(tag="upload")),
        rx.button(on_submit=State.<your_upload_handler>)
    )
```

For detailed information, see the reference page of the component [here](/docs/library/forms/upload/).