from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

FASTAPI_BASE_URL = "http://localhost:8000"


# Route to display the list of clients
@app.route('/')
def index():
    try:
        response = requests.get(f"{FASTAPI_BASE_URL}/clients")
        response.raise_for_status()
        clients = response.json()
    except requests.exceptions.RequestException as e:
        clients = []
        print(f"Error fetching clients: {e}")
    return render_template('index.html', clients=clients)


# Route to display cost details of a client for a particular month
from datetime import datetime
import requests


@app.route('/client/<client_id>/cost', methods=['GET', 'POST'])
def client_cost(client_id):
    # Get the current month if no POST request is made
    current_month = datetime.now().month
    month = request.form.get('month', current_month)  # Default to the current month

    cost_details = None
    try:
        response = requests.get(f"{FASTAPI_BASE_URL}/clients/{client_id}/cost", params={'month': month})
        response.raise_for_status()
        cost_details = response.json()  # Parse the response as JSON
    except requests.exceptions.RequestException as e:
        return render_template('error.html', message=f"Error fetching client cost details: {e}")

    if not cost_details:
        return render_template('error.html', message="No cost details found for this client and month.")

    return render_template('client_cost.html', cost_details=cost_details, month=int(month))


# Route to display cost details of a specific user within a client
@app.route('/client/<client_id>/user/<user_email>/cost', methods=['GET', 'POST'])
def user_cost(client_id, user_email):
    month = request.form.get('month') if request.method == 'POST' else 10  # Default to October if no month selected
    try:
        response = requests.get(f"{FASTAPI_BASE_URL}/clients/{client_id}/user/{user_email}/cost", params={'month': month})
        response.raise_for_status()
        user_cost_details = response.json()
    except requests.exceptions.RequestException as e:
        user_cost_details = None
        print(f"Error fetching user cost details: {e}")
    return render_template('user_cost.html', user_cost_details=user_cost_details, month=month)


if __name__ == '__main__':
    app.run(debug=True)