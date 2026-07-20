from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)  # 'facility', 'technical IT', 'services'
    status = db.Column(db.String(20), default='open')  # 'open', 'active', 'closed'
    opening_date = db.Column(db.DateTime, server_default=db.func.now())
    last_modification_date = db.Column(db.DateTime, onupdate=db.func.now(), nullable=True)
    closing_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Ticket {self.id}>'