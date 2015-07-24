# -*- coding: utf-8 -*-
from flask import Flask

from .extensions import db
from .person.views import person_bp


def create_app():
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///database.db'
    )

    register_extensions(app)
    register_bluenprints(app)

    create_database(app)
    return app


def register_extensions(app):
    db.init_app(app)


def register_bluenprints(app):
    app.register_blueprint(person_bp, url_prefix='/api/persons')


def create_database(app):
    from .person.models import Person  # noqa
    with app.app_context():
        db.create_all()
