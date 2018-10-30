from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:St4rtr3krul3s1!@localhostz:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.model):

    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    
    def __init__(self, name):
        self.name = name

tasks = []



@app.route('/build-a-blog', methods=['POST', 'GET'])
def build_a_blog():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('main.html', title="BuildABlog")

    