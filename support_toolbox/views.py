from flask import render_template, request, jsonify

from models import RobotWip
from . import db, app


@app.context_processor
def inject_robot_wip():
    robots = db.session.query(RobotWip).all()
    return dict(robot_wip=robots)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/<current_robot>')
def curren_robot(current_robot=None):

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

@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/create_mail')
def create_mail():
    return render_template('close_tictet.html')

if __name__ == "__main__":
    app.run()
