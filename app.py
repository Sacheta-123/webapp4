import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret"  # untuk session login

@app.route("/")
def main():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Dummy login
    if username == "admin" and password == "admin":
        session["username"] = username
        return redirect(url_for("dashboard"))
    else:
        return "Login gagal. <a href='/'>Coba lagi</a>"

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    return redirect(url_for("main"))

@app.route("/create", methods=["GET", "POST"])
def create():
    if "username" not in session:
        return redirect(url_for("main"))

    if request.method == "POST":
        item_name = request.form.get("item_name")
        message = f"Item '{item_name}' berhasil ditambahkan!"
        return render_template("success.html", message=message)

    return render_template("create.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")

@app.route("/how are you")
def hello():
    return "I am good, how about you?"

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is a simple Flask app for testing PR.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
