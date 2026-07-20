from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
    app.config['SECRET_KEY'] = 'secret_key'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp as routes_bp
    from .forms import LoginForm

    app.register_blueprint(routes_bp)

    return app


db = SQLAlchemy()
migrate = Migrate()

app = create_app()