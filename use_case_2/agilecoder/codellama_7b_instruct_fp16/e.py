'''
File: e.py
Author: $USERNAME
Description: $DESCRIPTION
'''
import requests
class Microservices:
    def __init__(self):
        pass
    def get_num_open_tickets(self, period):
        response = requests.get("http://localhost:5000/api/v1/tickets?period={}".format(period))
        num_open_tickets = response.json()["num_open_tickets"]
        return num_open_tickets
    def get_avg_ticket_resolution_time(self, month):
        response = requests.get("http://localhost:5000/api/v1/tickets?month={}".format(month))
        avg_ticket_resolution_time = response.json()["avg_ticket_resolution_time"]
        return avg_ticket_resolution_time
    def get_num_active_tickets_by_category(self, category):
        response = requests.get("http://localhost:5000/api/v1/tickets?category={}".format(category))
        num_active_tickets = response.json()["num_active_tickets"]
        return num_active_tickets