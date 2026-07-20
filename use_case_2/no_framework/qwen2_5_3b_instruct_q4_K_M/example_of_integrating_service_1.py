from flask import Flask
import requests

app = Flask(__name__)


@app.route('/api/tickets/open-count', methods=['POST'])
def open_tickets_count():
    start_date_str = request.json.get('start_date')
    end_date_str = request.json.get('end_date')

    # Call the microservice to get count of open tickets in a period
    response = requests.post("http://microservice-service1:5000/tickets/open-count",
                             json={"start_date": start_date_str, "end_date": end_date_str})

    data = response.json()
    return jsonify(data), 200


if __name__ == '__main__':
    socketio.run(app, debug=True)