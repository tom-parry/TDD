import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api



# instantiate DB
db = SQLAlchemy()

def create_app(script_info=None):
    # instantiate app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # extensions
    db.init_app(app)

    # create db tables
    with app.app_context():
        db.create_all()

    # register blueprints
    from project.api.ping import ping_blueprint
    app.register_blueprint(ping_blueprint)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app