import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Resource, Api

# declare app instance
app = Flask(__name__)
# add api to app
api = Api(app)


# get app settings from ENV variable
app_settings=os.getenv('APP_SETTINGS')
# configure app using app settings
app.config.from_object(app_settings)

# instantiate DB
db = SQLAlchemy(app)

# schema for users table, extends SQLAlchemy model
class User(db.Model):
    # table name
    __tablename__ = 'users'
    # columns set up
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    # init function
    def __init__(self, username, email):
        self.username = username
        self.email = email

# declare simple ping class
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Somebody poisoned the water hole'
        }

# add ping resource to app
api.add_resource(Ping, '/ping')