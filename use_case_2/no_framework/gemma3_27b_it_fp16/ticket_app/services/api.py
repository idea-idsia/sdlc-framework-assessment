from flask import Flask, jsonify
from analytics import AnalyticsService

app = Flask(__name__)
analytics_service = AnalyticsService()

@app.route('/analytics/tickets_opened/<period>/<period_unit>')
def get_tickets_opened(period, period_unit):
    return jsonify({'count': analytics_service.tickets_opened_in_period(int(period), period_unit)})

@app.route('/analytics/resolution_time')
def get_resolution_time():
    return jsonify(analytics_service.average_resolution_time())

@app.route('/analytics/category_counts')
def get_category_counts():
    return jsonify(analytics_service.cluster_tickets_by_category())

if __name__ == '__main__':
    app.run(debug=True)