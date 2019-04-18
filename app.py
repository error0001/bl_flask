from flask import Flask , render_template, request
from flask_sqlalchemy import  SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/andrey/PycharmProjects/bl_fls/blog.db'

db = SQLAlchemy(app)


class Blogpost(db.Model):
    # see the guide with flask sqlalchemy
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addpost')
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    return '<h1>Title: {} Subtitle: {} Author: {} Content: {}</h1>'.format(
        title,
        subtitle,
        author,
        content
    )


if __name__ == '__main__':
    app.run()
