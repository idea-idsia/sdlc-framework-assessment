from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/service3', methods=['GET'])
def service3():
    conn = get_db_connection()
    tickets = conn.execute('SELECT category, status FROM tickets WHERE status != ?',
                           ('closed',)).fetchall()
    conn.close()

    from collections import defaultdict
    active_tickets_by_category = defaultdict(int)

    for ticket in tickets:
        if ticket['status'] == 'active':
            active_tickets_by_category[ticket['category']] += 1

    result = dict(active_tickets_by_category)
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5003)