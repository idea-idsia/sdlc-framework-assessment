# Create ticket_count_service.py
service_code = '''
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import datetime

app = Flask(__name__)

DATABASE_URI = 'sqlite:///../database/tickets.db'
engine = create_engine(DATABASE_URI)

@app.route('/count_by_status', methods=['GET'])
def count_by_status():
    status = request.args.get('status')
    if not status:
        return jsonify({"error": "Status parameter is required"}), 400

    query = f"SELECT COUNT(*) FROM ticket WHERE status='{status}'"
    result = engine.execute(query).fetchone()
    count = result[0]

    return jsonify({f"count_{status}": count})

if __name__ == '__main__':
    app.run(port=5001)
'''

with open("ticket_management/ticket_count_service.py", "w") as f:
    f.write(service_code)

# Run the service
import sys
subprocess.run([sys.executable, "ticket_count_service.py"], cwd="ticket_management")