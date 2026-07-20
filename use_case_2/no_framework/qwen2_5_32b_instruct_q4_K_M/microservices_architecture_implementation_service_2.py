from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/tickets/average_resolution_time', methods=['GET'])
def average_resolution_time():
    # Query the database to get average resolution time by month.
    return "Average resolution times"

if __name__ == '__main__':
    app.run(debug=True, port=5002)