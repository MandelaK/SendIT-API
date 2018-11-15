from flask import Flask
# we import created blueprints to register them
from .api.v1 import version1


def create_app():
    """This is our app factory from where we register our app and
    API version"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    # we register the blueprint
    app.register_blueprint(version1)
    # register more blueprints in a similar manner

    return app

