from flask import Flask
from app.routes import blueprint as api
from db import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL', 'postgresql://ecom-vinoj.kannan@localhost:5432/mydb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.before_first_request
def create_tables():
  db.create_all()

app.register_blueprint(api)


db.init_app(app)

port = os.getenv('APP_PORT', '5000')
app.run(port=port)

