import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how are you")
def hello():
    return "I am good, how about you?"

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is a simple Flask app for testing PR.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
