# Django Receipt Tracker

## Description
Django Receipt Tracker is a web application for managing and tracking receipts. Users can create, view, update, and delete their receipts.

## Installation
1. Clone the repository: `git clone https://github.com/YacineHam/ExpenseTracker`
2. Navigate to the project directory: `cd Django-Receipt-Tracker`
3. Install required packages: `pip install -r requirements.txt`

## Setting Up
- Set up the database: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`

## Running the Application
Run the server using: `python manage.py runserver`
Access the app at `http://localhost:8000`.

## Using Docker (Optional)
- Build the Docker image: `docker build -t receipt-tracker .`
- Run the Docker container: `docker run -p 8000:8000 receipt-tracker`

## Testing
Run tests: `python manage.py test`

## Contributing
Contributions to the project are welcome!