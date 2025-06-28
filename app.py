import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            return redirect("/dashboard")
        return "Login failed"
    return render_template_string("""
        <form method="POST">
            <input name="username" placeholder="Username"><br>
            <input name="password" type="password" placeholder="Password"><br>
            <button type="submit">Login</button>
        </form>
    """)

@app.route("/dashboard")
def dashboard():
    return "You are logged in!"

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        item = request.form["item"]
        return f"Item '{item}' added!"
    return render_template_string("""
        <form method="POST">
            <input name="item" placeholder="Enter item"><br>
            <button type="submit">Add Item</button>
        </form>
    """)

@app.route("/logout")
def logout():
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

