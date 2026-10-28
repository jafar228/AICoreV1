
from flask import Flask, request, render_template
from DataManage import authenticate,register_user
import os

app = Flask(__name__)

app.secret_key = os.environ.get("SERJAF_SECRET_KEY", "dev-only-change-me")

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("login", "")
    password = request.form.get("password", "")

    if authenticate(username, password):
        return f"Welcome {username} to SerJaf!"

    return render_template(
        "login.html",error="Invalid username or password!"), 401


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    birthday = request.form.get("birthday", "").strip()
    email = request.form.get("email", "").strip()

    if not username or not password or not birthday or not email:
        return "All fields are required", 400

    success, message = register_user(
        username, password, birthday, email
    )

    if success:
        return f"Welcome to SerJaf, {username}!"

    return message, 400

if __name__ == "__main__":
    app.run(debug=True)
