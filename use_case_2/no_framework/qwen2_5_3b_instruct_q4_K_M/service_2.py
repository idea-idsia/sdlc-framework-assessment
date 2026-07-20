from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/tickets/average-resolve-time', methods=['GET'])
def average_resolve_time():
    month = request.args.get('month')

    if not month:
        return jsonify({"error": "Month is required"}), 400

    # Fetch tickets for the given month and calculate resolution time
    # Example logic goes here (fetching data, calculating, etc.)
    average_resolve_time = None

    return jsonify({"average_resolve_time": average_resolve_time}), 200