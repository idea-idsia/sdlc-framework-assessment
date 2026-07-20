# Ticket Management Web Application User Manual

Welcome to the Ticket Management Web Application! This application allows users to report and manage issues on a university campus. It is designed for both simple users reporting issues and helpdesk staff who are responsible for resolving these tickets.

## Quick Install

To get started with this application, you will need to install several dependencies:

1. Ensure that Python is installed on your system.
2. Clone the repository or download the source code files.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the following commands to create a virtual environment and install required packages:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
pip install -r requirements.txt
```

## 🤔 What is This?

The Ticket Management Web Application allows users to:
- Report issues related to facility management, technical IT problems, and service complaints.
- View, modify, and track the status of tickets.

For helpdesk staff, additional functionalities include:
- Updating ticket status from 'open' to 'active', and 'active' to 'closed'.
- Managing all open, active, and closed tickets.
- Exchanging messages related to specific tickets with users.

## 📖 Documentation

### Main Functions of the Software:

#### Login Page
The login page allows you to select your user type:
- **User**: For reporting issues as a simple campus user.
- **Helpdesk**: For managing and resolving issues as helpdesk staff.

#### User Dashboard
For simple users, this dashboard enables:
- Creating new tickets with descriptions and categories.
- Viewing and modifying all open and active tickets assigned to them.

#### Helpdesk Dashboard
For helpdesk staff, this dashboard provides:
- The ability to view all open, active, and closed tickets.
- Updating ticket statuses and exchanging messages related to each ticket.
- Access to data visualization and analysis functionalities via microservices.

### API Microservices:

The application includes three microservices that interact with the main application through APIs:

1. **Service 1**:
   - Allows you to choose a period (last X hours/days).
   - Displays the number of tickets opened in the selected period, which have not yet been closed.

2. **Service 2**:
   - Calculates and displays the average ticket resolution time by opening month.
   - Only includes resolved tickets.

3. **Service 3**:
   - Clusters the tickets by category.
   - Displays the number of active tickets per category.

### How to Use/Play It:

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **Access the Application**:
   Open your web browser and go to `http://localhost:5000` to access the application.

3. **Login**:
   - Select "User" or "Helpdesk" based on your role.
   - Note that no actual login is implemented; this step is just a selection of roles.

4. **User Dashboard**:
    - Fill in ticket details and submit new tickets.
    - View your open and active tickets, and update them as needed.

5. **Helpdesk Dashboard**:
    - View all open, active, and closed tickets.
    - Update the status of tickets to manage them effectively.
    - Use microservices to get detailed analytics on ticket data through API endpoints.

### How to Contribute

If you would like to contribute to this project:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## 📞 Support

For any support or queries, please contact us at [support@ticketmanagementapp.com].

---

We hope you find this application useful for managing tickets effectively! Happy ticketing!

```