# Ticket Management Web Application User Manual

## Introduction

The Ticket Management Web Application is a Python-based software designed for managing facility management problems, technical IT issues, and service complaints on a university campus. The application allows users to report and modify problems, while helpdesk staff can visualize and analyze data related to tickets.

This manual provides detailed instructions on installing the necessary environment dependencies and using the application.

## Table of Contents
1. [Main Functions](#main-functions)
2. [Environment Dependencies Installation](#environment-dependencies-installation)
3. [Using the Application](#using-the-application)

---

### Main Functions

The Ticket Management Web Application offers several key functionalities:

- **Ticket Reporting and Modification:**
  - Users can report new issues and modify open or active tickets.
  
- **Helpdesk Staff Interface:**
  - Helpdesk staff has access to all tickets (open, active, closed) and can change their status.

- **Microservices for Data Visualization and Analysis:**
  - Provides services for analyzing ticket data based on specific criteria like periods of time, resolution times, and category clusters.

### Environment Dependencies Installation

To run the Ticket Management Web Application, you need to have Python installed in your environment. The application uses `tkinter` and `sqlite3`, which are included by default with standard Python installations from version 3.6 onwards. Therefore, no additional package installation is required.

#### Step-by-Step Guide:
1. Ensure Python is installed on your system (version 3.6 or later recommended).
2. Download the project files.
3. Navigate to the folder containing the application's source code in your terminal.
4. Run `python main.py` to start the application.

### Using the Application

#### Starting the Application
- Open a terminal or command prompt and navigate to the directory where you have saved the application files.
- Execute the following command:
  ```bash
  python main.py
  ```

#### Logging In
Upon starting the application, you will see a login page with options for logging in as either a user or helpdesk staff.

- **User:** Click "Login as User" to proceed. This interface allows users to report new issues and modify their open or active tickets.
  
- **Helpdesk Staff:** Click "Login as Admin." This interface provides access to all tickets and the ability to change ticket statuses, among other administrative functions.

#### Managing Tickets
- **For Users:**
  - Report a New Ticket: From the user interface, you can click on the "Add Ticket" button. Fill in the description and category of the issue.
  - Modify an Existing Ticket: Select the open or active ticket from the list to modify its details.

- **For Helpdesk Staff:**
  - Manage Tickets: View all tickets and change their statuses as necessary (e.g., marking a ticket as 'active' or 'closed').
  - Analyze Data: Access microservices through specific interfaces for data analysis, such as average resolution times or unresolved tickets over certain periods.

#### Microservice Analysis
The application provides several services to helpdesk staff analyze the data:
- **Service 1:** Select and view the number of open but unresolved tickets within a given time period.
- **Service 2:** Calculate the average resolution time for tickets opened during specific months.
- **Service 3:** Cluster active tickets by category to understand distribution across different issue types.

By following these instructions, you should be able to effectively use the Ticket Management Web Application for both reporting issues and managing helpdesk tasks. If you encounter any issues or require further assistance, please refer to additional documentation provided with the application or contact technical support.