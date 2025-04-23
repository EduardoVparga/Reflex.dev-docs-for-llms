# Base

The base class subclassed by all Reflex classes.

This class wraps Pydantic and provides common methods such as serialization and setting fields.

Any data structure that needs to be transferred between the frontend and backend should subclass this class.

- [Methods](https://reflex.dev/docs/api-reference/base/#methods)

# Methods

## Signature
```python
json(self) -> 'str'
```
Convert the object to a json string.

## Description
Set multiple fields and return the object.
```python
set(self, **kwargs: 'Any')
```

## Signature
```python
get_fields(cls) -> 'dict[str, ModelField]'
```
Get the fields of the object.

## Description
Add a pydantic field after class definition.

        Used by State.add_var() to correctly handle the new variable.
```python
add_field(cls, var: 'Var', default_value: 'Any')
```

## Signature
```python
get_value(self, key: 'str') -> 'Any'
```
Get the value of a field.