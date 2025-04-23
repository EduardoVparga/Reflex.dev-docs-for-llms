# Script

The Script component can be used to include inline JavaScript or JavaScript files by URL.

It uses the `next/script` component to inject the script and can be safely used with conditional rendering to allow script side effects to be controlled by the state.

```python
rx.script("console.log('inline javascript')")
```

Complex inline scripting should be avoided. If the code to be included is more than a couple lines, it is more maintainable to implement it in a separate JavaScript file in the `assets` directory and include it via the `src` prop.

```python
rx.script(src="/my-custom.js")
```

This component is particularly helpful for including tracking and social scripts. Any additional attrs needed for the script tag can be supplied via `custom_attrs` prop.

```python
rx.script(
    src="//gc.zgo.at/count.js",
    custom_attrs={
        "data-goatcounter": "https://reflextoys.goatcounter.com/count"
    }
)
```

This code renders to something like the following to enable stat counting with a third party service.

```html
<script src="//gc.zgo.at/count.js" data-goatcounter="https://reflextoys.goatcounter.com/count" data-nscript="afterInteractive"></script>
```

# API Reference

[API Reference](/docs/library/other/script/#rx.script)

# rx.script

Next.js script component.

Note that this component differs from reflex.components.base.document.NextScript
in that it is intended for use with custom and user-defined scripts.
It also differs from reflex.components.base.link.ScriptTag, which is the plain
HTML `<script>` tag which does not work when rendering a component.

```python
Note that this component differs from reflex.components.base.document.NextScript
in that it is intended for use with custom and user-defined scripts.
It also differs from reflex.components.base.link.ScriptTag, which is the plain
HTML <script> tag which does not work when rendering a component.
```

## Props

- **Prop**: `src`
  - **Type | Values**: `str`
  - **Default**: None

- **Prop**: `strategy`
  - **Type | Values**: `"afterInteractive" | "beforeInteractive" | ...`
  - **Default**: `( LiteralVar.create("afterInteractive") )`

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_load`
  - Description: Triggered when the script is loading

- **Trigger**: `on_ready`
  - Description: Triggered when the script has loaded

- **Trigger**: `on_error`
  - Description: Triggered when the script has errored