from flask import Flask
from flask_restful import Api
from application.db import init_db
from application.app import User, Users


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    init_db(app)

    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')

    return app
