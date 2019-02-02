from app import db
from flask import Flask


def create_app(config_file):
    app = Flask(__name__)

    # TODO: Modularize.
    app.config.from_pyfile("defaultcfg.py")

    _setup_db(app)
    return app


def _setup_db(app):
    db.init_app(app)


def _register_blueprints(app):
    pass
