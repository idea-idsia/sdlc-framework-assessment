# Ticket Management System Manual
## Introduction
The Ticket Management System is a web-based application designed to manage and track issues reported by users at a university campus. The system allows users to report problems, modify existing tickets, and exchange messages with helpdesk staff.

## Main Functions
The system has the following main functions:

*   **Login Page**: A GUI that enables users to enter the application as either a helpdesk staff member or a simple user.
*   **Ticket Management System**: A GUI that allows users to create new tickets, view and modify existing tickets, and exchange messages related to specific tickets.
*   **Database**: The system uses a database to store all ticket-related data, including ticket attributes (status, description, category, opening date, last modification date, and closing date).
*   **Microservices Architecture**: The system implements a microservices architecture that interacts with the ticket management application to provide helpdesk users with data visualization and analysis functionalities.

## Installation
To install the required environment dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage
1.  **Running the Application**:
    *   To start the application, execute `python main.py`.
2.  **Creating a New Ticket**:
    *   Fill in the description and category fields.
    *   Click the "Create Ticket" button to create a new ticket.
3.  **Viewing and Modifying Existing Tickets**:
    *   Helpdesk staff can view all open, active, and closed tickets.
    *   Simple users can view and modify only open and active tickets.
4.  **Exchanging Messages**:
    *   Users and helpdesk staff can exchange messages related to specific tickets.

## Microservices
The system implements the following microservices:

*   **Service 1**: Allows users to choose a period (last X hours/days) and displays the number of tickets opened in that period that have not yet been closed.
*   **Service 2**: Calculates and displays the average ticket resolution time, grouped by opening month.
*   **Service 3**: Clusters tickets by category and displays the number of active tickets per category.

## API Interaction
The microservices interact with the database through APIs. The system provides a RESTful API for creating, reading, updating, and deleting (CRUD) ticket data.

## Troubleshooting
If you encounter any issues while using the application, refer to the `manual.md` file for troubleshooting guides or contact our support team for assistance.

By following this manual, users can effectively utilize the Ticket Management System to report and manage issues at the university campus.