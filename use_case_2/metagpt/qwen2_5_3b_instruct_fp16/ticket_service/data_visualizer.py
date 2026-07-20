from datetime import datetime
import json

class DataVisualization:
    def __init__(self):
        self.tickets_data = {}
        self.users_data = {}
        self.metrics = {}

    @staticmethod
    def fetch_tickets():
        # Placeholder for fetching tickets from the database or API.
        # For demonstration purposes, we will simulate fetching 3 tickets.
        tickets = [
            {"id": 1, "title": "Bug in login page", "description": "Cannot log in with correct credentials.", "status": "open"},
            {"id": 2, "title": "Issue with dashboard loading", "description": "Dashboard takes too long to load.", "status": "active"},
            {"id": 3, "title": "Problem with notifications", "description": "Notifications are not working as expected.", "status": "closed"}
        ]
        
        # Convert tickets into a dictionary for easier access
        self.tickets_data = {ticket["id"]: ticket for ticket in tickets}
        return self.tickets_data

    @staticmethod
    def fetch_users():
        # Placeholder for fetching users from the database or API.
        # For demonstration purposes, we will simulate fetching 2 users.
        users = [
            {"id": 1, "username": "admin", "email": "admin@example.com"},
            {"id": 2, "username": "user1", "email": "user1@example.com"}
        ]
        
        # Convert users into a dictionary for easier access
        self.users_data = {user["id"]: user for user in users}
        return self.users_data

    @staticmethod
    def generate_report():
        report = {
            'tickets': DataVisualization.fetch_tickets(),
            'users': DataVisualization.fetch_users()
        }
        
        # Placeholder for actual data visualization logic.
        # For demonstration purposes, we will just print the generated report.
        with open('data_visualization_report.json', 'w') as file:
            json.dump(report, file, indent=4)
            
        return "Generated Report"

    @staticmethod
    def fetch_tickets():
        if not DataVisualization.tickets_data:
            DataVisualization.fetch_tickets()
        
        return DataVisualization.tickets_data

    @staticmethod
    def fetch_users():
        if not DataVisualization.users_data:
            DataVisualization.fetch_users()
        
        return DataVisualization.users_data

    @staticmethod
    def generate_report():
        report = {
            'tickets': DataVisualization.fetch_tickets(),
            'users': DataVisualization.fetch_users()
        }
        
        # Placeholder for actual data visualization logic.
        # For demonstration purposes, we will just print the generated report.
        with open('data_visualization_report.json', 'w') as file:
            json.dump(report, file, indent=4)
            
        return "Generated Report"

# Example usage of DataVisualization class methods
if __name__ == "__main__":
    data_visualizer = DataVisualization()
    
    # Fetch tickets and users for the report
    tickets_data = data_visualizer.fetch_tickets()
    users_data = data_visualizer.fetch_users()
    
    # Generate a report and display it
    report = data_visualizer.generate_report()
    print(report)
