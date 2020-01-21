from flask import Flask, jsonify
from flask_restplus import Resource, Api

# declare app instance
app = Flask(__name__)
# add api to app
api = Api(app)

# set app config using object we declared
app.config.from_object('project.config.DevelopmentConfig')

# declare simple ping class
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Somebody poisoned the water hole'
        }


# add ping resource to app
api.add_resource(Ping, '/ping')