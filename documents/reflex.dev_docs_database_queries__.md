# Queries

Queries are used to retrieve data from a database.

A query is a request for information from a database table or combination of tables. A query can be used to retrieve data from a single table or multiple tables. A query can also be used to insert, update, or delete data from a table.

[Learn more](https://reflex.dev/docs/database/queries/#session)

# Session

To execute a query you must first create a `rx.session`. You can use the session to query the database using SQLModel or SQLAlchemy syntax.

The `rx.session` statement will automatically close the session when the code block is finished. If `session.commit()` is not called, the changes will be rolled back and not persisted to the database. The code can also explicitly rollback without closing the session via `session.rollback()`.

The following example shows how to create a session and query the database. First we create a table called `User`.

```python
class User(rx.Model, table=True):
    username: str
    email: str
```

For more information, see [Querying](https://reflex.dev/docs/database/queries/#select).

# Select

Then we create a session and query the User table.

```python
class QueryUser(rx.State):
    name: str
    users: list[User]

    @rx.event
    def get_users(self):
        with rx.session() as session:
            self.users = session.exec(
                User.select().where(
                    User.username.contains(self.name)
                )
            ).all()
```

The `get_users` method will query the database for all users that contain the value of the state var `name`. 

[![Copy](https://reflex.dev/assets/copy-8201d0f32e95640f7e5063a97c3b60e6.svg)](https://reflex.dev/docs/database/queries/#insert)

# Insert

Similarly, the `session.add()` method to add a new record to the database or persist an existing object.

```python
class AddUser(rx.State):
    username: str
    email: str

    @rx.event
    def add_user(self):
        with rx.session() as session:
            session.add(
                User(
                    username=self.username, 
                    email=self.email
                )
            )
            session.commit()
```

[![Copy](https://reflex.dev/docs/database/queries/#update)](https://reflex.dev/docs/database/queries/#update)

# Update

To update the user, first query the database for the object, make the desired modifications, `.add` the object to the session and finally call `.commit()`.

```python
class ChangeEmail(rx.State):
    username: str
    email: str

    @rx.event
    def modify_user(self):
        with rx.session() as session:
            user = session.exec(
                User.select().where(
                    (User.username == self.username)
                )
            ).first()
            user.email = self.email
            session.add(user)
            session.commit()
```

[![Copy](https://raw.githubusercontent.com/alibabacloud-sdk/Qwen/main/docs/copy_icon.svg)](javascript:void(0))

# Delete

To delete a user, first query the database for the object, then call `.delete()` on the session and finally call `.commit()`.

```python
class RemoveUser(rx.State):
    username: str

    @rx.event
    def delete_user(self):
        with rx.session() as session:
            user = session.exec(User.select().where(User.username == self.username)).first()
            session.delete(user)
            session.commit()
```

[![](https://assets.reflex.dev/toolbar/copy_icon.svg)](https://reflex.dev/docs/database/queries/#orm-object-lifecycle)

# ORM Object Lifecycle

The objects returned by queries are bound to the session that created them, and cannot generally be used outside that session. After adding or updating an object, not all fields are automatically updated, so accessing certain attributes may trigger additional queries to refresh the object.

To avoid this, the `session.refresh()` method can be used to update the object explicitly and ensure all fields are up to date before exiting the session.

```python
class AddUserForm(rx.State):
    user: User | None = None

    @rx.event
    def add_user(self, form_data: dict[str, Any]):
        with rx.session() as session:
            self.user = User(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)
```

Now the `self.user` object will have a correct reference to the auto-generated primary key, `id`, even though this was not provided when the object was created from the form data.

If `self.user` needs to be modified or used in another query in a new session, it must be added to the session. Adding an object to a session does not necessarily create the object, but rather associates it with a session where it may either be created or updated accordingly.

```python
class AddUserForm(rx.State):
    ...

    @rx.event
    def update_user(self, form_data: dict[str, Any]):
        if self.user is None:
            return
        with rx.session() as session:
            self.user.set(**form_data)
            session.add(self.user)
            session.commit()
            session.refresh(self.user)
```

If an ORM object will be referenced and accessed outside of a session, you should call `.refresh()` on it to avoid stale object exceptions.

# Using SQL Directly

Avoiding SQL is one of the main benefits of using an ORM, but sometimes it is necessary for particularly complex queries, or when using database-specific features.

SQLModel exposes the `session.execute()` method that can be used to execute raw SQL strings. If parameter binding is needed, the query may be wrapped in [sqlalchemy.text](https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.text), which allows colon-prefix names to be used as placeholders.

Never use string formatting to construct SQL queries, as this may lead to SQL injection vulnerabilities in the app.

```python
import sqlalchemy

import reflex as rx

class State(rx.State):
    @rx.event
    def insert_user_raw(self, username: str, email: str):
        with rx.session() as session:
            session.execute(
                sqlalchemy.text(
                    "INSERT INTO user (username, email) VALUES (:username, :email)"
                ),
                {"username": username, "email": email},
            )
            session.commit()

    @rx.var
    def raw_user_tuples(self) -> list[list]:
        with rx.session() as session:
            return [
                list(row)
                for row in session.execute("SELECT * FROM user").all()
            ]
```
```