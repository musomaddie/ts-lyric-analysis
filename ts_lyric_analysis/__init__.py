import os

from . import db
from . import song
from flask import Flask

def create_app(test_config=None):
    """ Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY="dev",
            DATABASE=os.path.join(app.instance_path, "ts_lyric_analysis"),
    )

    if test_config is None:
        # Load the instance config
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(song.bp)
    db.init_app(app)

    return app
