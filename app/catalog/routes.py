# app/catalog/routes.py
# Setting the routes to render pages

from app.catalog import main
from app import db
from app.catalog.models import Book
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required



@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('index.html', books=books)