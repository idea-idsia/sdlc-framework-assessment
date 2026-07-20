from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/tickets/period', methods=['GET'])
def tickets_period():
    hours = int(request.args.get('hours'))
    # Query the database to get tickets opened in last X hours that are not closed.
    return "Number of open tickets"

if __name__ == '__main__':
    app.run(debug=True, port=5001)