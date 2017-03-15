import flask
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

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
    return render_template('create_mail.html')

if __name__ == "__main__":
    app.run()
