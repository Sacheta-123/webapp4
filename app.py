from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "selamat datang di akun milik iqbal yusanta"

@app.route("/about")
def about():
    return "Ini halaman About"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
