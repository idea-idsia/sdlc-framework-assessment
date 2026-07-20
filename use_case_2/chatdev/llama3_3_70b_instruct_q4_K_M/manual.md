# Ticket Management System
A web application for reporting and managing issues at a university campus.

## Introduction
The ticket management system is designed to allow users to report issues related to facility management, technical IT problems, and services complaints. The system enables helpdesk staff to visualize data, select analysis to perform, and interact with users who reported the issues.

## Main Functions
- **Login Page**: A GUI that allows users to enter the application as either a helpdesk staff or a simple user.
- **Ticket Management System**: A GUI that enables ticket management, including inserting new tickets, viewing and modifying existing tickets, exchanging messages related to each ticket, and changing ticket status.
- **Database**: A database to store all data, enabling basic functionalities such as inserting and modifying data.
- **Microservices Architecture**: A microservices architecture that interacts with the ticket management application to provide helpdesk users with data visualization and analysis functionalities.

## Installing Environment Dependencies
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```
The `requirements.txt` file includes the necessary packages for potential additional functionalities:
```
numpy==1.22.4
pandas>=1.4.2
matplotlib>=3.5.1
```

## Using the Ticket Management System
To use the ticket management system, follow these steps:

### 1. Running the Application
Run the `main.py` file to start the application:
```bash
python main.py
```
This will initialize the database and provide a menu-driven interface for users to interact with the system.

### 2. Inserting a New Ticket
To insert a new ticket, select option 1 from the menu and enter the required information:
- Description: A brief description of the issue.
- Status: The initial status of the ticket (default is 'open').
- Opening Date: The date when the ticket was opened.
- Last Modification Date: The date when the ticket was last modified.
- Closing Date: The date when the ticket was closed (optional).
- Category: The category of the issue (facility management, technical IT, or services complaints).

### 3. Viewing and Modifying Existing Tickets
To view and modify existing tickets, select option 2 from the menu. This will display a list of all tickets in the system.

### 4. Changing Ticket Status
To change the status of a ticket, select option 3 from the menu and enter the ticket ID and new status.

### 5. Getting Tickets by Period
To get tickets by period, select option 4 from the menu and enter the desired period (e.g., last X hours/days).

### 6. Calculating Average Ticket Resolution Time
To calculate the average ticket resolution time, select option 5 from the menu. This will display the average time it takes to resolve a ticket.

### 7. Clustering Tickets by Category
To cluster tickets by category, select option 6 from the menu. This will group tickets by their respective categories and display the number of active tickets in each category.

## Microservices Architecture
The microservices architecture provides helpdesk users with data visualization and analysis functionalities. The following services are available:

- **Service 1**: Get tickets by period.
- **Service 2**: Calculate average ticket resolution time.
- **Service 3**: Cluster tickets by category.

These services interact with the database via API to retrieve and analyze data.

## Troubleshooting
If you encounter any issues while using the ticket management system, refer to the following troubleshooting tips:

* Check that the `requirements.txt` file is up-to-date and that all dependencies are installed.
* Verify that the database connection is established correctly.
* Ensure that the user input is valid and consistent with the expected format.

By following these steps and guidelines, you should be able to successfully use the ticket management system and take advantage of its features.