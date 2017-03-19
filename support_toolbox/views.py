from flask import render_template, request, jsonify
from flask_socketio import  emit

from models import RobotWip, RobotLog
from . import db, app, socketio
thread = None


# add robot wip list to as a global var
@app.context_processor
def inject_robot_wip():
    robots = db.session.query(RobotWip).all()
    return dict(robot_wip=robots)


def background_thread():
    """Send server generated event to clients"""
    while True:
        running_robots = []
        robot_log = db.session.query(RobotLog).filter(RobotLog.end_time == None).all()
        for robot in robot_log:
            running_robots.append(robot.robot_name)

        # json_data = json.dumps([i.serialize for i in robot_log])[0]
        # print json_data
        socketio.sleep(10)
        socketio.emit('my_response',
                      running_robots,
                      namespace='/test')


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@app.route('/')
def home():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/<current_robot>')
def curren_robot(current_robot=None):
    # add current clicked robot as global...
    # @app.context_processor
    # def inject_current_robot():
    #     current_r = current_robot
    #     return dict(current_r=current_r)
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
