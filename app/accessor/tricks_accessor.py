from db import db

class TricksAccessor(db.Model):
  __tablename__ = 'tricks'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80))
  content = db.Column(db.String(1000))


  def __init__(self, title, content):
      self.title = title
      self.content = content

  def json(self):
    return {
      'id': self.id,
      'title': self.title,
      'content': self.content
    }

  @classmethod
  def find_by_name(cls, name):
      return cls.query.filter_by(name=name).first()

  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).first()

  @classmethod
  def find_all(cls):
      return cls.query.all()

  def save_to_db(self):
      db.session.add(self)
      db.session.commit()

  def delete_from_db(self):
      db.session.delete(self)
      db.session.commit()

  @classmethod
  def delete_all(self):
    db.drop_all()