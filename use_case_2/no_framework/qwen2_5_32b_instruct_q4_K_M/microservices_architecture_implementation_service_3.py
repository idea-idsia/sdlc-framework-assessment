from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/tickets/cluster_by_category', methods=['GET'])
def cluster_by_category():
    # Query the database to get number of active tickets per category.
    return "Number of active tickets by category"

if __name__ == '__main__':
    app.run(debug=True, port=5003)