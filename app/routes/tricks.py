from flask_restplus import Namespace, Resource
from app.service.tricks_service import TricksService
from flask import request

tricks_service = TricksService()
api = Namespace('Trickss')


@api.route('')
class Home(Resource):
  def get(self):
    '''Home Route'''
    tricks = tricks_service.getTricks()
    return tricks

@api.route('tricks')
class Tricks(Resource):
  def get(self):
    tricks = tricks_service.getTricks()
    return tricks
  def post(self):
    trick = request.json
    result = tricks_service.addTrick(trick)
    return result.json()

@api.route('trick/<trick_id>')
class Trick(Resource):
  def get(self, trick_id):
    result = tricks_service.getTrick(trick_id)
    if result is None:
      return 'Trick not found', 404
    return result.json()
  def put(self, trick_id):
    trick = request.json
    result = tricks_service.editTrick(trick_id, trick)
    if result is None:
      return 'Trick not found', 404
    return f'modified {trick_id}'
  def delete(self, trick_id):
    result = tricks_service.deleteTrick(trick_id)
    if result is None:
      return 'Trick not found', 404
    return f'deleted {trick_id}'