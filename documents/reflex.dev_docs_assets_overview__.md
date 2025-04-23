# Assets

Static files such as images and stylesheets can be placed in `assets/` folder of the project. These files can be referenced within your app.

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic"><div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed"></div></div>

# Assets are copied during the build process.

# Referencing Assets

To reference an image in the `assets/` simply pass the relative path as a prop.

For example, you can store your logo in your assets folder:
```
assets
└── Reflex.svg
```

Then you can display it using a `rx.image` component:
![](https://reflex.dev/assets/Reflex.svg)

```python
rx.image(src="/Reflex.svg", width="5em")
```

Always prefix the asset path with a forward slash `/` to reference the asset from the root of the project, or it may not display correctly on non-root pages.

# Favicon

The favicon is the small icon that appears in the browser tab.

You can add a `favicon.ico` file to the `assets/` folder to change the favicon.