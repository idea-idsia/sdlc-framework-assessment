'''
File: guide.py
Author: $USERNAME
Description: This file contains the class that implements the guide functionality for the ticket management system.
'''
class Guide():
    '''
    Class for implementing the guide functionality in the ticket management system.
    Attributes:
        tms: The TicketManagementSystem object that provides access to the database and other functionalities.
    '''
    def __init__(self, tms):
        '''
        Constructor for the Guide class.
        Args:
            tms: The TicketManagementSystem object that provides access to the database and other functionalities.
        '''
        self.tms = tms
    def display_guide(self):
        '''
        Displays a guide on how to use the ticket management system.
        '''
        print("Welcome to the ticket management system!")
        print("Here is a step-by-step guide on how to use this software:")
        print("1. Open the application and select either 'Helpdesk' or 'User'.")
        print("2. Log in using your credentials.")
        print("3. If you are a helpdesk user, you can view all open and active tickets by clicking on the 'Tickets' button.")
        print("4. To create a new ticket, click on the 'New Ticket' button.")
        print("5. Enter the necessary details for the ticket and select the appropriate category.")
        print("6. Once you have created the ticket, you can view it by clicking on its ID number in the list of tickets.")
        print("7. You can change the status of a ticket from 'open' to 'active' or from 'active' to 'closed'.")
        print("8. To interact with other users, click on the 'Messages' button.")
        print("9. If you are a user, you can view all open and active tickets by clicking on the 'Tickets' button.")
        print("10. To create a new ticket, click on the 'New Ticket' button.")
        print("11. Enter the necessary details for the ticket and select the appropriate category.")
        print("12. Once you have created the ticket, you can view it by clicking on its ID number in the list of tickets.")
        print("That's it! You now know how to use this software.")