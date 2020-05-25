from app.accessor.tricks_accessor import TricksAccessor


class TricksService:
  def getTricks(self):
    tricks = [trick.json() for trick in TricksAccessor.find_all()]
    return tricks, 200
  
  def getTrick(self, trickId):
    trick = TricksAccessor.find_by_id(trickId)
    return trick

  def addTrick(self, trick):
    trick = TricksAccessor(trick.get('title'), trick.get('content'))
    if trick is not None:
      trick.save_to_db()
    return trick

  def editTrick(self, id, newTrick):
    trick = TricksAccessor.find_by_id(id)
    if trick is not None:
      trick.title = newTrick.get('title')
      trick.content = newTrick.get('content')
      trick.save_to_db()
    return trick

  def deleteTrick(self, trickId):
    trick = TricksAccessor.find_by_id(trickId)
    if trick is not None:
      trick.delete_from_db()
    return trick
  
  def deleteTricks(self):
    TricksAccessor.delete_all()
    return