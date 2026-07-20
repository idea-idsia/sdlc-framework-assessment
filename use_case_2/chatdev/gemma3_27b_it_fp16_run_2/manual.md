```markdown
# University Ticket Management System - User Manual

## Introduction

Welcome to the University Ticket Management System! This application allows students, faculty, and staff to report issues on campus, and enables helpdesk staff to manage and resolve these issues efficiently.  This manual will guide you through the installation, setup, and usage of the system.

## System Overview

This application is built with Python, utilizing a graphical user interface (GUI) and a SQLite database to store information.  It’s structured using a microservices architecture, allowing for data visualization and analysis capabilities for helpdesk staff. The application offers different functionalities based on user roles: simple users and helpdesk staff.

## 1. Environment Setup

Before running the application, you need to ensure you have the necessary Python packages installed.

### 1.1 Prerequisites

*   **Python 3.7+:**  Make sure you have Python 3.7 or a later version installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
*   **pip:** Python package installer. Typically included with Python installations.

### 1.2 Installing Dependencies

Open your terminal or command prompt and navigate to the directory containing the application files. Then, run the following command to install the required packages:

```bash
pip install tkinter flask
```

This command installs:

*   **tkinter:** For creating the GUI.
*   **flask:** For building the microservices API.

## 2. Application Structure

The application consists of several Python files:

*   **main.py:** Contains the Flask API endpoints for data visualization and analysis.  This implements the microservices portion.
*   **gui.py:**  Contains the GUI code built with tkinter, providing the user interface for interacting with the system.
*   **database_manager.py:** Handles the interaction with the SQLite database.  Provides functions for inserting, updating, and retrieving ticket and message data.
*   **ticket_manager.py:** Provides a layer of abstraction for ticket operations like creating, updating and adding messages.

## 3. Running the Application

### 3.1 Starting the API (Microservices)

1.  Open your terminal or command prompt.
2.  Navigate to the directory where `main.py` is located.
3.  Run the following command:

    ```bash
    python main.py
    ```

    This will start the Flask API server.  By default, it runs on `http://127.0.0.1:5000/`.  Keep this terminal window open as the API needs to be running in the background.

### 3.2 Starting the GUI

1.  Open a *new* terminal or command prompt.
2.  Navigate to the directory where `gui.py` is located.
3.  Run the following command:

    ```bash
    python gui.py
    ```

    This will launch the application's GUI.

## 4. Using the Application – User Guide

### 4.1 Login (User Type Selection)

The application doesn't have a traditional login system. Instead, you select your user type:

*   **Simple User:**  For students, faculty, and staff reporting issues.
*   **Helpdesk:** For helpdesk personnel managing and resolving issues.

Click the "Toggle Helpdesk Mode" button to switch between these roles. The available functionalities will change depending on your selected role.

### 4.2 Simple User Functionality

*   **New Ticket:**
    1.  Click the "New Ticket" tab.
    2.  Enter a detailed description of the issue in the "Description" field.
    3.  Select the appropriate category from the "Category" dropdown menu (Facility Management, Technical IT, Services Complaints).
    4.  Click "Submit". A confirmation message will appear.  The ticket will be created with a status of "open".
*   **Ticket List:**
    1.  Click the "Tickets" tab.
    2.  You will see a list of tickets with the status of "open" or "active".
    3.  Select a ticket from the list to view details.
    4.  You can *modify* tickets that you have created. To do this, select a ticket from the list and view details.
* **Viewing Ticket Details & Adding Messages:**
    1. Select a ticket.
    2. Click "View Details". A new window will appear showing the ticket details and any existing messages.
    3. Enter a message in the message entry field and click "Send Message".

### 4.3 Helpdesk User Functionality

Helpdesk users have all the functionalities of a simple user, plus the following:

*   **View All Tickets:** You can see tickets with the status "open," "active," and "closed."
*   **Modify Ticket Status:**
    1.  Select a ticket from the "Tickets" tab.
    2.  Click the "Modify Status" button.
    3.  The status will automatically change based on the current status:
        *   "Open" -> "Active"
        *   "Active" -> "Closed"
    4.  A confirmation message will appear.
*   **Viewing Ticket Details & Adding Messages:** Same as for simple users.

## 5. Microservices – Data Visualization and Analysis

The `main.py` file provides the following API endpoints for data visualization and analysis:

*   **/api/tickets/period?period=[hours]**: Returns the number of open (not closed) tickets within the specified number of hours.  Example: `http://127.0.0.1:5000/api/tickets/period?period=24` (returns tickets opened in the last 24 hours).
*   **/api/tickets/resolution_time**: Returns the average ticket resolution time (in hours) grouped by the opening month of the ticket.
*   **/api/tickets/category**: Returns the number of active tickets per category.

These endpoints can be used by external applications or dashboards to visualize ticket data.

## 6. Troubleshooting

*   **Error connecting to the database:** Ensure that the `tickets.db` file exists in the same directory as the application files. If it doesn’t, the application will create it.  Permissions issues can sometimes prevent database creation.
*   **GUI not launching:** Verify that you have tkinter installed correctly.
*   **API not responding:** Check that `main.py` is running in a terminal window.
* **Database errors:** Check the terminal output for any error messages from SQLite.

## 7.  Future Enhancements

*   User authentication and authorization system.
*   More advanced data visualization and reporting features.
*   Integration with email or other notification systems.
*   Improved search functionality.
```