Here is a detailed user manual to use the software:
manual.md
```
# Ticket Management System
## Introduction
The Ticket Management System is a web application designed for users to report issues at a university campus. The system allows users to create, modify, and view tickets, as well as interact with helpdesk staff who are responsible for resolving the issues.

## Installation
To use the Ticket Management System, you need to install the required dependencies. You can do this by running the following command:
```
pip install -r requirements.txt
```
This will install all the necessary packages, including `sqlite3`, `tkinter`, and `datetime`.

## Running the Application
Once you have installed the dependencies, you can run the application by executing the `main.py` file:
```
python main.py
```
This will launch the login page of the application.

## Login Page
The login page allows users to enter the application either as a helpdesk staff or a simple user. To log in, simply enter your username and password, and select your role from the dropdown menu.

## Ticket Management
Once you have logged in, you can access the ticket management system. The system allows you to:

* Create new tickets: Simple users can create new tickets by filling out the description and category fields.
* View tickets: Both helpdesk staff and simple users can view all open and active tickets.
* Modify tickets: Helpdesk staff can modify ticket status from 'open' to 'active' and from 'active' to 'closed'.
* Exchange messages: Both helpdesk staff and simple users can exchange messages related to a specific ticket.

## Services
The application also provides three services:

* Service 1: Display the number of tickets opened in a selected period that have not yet been closed.
* Service 2: Display the average resolution time of all tickets.
* Service 3: Display the number of active tickets by category.

## Using the Services
To use the services, you need to access the corresponding pages:

* Service 1: Go to the "Open Tickets" page and select the period from the dropdown menu.
* Service 2: Go to the "Resolution Time" page.
* Service 3: Go to the "Active Tickets by Category" page.

## Database
The application uses a SQLite database to store all data. The database is created automatically when you run the application for the first time.

## Troubleshooting
If you encounter any issues while using the application, you can check the following:

* Make sure you have installed all the required dependencies.
* Check that the database is properly configured.
* If you are experiencing issues with the login page, try resetting your password or contacting the administrator.

By following these steps, you should be able to use the Ticket Management System effectively. If you have any further questions or need additional assistance, don't hesitate to contact us.
```