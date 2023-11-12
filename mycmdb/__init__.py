from collections.abc import Mapping
from pathlib import Path
from typing import Any, Optional

import click
import flask.cli
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app(test_config: Optional[Mapping[str, Any]] = None) -> Flask:
    """Application factory."""

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite3+pysqlite:///database.sqlite3",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    Path(app.instance_path).mkdir(exist_ok=True)

    # initialize Flask-SQLAlchemy and the init-db command
    db.init_app(app)
    app.cli.add_command(init_db_command)

    return app


def init_db() -> None:
    db.drop_all()
    db.create_all()


@click.command("init-db")
@flask.cli.with_appcontext
def init_db_command() -> None:
    init_db()
    click.echo("Database initialized")
