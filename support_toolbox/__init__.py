from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
# db.create_all()
db.session.commit()

from . import views