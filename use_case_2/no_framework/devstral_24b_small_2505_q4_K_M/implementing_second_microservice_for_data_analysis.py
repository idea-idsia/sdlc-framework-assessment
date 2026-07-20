# Create ticket_analysis_service.py
service_code = '''
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import datetime

app = Flask(__name__)

DATABASE_URI = 'sqlite:///../database/tickets.db'
engine = create_engine(DATABASE_URI)

@app.route('/average_response_time', methods=['GET'])
def average_response_time():
    category = request.args.get('category')
    if not category:
        return jsonify({"error": "Category parameter is required"}), 400

    query = f"""
    SELECT AVG(JULIANDAY(closing_date) - JULIANDAY(opening_date))
    FROM ticket
    WHERE status='closed' AND category='{category}'
    """
    result = engine.execute(query).fetchone()
    avg_time = result[0]

    return jsonify({f"average_response_time_{category}": avg_time})

if __name__ == '__main__':
    app.run(port=5002)
'''

with open("ticket_management/ticket_analysis_service.py", "w") as f:
    f.write(service_code)

# Run the service
import sys
subprocess.run([sys.executable, "ticket_analysis_service.py"], cwd="ticket_management")