# Database

Reflex uses [sqlmodel](https://sqlmodel.tiangolo.com) to provide a built-in ORM wrapping SQLAlchemy.

The examples on this page refer specifically to how Reflex uses various tools to expose an integrated database interface. Only basic use cases will be covered below, but you can refer to the [sqlmodel tutorial](https://sqlmodel.tiangolo.com/tutorial/select/) for more examples and information, just replace `SQLModel` with `rx.Model` and `Session(engine)` with `rx.session()`.

For advanced use cases, please see the [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/orm/quickstart.html) (v1.4).

<div class="css-116ytrl" data-orientation="vertical" data-variant="classic">
    <div class="AccordionItem css-1g1zb7l" data-orientation="vertical" data-state="closed">
    </div>
</div>

# Using NoSQL Databases

--- 

[Connecting to a Database](https://reflex.dev/docs/database/overview/#connecting)

# Connecting

Reflex provides a built-in SQLite database for storing and retrieving data.

You can connect to your own SQL compatible database by modifying the `rxconfig.py` file with your database url.

```python
config = rx.Config(
    app_name="my_app",
    db_url="sqlite:///reflex.db",
)
```

For more examples of database URLs that can be used, see the [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/core/engines.html#backend-specific-urls).
Be sure to install the appropriate DBAPI driver for the database you intend to use.

[Learn More](https://reflex.dev/docs/database/overview/#tables)

# Tables

To create a table make a class that inherits from `rx.Model` with and specify that it is a table.

```python
class User(rx.Model, table=True):
    username: str
    email: str
    password: str
```

[Link to Reflex documentation](https://reflex.dev/docs/database/overview/#migrations)

# Migrations

Reflex leverages [alembic](https://alembic.sqlalchemy.org/en/latest/) to manage database schema changes.

Before the database feature can be used in a new app you must call `reflex db init` to initialize alembic and create a migration script with the current schema.

After making changes to the schema, use `reflex db makemigrations --message 'something changed'` to generate a script in the `alembic/versions` directory that will update the database schema. It is recommended that scripts be inspected before applying them.

The `reflex db migrate` command is used to apply migration scripts to bring the database up to date. During app startup, if Reflex detects that the current database schema is not up to date, a warning will be displayed on the console.

# Queries

To query the database you can create a `rx.session()`
which handles opening and closing the database connection.

You can use normal SQLAlchemy queries to query the database.

```python
with rx.session() as session:
    session.add(
        User(
            username="test",
            email="admin@reflex.dev",
            password="admin"
        )
    )
    session.commit()
```

<div class="css-10ddbmu" data-orientation="vertical" data-variant="classic">
<div class="AccordionItem css-tzz23y" data-orientation="vertical" data-state="closed">
```

### Video: Tutorial of Database Model with Forms, Model Field Changes and Migrations, and adding a DateTime Field