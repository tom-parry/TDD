import os
from flask import Flask, jsonify
from flask_restplus import Resource, Api

# declare app instance
app = Flask(__name__)
# add api to app
api = Api(app)


# get app settings from ENV variables
app_settings=os.getenv('APP_SETTINGS')
# configure app using app settings
app.config.from_object(app_settings)

# declare simple ping class
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Somebody poisoned the water hole'
        }

# add ping resource to app
api.add_resource(Ping, '/ping')