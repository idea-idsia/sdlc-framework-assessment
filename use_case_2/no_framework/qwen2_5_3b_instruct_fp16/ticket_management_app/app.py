from flask import Flask
from config import Config
from views import app as application


def create_app():
    # Initialize extensions like SQLAlchemy
    db.init_app(application)

    with application.app_context():
        init_db()  # Database initialization

    return application


if __name__ == '__main__':
    application = create_app()
    application.run(debug=True)