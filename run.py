# Robert M. Propheter
# run.py is the main python file for "The Book Shelf" project

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ====================  Database Info ====================
app.config.update(
    SECRET_KEY='!Loki1209',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:!Loki1209@localhost/catalog_db',
    # Below is the "template" for the database URI
    # SQLALCHEMY_DATABASE_URI='<database>://<user_id>:<password>@<server>/<database_name>',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

# Creating an instance of the db
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(500))
    book_format = db.Column(db.String(500))
    num_pages = db.Column(db.Integer)
    isbn = db.Column(db.Integer)

    def __init__(self, title, author, book_format, num_pages, isbn):
        self.title = title
        self.author = author
        self.book_format = book_format
        self.num_pages = num_pages
        self.isbn = isbn
    
    def __repr__(self):
        return '{} written by {}'.format(self.title, self.author)



# ====================  ROUTES  ==================== 
@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hello World!'

# Using Templates
@app.route('/home')
def using_templates():
    return render_template('default.html')

# Using Jinja in the html
@app.route('/practice')
def top_movies():
    movie_dict = {
        'Saving Private Ryan': 02.14,
        'Outerbanks': 3.20,
        '13 Ghost': 1.50 ,
        'Menace to Society': 3.50
        }  
    return render_template('practice.html', movies=movie_dict, name='Robert')



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)