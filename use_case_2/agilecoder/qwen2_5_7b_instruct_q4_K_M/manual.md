Sure, let's create a `manual.md` file for your ticket management system. This manual will cover how to install the dependencies, run the application, and use its features effectively.

### manual.md

```markdown
# Ticket Management System User Manual

## Introduction

This document provides detailed instructions on installing and using our ticket management system. The system allows users to report issues related to facility management, technical IT, or services complaints. Helpdesk staff can view, update, and analyze the tickets to resolve issues efficiently.

## Installation

### Prerequisites

- Python 3.x
- SQLite database (comes bundled with Python)

### Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-repo/ticket-management-system.git
   cd ticket-management-system
   ```

2. **Install Dependencies:**
   The project does not require any external libraries, so no additional dependencies need to be installed.

3. **Run the Application:**
   ```sh
   python main.py
   ```

### Running the Application

1. **Login Page:**
   - Upon running `main.py`, you will see a simple CLI interface.
   - You can log in as either an "helpdesk staff" or a "simple user" using predefined credentials.

2. **Ticket Management System:**
   - **Simple User:**
     - From the main menu, select option 1 to add a new ticket.
     - Enter the category and description for the ticket.
     - You can view and modify all open and active tickets by selecting option 2 from the main menu.

   - **Helpdesk Staff:**
     - From the main menu, select option 2 to update the status of an existing ticket.
     - You can also view all open, active, and closed tickets. Additionally, you can change the status of a ticket from 'open' to 'active' or from 'active' to 'closed'.

3. **Database Interaction:**
   - The application interacts with a local SQLite database named `tickets.db` to store and manage tickets.

4. **Microservices Architecture (Not Fully Implemented):**
   - Service 1: View the number of open tickets in a given period.
   - Service 2: Calculate the average resolution time for tickets by month.
   - Service 3: Cluster active tickets by category.

### Example Usage

#### Adding a New Ticket as a Simple User
```sh
1. Add new ticket
2. Update ticket status
3. Exit
Enter your choice: 1
Enter ticket category: facility management
Enter ticket description: Elevator is not working in Building A
Ticket added successfully.
```

#### Updating Ticket Status as Helpdesk Staff
```sh
1. Add new ticket
2. Update ticket status
3. Exit
Enter your choice: 2
Enter the ID of the ticket to update: 1
Enter the new status (open, active, resolved): active
Ticket status updated successfully.
```

#### Viewing Open Tickets as Helpdesk Staff
```sh
1. Add new ticket
2. Update ticket status
3. Exit
Enter your choice: 2
ID: 1 | Category: facility management | Description: Elevator is not working in Building A | Status: active
```

### Troubleshooting

- If you encounter any issues, ensure that Python 3.x is installed and the script runs without errors.
- Check the logs for any database connection or query errors.

## Contributing

If you find any bugs or have suggestions for improvements, please create an issue on our GitHub repository: [https://github.com/your-repo/ticket-management-system](https://github.com/your-repo/ticket-management-system)

---

For more detailed information and advanced usage, refer to the `README.md` file in the root directory.

```

This manual provides a clear guide for users on how to set up and use the ticket management system effectively. Make sure to update the placeholders with relevant details specific to your project before sharing it with others.