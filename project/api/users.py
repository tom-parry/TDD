from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

from project import db
from project.api.models import User

# create blueprint & add it to api
users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

# use api.model factory pattern to instantiate & register user model to API
user = api.model('User', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'created_date': fields.DateTime,
})


class UsersList(Resource):
    # attach model to method & use it to validate payload
    @api.expect(user, validate=True)
    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        response_object = {}
        print("email:" + str(email))

        user = User.query.filter_by(email=email).first()
        if user:
            response_object['message'] = 'Sorry. That email already exists.'
            return response_object, 400

        db.session.add(User(username=username, email=email))
        db.session.commit()
        response_object = {
            'message': f'{email} was added!'
        }
        return response_object, 201

    # use model as serializer to generate a JSON object with fields from the model
    # as_list=True: we want to return a list of objects instead of a single object
    @api.marshal_with(user, as_list=True)
    def get(self):
        return User.query.all(), 200


class Users(Resource):
    # use model as a serializer to generate a JSON object with fields from the model
    @api.marshal_with(user)
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            api.abort(404, f"User {user_id} does not exist")
        return user, 200


api.add_resource(UsersList, '/users')
api.add_resource(Users, '/users/<int:user_id>')
