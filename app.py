from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Selamat Datang!</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f0f8ff; }
                h1 { color: #333; }
                p { font-size: 18px; }
                a.button {
                    display: inline-block;
                    padding: 10px 20px;
                    margin-top: 20px;
                    font-size: 16px;
                    color: white;
                    background-color: #007BFF;
                    border: none;
                    border-radius: 5px;
                    text-decoration: none;
                }
                a.button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Selamat datang di aplikasi web Flask!</h1>
            <p>Hai, saya <strong>Iqbal Yusanta</strong> (A710230023), ini adalah proyek praktikum saya menggunakan Python Flask.</p>
            <p>Silakan coba tombol di bawah ini untuk melihat halaman lain:</p>
            <a href="/about" class="button">Ke Halaman About</a>
        </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <html>
        <head><title>About</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h2>📄 Halaman Tentang</h2>
            <p>Aplikasi ini dibuat oleh Iqbal Yusanta untuk latihan menggunakan Flask.</p>
            <a href="/" style="text-decoration: none; color: #007BFF;">⬅️ Kembali ke Beranda</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



