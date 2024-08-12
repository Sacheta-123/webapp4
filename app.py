import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to webhooks!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you? This is my new update to the app.py to test the OpenShift Webhooks'

@app.route('/test')
def hello():
    return "Well, the test works!!!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
