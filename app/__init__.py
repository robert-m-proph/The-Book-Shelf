# app/__init__.py
# Main initialization for app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


#from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'authentication.sign_in_user'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

# developemnt, testing, production
def create_app(config_type):
    app = Flask(__name__)
    #csrf = CSRFProtect(app)
    configuration = os.path.join(os.getcwd(),'config',config_type + '.py')

    # Loading configuration
    app.config.from_pyfile(configuration)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    # Passing flask application instance to database
    db.init_app(app)

    # Initializing bootstrap
    bootstrap.init_app(app)
    
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    # importing and registering blueprint
    from app.catalog import main
    app.register_blueprint(main)

    from app.authentication import authentication
    app.register_blueprint(authentication)

    return app