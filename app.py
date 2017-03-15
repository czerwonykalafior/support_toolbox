from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

from models import RobotWip

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:zajzajer@127.0.0.1:5432/support_toolbox'
db = SQLAlchemy(app)
db.create_all()
db.session.commit()

@app.context_processor
def inject_robot_wip():
    robots = db.session.query(RobotWip).all()
    return dict(robot_wip=robots)


@app.route('/')
@app.route('/<current_robot>')
def home(current_robot=None):

    @app.context_processor
    def inject_current_robot():
        current_r = current_robot
        return dict(current_r=current_r)
    return render_template('robot_logs.html')


@app.route('/robot_logs')
def robot_logs():
    return render_template('robot_logs.html')

@app.route('/category_structure')
def category_structure():
    return render_template('category_structure.html')

@app.route('/gans_sql')
def gans_sql():
    return render_template('gans_sql.html')

@app.route('/robot_error')
def robot_error():
    return render_template('robot_error.html')

@app.route('/dq_issues')
def dq_issues():
    return render_template('dq_issues.html')

@app.route('/robot_extraction_stats')
def robot_extraction_stats():
    return render_template('robot_extraction_stats.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/create_mail')
def create_mail():
    return render_template('close_tictet.html')

if __name__ == "__main__":
    app.run()
