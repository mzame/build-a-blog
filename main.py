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


@app.route("/")
def index():
    return redirect("/blogs")


@app.route("/blogs")
def display_blog_entries():
    blog_id = request.args.get('id')
    if(blog_id):
        entry = Blog.query.get(blog_id)
        return render_template('single_entry.html', title="Blog Entry", entry=entry)

    all_entries = Blog.query.all()
    return render_template('all_entries.html', entries=all_entries)


if __name__ == "__main__":
    app.run()
