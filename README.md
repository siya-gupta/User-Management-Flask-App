# User-Management-Flask-App
User Management Flask App
Overview:
In this assignment, you will be building a Flask application that manages user data. Users' information will be stored in a CSV file, and you'll create APIs to interact with this data.

Requirements:
Setting up the Flask App:
Initialize a new Flask project.
Create a virtual environment for the project.
Install Flask and any other necessary dependencies.
User Class:
Create a Python class User with the following attributes:
id (integer): Unique identifier for the user.
name (string): Name of the user.
email (string): Email address of the user.
location (string): Location of the user.
Data Storage:Store user information in a CSV file. Each row in the CSV file represents a user.
Endpoints:
Create the following endpoints:
GET /users: Retrieve a list of all users.
GET /users/{id}: Retrieve details of a user by ID.
GET /users?name={name}: Retrieve details of a user by name.
GET /users?email={email}: Retrieve details of a user by email.
GET /users?location={location}: Retrieve details of users by location.
POST /users: Insert a new user. Support input types: JSON, form data, and query parameters.
DELETE /users/{id}: Delete a user by ID.
HTML Rendering:
Implement an API endpoint to display user data in JSON format in HTML using render_template.

Instructions:
Setting up the project:
Initialize a new Flask project.
Create a virtual environment for the project.
Install Flask and any other necessary dependencies.
User Class:
Create a Python class User with the specified attributes.

Data Storage:
Implement methods to read and write user data to a CSV file.
Endpoints:
Implement the specified endpoints using Flask routes.
Use appropriate request and response formats for each endpoint.
Test each endpoint using a tool like Postman or curl.
HTML Rendering:
Implement an API endpoint to display user data in JSON format in HTML using render_template.
