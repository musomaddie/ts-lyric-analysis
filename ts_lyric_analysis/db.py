import click
import sqlite3

from flask import current_app, g
from flask.cli import with_appcontext
from ts_lyric_analysis.database.init_helper import populate_albums
from ts_lyric_analysis.database.init_helper import populate_songs

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
                current_app.config["DATABASE"],
                detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    """ Initialises the database. Adds the song information as well as the
    empty tables.
    """
    db = get_db()
    # Create the empty tables
    with current_app.open_resource("database/schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    populate_albums(db)
    populate_songs(db, "Taylor Swift")
    populate_songs(db, "Fearless")
    populate_songs(db, "Speak Now")
    populate_songs(db, "Red")

@click.command("init-db")
@with_appcontext
def init_db_command():
    """ Clear the existing data and create new tables. """
    click.echo("Beginning the initialisation of the database")
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """ Register database functions with the Flask app. This is called by the
    application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
