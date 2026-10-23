Online Notes App

A simple and responsive web application for taking and managing personal notes, built with Python and Flask.

Features

Create, edit, and delete notes.

Automatic creation dates and timestamps for each note.

Light and dark mode with setting retention in your browser.

Basic security features including CSRF protection and database parameterization.

Clean design focused on readability and ease of use.

Technologies Used

Backend: Python 3, Flask, Flask-SQLAlchemy, Flask-WTF

Database: SQLite

Frontend: HTML5, CSS3, JavaScript

How to Run the Project

Clone or download this repository to your local machine.

Install the required dependencies using pip:

pip install flask flask-sqlalchemy flask-wtf

Run the main application file:

python app.py

Open your web browser and go to http://127.0.0.1:5000 to access the app.

Project Structure

app.py: The primary application script containing database models and routes.

templates/: Contains the HTML pages (index.html and edit.html).

static/: Holds CSS styling and theme configuration.

database.db: The local SQLite database file generated on first startup.
