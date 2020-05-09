# Database table

from app import db

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