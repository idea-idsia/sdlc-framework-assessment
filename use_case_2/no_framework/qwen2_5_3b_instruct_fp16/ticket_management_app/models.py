from flask_security import Security, SQLAlchemyUserDatastore

user_datastore = SQLAlchemyUserDatastore(db.session, User, TicketMessages)
security = Security(app, user_datastore)