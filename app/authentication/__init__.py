# app/authentication/__init__.py
# Main initialization for log in

from flask import Blueprint

authentication = Blueprint('authentication',__name__,template_folder='templates')

from app.authentication import routes