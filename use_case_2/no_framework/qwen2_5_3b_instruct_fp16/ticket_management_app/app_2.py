from config import Config

application = Flask(__name__)
application.config.from_object(Config)
db.init_app(application)
init_db()

@application.route('/tickets/status/open/count/<int:days>', methods=['GET'])
def status_open_count(days):
    return jsonify({'count': count_open_tickets(days)})

# Implement routes for other microservices