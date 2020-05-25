from flask import Flask
from app.routes import blueprint as api
from db import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://ecom-vinoj.kannan@localhost:5432/mydb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.before_first_request
def create_tables():
  db.create_all()

app.register_blueprint(api)
db.init_app(app)

if __name__ == '__main__':
  app.run()

