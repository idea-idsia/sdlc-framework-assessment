manual.md
# Ticket Management System

A web application for managing tickets and interacting with helpdesk staff.

## Introduction

The Ticket Management System is a web application designed to allow users to report issues at a university campus, including facility management problems, technical IT issues, and services complaints. The application enables users to report and modify problems, and interacts with helpdesk staff who are responsible for resolving the issues.

## Main Functions

*   **Login Page**: A GUI that allows users to enter the application either as an helpdesk staff or a simple user.
*   **Ticket Management System**: A GUI that enables ticket management, including:
    *   Creating new tickets
    *   Viewing and modifying open and active tickets
    *   Exchanging messages related to each ticket
*   **Database**: A database that stores all the data, enabling helpdesk staff to visualize the data and select analysis to perform.
*   **Micro-services Architecture**: A microservices architecture that interacts with the ticket management application to provide helpdesk users with data visualization and analysis functionalities.

## Installation

To install the environment dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This will install the required packages, including Flask and sqlite3.

## Usage

1.  **Running the Application**: To run the application, execute the following command:

    ```bash
python main.py
```
2.  **Accessing the Application**: Open a web browser and navigate to `http://localhost:5000` to access the application.
3.  **Login**: Enter the application as either an helpdesk staff or a simple user.
4.  **Creating Tickets**: Create new tickets by filling out the ticket form and submitting it.
5.  **Viewing and Modifying Tickets**: View and modify open and active tickets, and exchange messages related to each ticket.

## Micro-services

The application includes three micro-services:

*   **Service 1**: Displays the number of tickets opened in a selected period that have not yet been closed.
*   **Service 2**: Calculates the average ticket resolution time, displayed by the opening month of the ticket.
*   **Service 3**: Clusters tickets by category and displays the number of active tickets per category.

These micro-services can be accessed through the following API endpoints:

*   `/service1`: Service 1
*   `/service2`: Service 2
*   `/service3`: Service 3

## Database

The application uses a SQLite database to store all the data. The database includes two tables: `tickets` and `users`.

*   **Tickets Table**: Stores information about each ticket, including status, description, category, opening date, last modification date, and closing date.
*   **Users Table**: Stores information about each user, including username and role.

## Troubleshooting

If you encounter any issues while using the application, refer to the [troubleshooting guide](troubleshooting.md) for assistance.