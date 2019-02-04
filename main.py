from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bb826f7f473246:d3cc1772@us-cdbr-iron-east-01.cleardb.net/heroku_459e9faa50531d7'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(1000))
    
    def __init__(self, title, content):
        self.title = title
        self.content = content

@app.route('/build-a-blog', methods=['POST', 'GET'])
def is_valid(self):
	if self.title and self.content:
		return True
	else:
		return False

@app.route("/")
def index():
	return redirect("/blog")


@app.route("/blog")
def display_blog_entries():
    entry_id = request.args.get('id')
    if(entry_id):
        entry = Blog.query.get(entry_id)
        return render_template('single_entry.html', title="Blog Entry", entry=entry)
    sort = request.args.get('sort')
    if (sort == 'newest'):
        all_entries = Blog.query.order_by(Entry.created.desc()).all()
    else:
        all_entries = Blog.query.all()


if __name__ == "__main__":
    app.run()