from app.routes.tricks import api as tricks
from flask_restplus import Api
from flask import Blueprint


blueprint = Blueprint('api', __name__)
api = Api(blueprint, title="my blueprint", doc="/doc/")

api.add_namespace(tricks, path="/")