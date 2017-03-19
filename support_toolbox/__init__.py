from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.session.commit()
socketio = SocketIO(app, async_mode=async_mode)
thread = None


from . import views
