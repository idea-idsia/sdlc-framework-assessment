from ticket_management import TicketManagementSystem

# Create a new ticket management system instance
tms = TicketManagementSystem()

# Add a new ticket to the database
ticket = tms.add_new_ticket(
    status='open',
    description='Elevator is not working in building A',
    category='facility management'
)

# View the newly added ticket
print(ticket)