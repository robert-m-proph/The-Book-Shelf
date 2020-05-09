# Main python file to run application

from app import create_app, db
from app.authentication.models import User

if __name__ == '__main__':
    flask_app = create_app('development')
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='robert').first():
            User.create_user(user='robert',email='robert@emailaddress.com',password='secrete')
            
    flask_app.run()