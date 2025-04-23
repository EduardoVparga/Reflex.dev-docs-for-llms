# Moment

Displaying date and relative time to now sometimes can be more complicated than necessary.

To make it easy, Reflex is wrapping `react-moment` under `rx.moment`.

[Reflex Documentation](https://reflex.dev/docs/library/data-display/moment/#examples)

# Examples

Using a date from a state var as a value, we will display it in a few different way using `rx.moment`.

The `date_now` state var is initialized when the site was deployed. The button below can be used to update the var to the current datetime, which will be reflected in the subsequent examples.

[Update](<time datetime="1744765000278">Tue Apr 15 2025 20:56:40 GMT-0400</time>)

```python
from datetime import datetime, timezone

class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    @rx.event
    def update(self):
        self.date_now = datetime.now(timezone.utc)

def moment_update_example():
    return rx.button(
        "Update",
        rx.moment(MomentState.date_now),
        on_click=MomentState.update,
    )
```

[![Copy](<svg class="lucide lucide-copy css-cqk0y8" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><rect height="14" rx="2" ry="2" width="14" x="8" y="8"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg>)](https://reflex.dev/docs/library/data-display/moment/#display-the-date-as-is:)

# Display the date as-is:
Tue Apr 15 2025 20:56:40 GMT-0400

```python
rx.moment(MomentState.date_now)
```

[Link to Reflex.dev](https://reflex.dev/docs/library/data-display/moment/#humanized-interval)

# Humanized interval

Sometimes we don't want to display just a raw date, but we want something more instinctive to read. That's when we can use `from_now` and `to_now`.

## Example 1: from_now
a day ago

```python
rx.moment(MomentState.date_now, from_now=True)
```

## Example 2: to_now
in a day

```python
rx.moment(MomentState.date_now, to_now=True)
```

You can also set a duration (in milliseconds) with `from_now_during` where the date will display as relative, then after that, it will be displayed as defined in `format`.

## Example 3: from_now_during
Tue Apr 15 2025 20:56:40 GMT-0400

```python
rx.moment(
    MomentState.date_now, 
    from_now_during=100000
)  # after 100 seconds, date will display normally
```

[Learn more about formatting dates](https://reflex.dev/docs/library/data-display/moment/#formatting-dates)

# Formatting dates

## 2025-04-15

```python
rx.moment(MomentState.date_now, format="YYYY-MM-DD")
```

## 20:56:40

```python
rx.moment(MomentState.date_now, format="HH:mm:ss")
```

# Offset Date

With the props `add` and `subtract`, you can pass an `rx.MomentDelta` object to modify the displayed date without affecting the stored date in your state.

## Add

- 2027-04-15 - 20:56:40
- 2025-10-15 - 20:56:40
- 2025-06-15 - 20:56:40
- 2025-06-15 - 20:56:40
- 2025-06-15 - 20:56:40
- 2025-04-29 - 20:56:40
- 2025-04-17 - 20:56:40
- 2025-04-15 - 22:56:40
- 2025-04-15 - 20:58:40
- 2025-04-15 - 20:56:42

```python
rx.vstack(
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(years=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(quarters=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(months=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(months=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(months=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(weeks=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(days=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(hours=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(minutes=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
    rx.moment(
        MomentState.date_now,
        add=rx.MomentDelta(seconds=2),
        format="YYYY-MM-DD - HH:mm:ss",
    ),
)
```

## Subtract
- (Content is not provided)

# Timezones

You can also set dates to display in a specific timezone:

- Tue Apr 15 2025 17:56:40 GMT-0700
- Wed Apr 16 2025 02:56:40 GMT+0200
- Wed Apr 16 2025 09:56:40 GMT+0900

```python
rx.vstack(
    rx.moment(MomentState.date_now, tz="America/Los_Angeles"),
    rx.moment(MomentState.date_now, tz="Europe/Paris"),
    rx.moment(MomentState.date_now, tz="Asia/Tokyo"),
)
```

For more information, see [Reflex Docs](https://reflex.dev/docs/library/data-display/moment/#client-side-periodic-update)

# Client-side periodic update

If a date is not passed to `rx.moment`, it will use the client's current time.

If you want to update the date every second, you can use the `interval` prop.

Even better, you can actually link an event handler to the `on_change` prop that will be called every time the date is updated:

```python
class MomentLiveState(rx.State):
    updating: bool = False

    @rx.event
    def on_update(self, date):
        return rx.toast(f"Date updated: {date}")

def moment_live_example():
    return rx.hstack(
        rx.moment(
            format="HH:mm:ss",
            interval=rx.cond(MomentLiveState.updating, 5000, 0),
            on_change=MomentLiveState.on_update,
        ),
        rx.switch(
            is_checked=MomentLiveState.updating,
            on_change=MomentLiveState.set_updating,
        ),
    )
```

For more information, see [moment API reference](https://reflex.dev/docs/library/data-display/moment/#api-reference)

# API Reference

[API Reference](https://reflex.dev/docs/library/data-display/moment/#rx.moment)

# rx.moment

The Moment component.

## Props

| Prop            | Type | Default  |
|-----------------|------|----------|
| interval        | int  |          |
| format          | str  |          |
| trim            | bool |          |
| parse           | str  |          |
| add             | MomentDelta |       |
| subtract        | MomentDelta |       |
| from_now        | bool |          |
| from_now_during | int  |          |
| to_now          | bool |          |
| with_title      | bool |          |
| title_format    | str  |          |
| diff            | str  |          |
| decimal         | bool |          |
| unit            | str  |          |
| duration        | str  |          |
| date            | Union[str, datetime, date, time, timedelta] | |
| duration_from_now | bool |          |
| unix            | bool |          |
| local           | bool |          |
| tz              | str  |          |
| locale          | str  |          |

# Event Triggers

See the full list of default event triggers [here](https://reflex.dev/docs/api-reference/event-triggers/)

- **Trigger**: `on_change`
  - Description: Fires when the date changes.