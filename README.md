# Multi-User TODO App 📝

## Introduction
The Multi-User TODO App is a Django-based web application designed for users to efficiently manage their daily tasks. It includes an authentication system where users can create accounts, log in, and perform CRUD (Create, Read, Update, Delete) operations on tasks. Administrators or superusers have extended privileges to manage all user activities through the Django admin panel. The app features CSS styling, Google Fonts, and Font Awesome icons for a clean and interactive interface.

# Features
## User-Specific Functionality:
### Authentication System: Create an account, login, and logout securely.

### Task Management:

- Add daily tasks with relevant details.

- Edit existing tasks when priorities change.

- Delete tasks that are no longer needed.

## Admin-Specific Functionality:
### Admin Panel:

- Full control over all users and their tasks.

- Ability to edit or delete any user’s tasks.

- User management, including account creation or suspension.

### Interactive Design:
- Custom Styling: CSS enhances visual appeal.

- Google Fonts Integration: Sleek typography for better readability.

- Font Awesome Icons: Adds interactive and aesthetic elements to buttons and task lists.

# Technologies Used
## Backend:
- Django (Python)

## Frontend:
- HTML

- CSS (with Google Fonts and Font Awesome Icons)

- JavaScript (for dynamic interactivity)

## Database:
- SQLite (default, but can be switched to PostgreSQL or MySQL)

# Usage
## User Workflow:

### Account Creation:

- Click on "Sign Up" to create a new account.

- Login with your credentials.

### Task Management:

- Add tasks via the form interface.

- View tasks in the list along with options to edit or delete.

### Logout:

- Securely logout when finished.

## Admin Workflow:
- Login to the admin panel.

- Manage users and their tasks:

+ View all tasks in the database.

+ Edit or delete any user’s tasks.

- Perform advanced administrative actions.

# Customization
## Fonts:
- Modify Google Fonts from the CSS file for custom typography.

## Icons:
- Adjust or add Font Awesome icons based on your design preferences.

## Database:
- Replace SQLite with a production-ready database like PostgreSQL for scalability:

+ Update DATABASES in settings.py.

# Acknowledgements
- Google Fonts for typography.

- Font Awesome for interactive icons.

- Django documentation for development resources.
