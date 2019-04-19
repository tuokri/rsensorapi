import app

from flask import Flask

from app import blueprints
from db import db


def create_app(config_file=app.DEFAULTCFG):
    app = Flask(__name__)

    try:
        app.config.from_pyfile(config_file)
    except EnvironmentError as ee:
        app.config.from_pyfile(app.DEFAULTCFG)

    _setup_db(app)
    _register_blueprints(app)

    return app


def _setup_db(app):
    db.init_app(app)


def _register_blueprints(app):
    app.register_blueprint(blueprints.api_bp, url_prefix="/api")
