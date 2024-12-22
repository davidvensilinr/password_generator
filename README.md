Password Manager Web App

A simple and secure password manager web application built with Flask and JSON for data storage. This app allows users to register, login, generate passwords for specific domains, and securely store and retrieve them.

Features

User Authentication

Secure registration and login functionality.

Password Generation

Generate random passwords for specific domains.

Customize the length of the password.

Password Storage

Store generated passwords in a JSON file.

Retrieve stored passwords upon subsequent logins.

User-friendly Interface

Simple and responsive design for ease of use.

Directory Structure

project-root/
├── app.py               # Main Flask application
├── static/
│   ├── style.css        # CSS for styling the web app
├── templates/
│   ├── login.html       # Login page template
│   ├── register.html    # Registration page template
│   ├── dashboard.html   # Dashboard page template
├── data.json            # JSON file to store user data
└── README.md            # Documentation for the project

Requirements

Python 3.10 or higher

Flask

Installation

Clone the repository:

git clone https://github.com/your-repo/password-manager.git
cd password-manager

Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install flask

Run the application:

python app.py

Access the app:
Open your browser and navigate to http://127.0.0.1:5000/.

Usage

Register:

Create an account with a username and password.

Login:

Log in using your credentials.

Generate Password:

Enter a domain name and specify the character length for the password.

Generate and save the password.

View Saved Passwords:

Access previously saved passwords after logging in.

Logout:

Securely logout from the application.

How Data is Stored

All user data, including credentials and generated passwords, are securely stored in a data.json file in the following format:

{
    "username": {
        "password": "user_password",
        "saved_passwords": {
            "domain1": "generated_password1",
            "domain2": "generated_password2"
        }
    }
}

Security Considerations

JSON Storage:

The data.json file is used for simplicity. For production, consider switching to a secure database.

Password Protection:

User passwords are stored in plaintext for demonstration purposes. Use hashing (e.g., bcrypt) for added security.

Session Management:

Flask sessions are used to manage user sessions. Ensure the SECRET_KEY in Flask is securely set.

Future Enhancements

Add password encryption for storage.

Implement password recovery.

Use a database like SQLite or PostgreSQL for better scalability.

Enhance UI/UX with more interactive elements.

License

This project is open-source and available under the MIT License.

Acknowledgements

Built with Flask and inspired by the need for simple password management solutions.
