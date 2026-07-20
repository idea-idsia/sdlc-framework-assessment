'''
API Manager to handle interactions between microservices and the main application.
'''
from tkinter import Tk, StringVar
import service1, service2, service3
from flask import Flask, jsonify, request
from login_page import LoginPage
from database_manager import DatabaseManager
from user_dashboard import UserDashboard
from helpdesk_dashboard import HelpdeskDashboard
app = Flask(__name__)
db_manager = DatabaseManager()
def open_dashboard(user_type):
    root = Tk()
    if user_type == "simple_user":
        dashboard = UserDashboard(root, db_manager)
    elif user_type == "helpdesk":
        dashboard = HelpdeskDashboard(root, db_manager)
    root.mainloop()
@app.route('/open_tickets/<int:days>')
def open_tickets(days):
    service = Service1()
    return jsonify(service.get_open_tickets(days))
@app.route('/avg_resolution_time')
def avg_resolution_time():
    service = Service2()
    return jsonify(service.get_avg_resolution_time())
@app.route('/active_tickets_by_category')
def active_tickets_by_category():
    service = Service3()
    return jsonify(service.get_active_tickets_by_category())
if __name__ == "__main__":
    root = Tk()
    login_page = LoginPage(root, open_dashboard)
    app.run(debug=True)