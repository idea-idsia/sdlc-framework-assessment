'''
File: ticket.py
Author: $USERNAME
Description: This file contains the class that represents a ticket in the ticket management system.
'''
class Ticket():
    '''
    Class for representing a ticket in the ticket management system.
    Attributes:
        tms: The TicketManagementSystem object that provides access to the database and other functionalities.
        id: The unique identifier of the ticket.
        description: A brief description of the issue.
        category: The category of the issue (e.g.: facility management, technical IT, services complaints).
        status: The current status of the ticket (e.g.: open, active, closed).
    '''
    def __init__(self, tms, id):
        '''
        Constructor for the Ticket class.
        Args:
            tms: The TicketManagementSystem object that provides access to the database and other functionalities.
            id: The unique identifier of the ticket.
        '''
        self.tms = tms
        self.id = id
        self.description = None
        self.category = None
        self.status = 'open'
    def set_description(self, description):
        '''
        Sets a brief description of the issue.
        Args:
            description: The description to be set.
        '''
        self.description = description
    def set_category(self, category):
        '''
        Sets the category of the issue (e.g.: facility management, technical IT, services complaints).
        Args:
            category: The category to be set.
        '''
        self.category = category
    def set_status(self, status):
        '''
        Sets the current status of the ticket (e.g.: open, active, closed).
        Args:
            status: The status to be set.
        '''
        self.status = status
    def get_description(self):
        '''
        Returns a brief description of the issue.
        Returns:
            The description of the issue.
        '''
        return self.description
    def get_category(self):
        '''
        Returns the category of the issue (e.g.: facility management, technical IT, services complaints).
        Returns:
            The category of the issue.
        '''
        return self.category
    def get_status(self):
        '''
        Returns the current status of the ticket (e.g.: open, active, closed).
        Returns:
            The status of the ticket.
        '''
        return self.status