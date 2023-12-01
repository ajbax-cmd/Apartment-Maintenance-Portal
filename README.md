# XYZ Apartments Maintenance Portal

## Overview
The XYZ Apartments Maintenance Portal is a Django-based web application designed to streamline the process of handling maintenance requests within an apartment complex. It allows tenants to submit maintenance requests, enables the maintenance team to view and filter these requests, and provides management capabilities for tenant information.

## Features
- **Tenant Submission**: Tenants can submit maintenance requests, including details like the affected area, a description of the issue, and optional images.
- **Maintenance Team Access**: A dedicated interface for the maintenance team to view, filter, and update the status of maintenance requests.
- **Management Interface**: Allows apartment management to add, edit, or delete tenant information, and search through tenant records.
- **Responsive Design**: The application is styled with responsive design principles, ensuring a seamless experience across various devices.

## Technologies
- **Django**: The application is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite**: Uses SQLite as the database backend.
- **HTML/CSS**: Front-end built using HTML and CSS, with Django template system.

## Installation and Setup
### Clone the Repository
   ```bash
   git clone https://github.com/your-username/xyz-apartments.git
   cd xyz-apartments
  ```
### Install Dependencies
  ```bash
    pip install -r requirements.txt
  ```
### Initialzie Database
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
### Run the Server
  ```bash
    python manage.py runserver
  ```
Access the application at http://127.0.0.1:8000/.

## Usage

* Navigate to the home page and choose the appropriate section (Tenants, Maintenance Team, Management).
* Tenants can submit requests via the Tenant section.
* Maintenance Team can view and update request statuses.
* Management can manage tenant records.
