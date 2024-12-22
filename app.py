import json
import os
import random
import string
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key
DATA_FILE = "data.json"


# Load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# Route for login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        data = load_data()

        # Validate login
        if username in data and data[username]["password"] == password:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.")
    return render_template("login.html")


# Route for dashboard
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    data = load_data()

    if request.method == "POST":
        domain = request.form["domain"]
        char_length = int(request.form["char_length"])
        password = generate_password(char_length)

        # Save password in user's record
        if "passwords" not in data[username]:
            data[username]["passwords"] = {}
        data[username]["passwords"][domain] = password
        save_data(data)

    user_passwords = data[username].get("passwords", {})
    return render_template(
        "dashboard.html", username=username, passwords=user_passwords
    )


# Route for logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


# Generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


# Register a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        data = load_data()

        if username in data:
            flash("Username already exists.")
        else:
            data[username] = {"password": password, "passwords": {}}
            save_data(data)
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
