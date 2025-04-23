# Spinner
Spinner is used to display an animated loading indicator when a task is in progress.

A spinner example:
- - -
```python
rx.spinner()
```
![](https://reflex.dev/docs/library/data-display/spinner/)

# Basic Examples

Spinner can have different sizes.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
  <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
    <div class="rt-Flex rt-r-fd-column rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt">
      <div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-gap-3 rx-Stack css-6pkcdq">
        <span class="rt-Spinner rt-r-size-1"><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span></span>
        <span class="rt-Spinner rt-r-size-2"><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span></span>
        <span class="rt-Spinner rt-r-size-3"><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span><span class="rt-SpinnerLeaf"></span></span>
      </div>
    </div>
  </div>
</div>

```python
rx.vstack(
    rx.hstack(
        rx.spinner(size="1"),
        rx.spinner(size="2"),
        rx.spinner(size="3"),
        align="center",
        gap="1em",
    )
)
```

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/data-display/spinner/#demo-with-buttons">...</a>

# Demo with buttons

Buttons have their own loading prop that automatically composes a spinner.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-loading rt-Button" data-accent-color="" data-disabled="true" disabled="">
            Bookmark
        </button>
    </div>
    <div class="rt-Box relative mb-4">
        <div class="rt-Box code-block css-1islnds">
            <pre class="shiki one-dark-pro" style="background-color:#282c34;color:#abb2bf" tabindex="0"><code>rx.button("Bookmark", loading=True)</code></pre>
        </div>
    </div>
</a>

<a class="rt-Text rt-reset rt-Link rt-underline-none flex flex-row items-center gap-6 hover:!text-violet-11 text-slate-12 cursor-pointer mb-2 transition-colors group css-1macts" data-accent-color="" href="https://reflex.dev/docs/library/data-display/spinner/#spinner-inside-a-button"></a>

# Spinner inside a button

If you have an icon inside the button, you can use the button's disabled state and wrap the icon in a standalone rx.spinner to achieve a more sophisticated design.

<div class="rt-Box py-4 gap-4 flex flex-col w-full">
    <div class="rt-Box flex flex-col p-6 rounded-xl overflow-x-auto border border-slate-4 bg-slate-2 items-center justify-center w-full">
        <button class="rt-reset rt-BaseButton rt-r-size-2 rt-variant-solid rt-Button" data-accent-color="" data-disabled="true" disabled="">
            <span class="rt-Spinner rt-r-size-2">
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
                <span class="rt-SpinnerLeaf"></span>
            </span>Bookmark
        </button>
    </div>
    <div class="rt-Box relative mb-4">
        <div class="rt-Box code-block css-1islnds">
            <pre class="shiki one-dark-pro" style="background-color:#282c34;color:#abb2bf" tabindex="0">
<code>
rx.button(
    rx.spinner(loading=True, "Bookmark", disabled=True)
)
</code></pre>
        </div>
    </div>
</a>

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/spinner/#rx.spinner)

# rx.spinner
A spinner component.

Test

- **Prop**: size  
  - **Type | Values**: "1" | "2" | ...  
  - **Default**: None  
  - **Interactive**: Yes

- **Prop**: loading  
  - **Type | Values**: bool  
  - **Default**: false  
  - **Interactive**: No

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)