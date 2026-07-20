'''
Module providing microservices for data analysis.
Includes functions that interact with the database to provide specific analyses as required.
'''
import sqlite3
def get_unresolved_tickets(start_date: str):
    """Get number of unresolved tickets since a certain start date."""
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM tickets WHERE status != 'closed' AND opening_date >= ?"
    result = cursor.execute(query, (start_date,))
    return result.fetchone()[0]
def average_resolution_time(month: str):
    """Calculate the average resolution time for tickets opened in a specific month."""
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    query = "SELECT AVG(julianday(closing_date) - julianday(opening_date)) FROM tickets WHERE strftime('%m', opening_date) = ?"
    result = cursor.execute(query, (month,))
    return result.fetchone()[0]
def ticket_category_count():
    """Cluster the tickets by category and display active tickets per category."""
    connection = sqlite3.connect("tickets.db")
    cursor = connection.cursor()
    query = "SELECT category, COUNT(*) FROM tickets WHERE status != 'closed' GROUP BY category"
    results = cursor.execute(query)
    return {row[0]: row[1] for row in results}