# Frontend (Flask)
The frontend provides a simple interface for interacting with the FastAPI backend. It displays list of clients and allows you to drill down into the cost details for each client by task and user.

## Features
1. Displays a list of clients with pagination.
2. Displays cost details categorized by task and user.
3. Handles errors and exceptions (e.g., server down or no data available).
## Requirements
1. Python 3.8+
2. Flask for the web server
3.Requests to interact with FastAPI

## Setup Instructions
### Clone the repository:

If you haven’t already, clone the repository and navigate to the frontend folder:
```
git clone https://github.com/your-repo/flask-frontend.git
```
## Frontend Structure
- templates/: Contains HTML templates for rendering client lists and cost details.
- static/: Holds any static files like CSS, images, etc.
### Routes:
- /: Displays a paginated list of clients.
- /clients/<client_id>/cost: Displays the cost details of the selected client, categorized by task and user.
