from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rahasia'  # Digunakan untuk menyimpan session login

# Akun pengguna (dummy)
USER_CREDENTIALS = {
    'admin': 'admin'
}

# ========================
# ROUTE: Halaman Login
# ========================
@app.route("/")
def index():
    return render_template("login.html")

# ========================
# ROUTE: Proses Login
# ========================
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return """
        <h3>Login gagal!</h3>
        <p>Username atau password salah.</p>
        <a href='/'>Kembali ke login</a>
        """

# ========================
# ROUTE: Dashboard
# ========================
@app.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template("dashboard.html")

# ========================
# ROUTE: Tambah Data
# ========================
@app.route("/create", methods=["GET", "POST"])
def create():
    if 'user' not in session:
        return redirect(url_for('index'))

    if request.method == "POST":
        nama = request.form.get("nama")
        jumlah = request.form.get("jumlah")
        
        if nama and jumlah:
            print(f"Data disimpan: {nama}, jumlah: {jumlah}")  # Log ke terminal
            return render_template("success.html")
        else:
            return """
            <h3>Data tidak lengkap!</h3>
            <a href='/create'>Coba lagi</a>
            """

    return render_template("create.html")

# ========================
# ROUTE: Logout
# ========================
@app.route("/logout")
def logout():
    session.pop('user', None)
    return render_template("logout.html")

# ========================
# RUN APP
# ========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
