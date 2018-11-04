from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:St4rtr3krul3s1!@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.model):

    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    body = db.Column(db.String(1000))
     created = db.Column(db.DateTime)
    
    def __init__(self, name):
        self.name = name
		self.body = body

@app.route('/build-a-blog', methods=['POST', 'GET'])
def is_valid(self):
	if self.title and self.body and self.created:
		return True
	else:
		return False

@app.route("/")
def index():
	return redirect("/blog")
@app.route("/blog")
def display_blog_entries():
	entry_id = request.args.get('id')
	if (entry_id):
		      entry = Entry.query.get(entry_id)
        return render_template('single_entry.html', title="Blog Entry", entry=entry)

    sort = request.args.get('sort')
    if (sort=="newest"):
        all_entries = Entry.query.order_by(Entry.created.desc()).all()
    else:
        all_entries = Entry.query.all()   
