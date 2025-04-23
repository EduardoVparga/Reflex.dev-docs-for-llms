# Fragment
A Fragment is a Component that allows you to group multiple Components without a wrapper node.
Refer to the React docs at [React/Fragment](https://react.dev/reference/react/Fragment) for more information on its use-case.

Component1  
Component2

```python
rx.fragment(rx.text("Component1"), rx.text("Component2"))
```
<button>
<svg class="lucide lucide-copy" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg>
</button>

<div data-orientation="vertical" data-variant="classic">
<div class="AccordionItem" data-orientation="vertical" data-state="closed">
```

# Video: Fragment

[Reflex.dev Docs](https://reflex.dev/docs/library/layout/fragment/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/layout/fragment/#rx.fragment)

# rx.fragment

A React fragment to return multiple components from a function without wrapping it in a container.

<div class="rt-Box flex flex-col overflow-x-auto justify-start py-2 w-full"></div>

Props
No component specific props

<div class="rt-Box py-2 overflow-x-auto justify-start flex flex-col gap-4">

# Event Triggers

[See the full list of default event triggers](https://reflex.dev/docs/api-reference/event-triggers/)