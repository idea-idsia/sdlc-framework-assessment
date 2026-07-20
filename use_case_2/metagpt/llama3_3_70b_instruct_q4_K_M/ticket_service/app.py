"""
This is the main application file for the ticket management system.

It initializes the Flask application instance, configures the database,
and imports the necessary routes from the routes module.
"""

from flask import Flask
from models import db
from routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_management.db'
db.init_app(app)

# Import and register the routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
