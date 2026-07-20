from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime, timedelta
app = Flask(__name__)
@app.route('/tickets/cluster', methods=['GET'])
def cluster_tickets_by_category():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    query = """
        SELECT strftime('%Y-%m', open_date) AS month, category
        FROM Tickets 
        GROUP BY strftime('%Y-%m', open_date), category
    """
    cursor.execute(query)
    results = []
    for row in cursor:
        date_str = datetime.strptime(row[0], "%Y-%m").strftime("%b '%y")
        if len(results) == 0 or results[-1][0] != (date_str,):
            results.append((date_str, [row[1]]))
        else:
            prev_category = results[-1][1][-1]
            found = False
            for i in range(len(results[-1][1])):
                if row[1] == prev_category:
                    results[-1][1][i] = (prev_category, results[-1][1].count(prev_category))
                    found = True
                    break
            if not found:
                results[-1][1].append((row[1], 1))
    conn.close()
    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)