from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rahasia123'  # Untuk session

# Dummy login
USER_CREDENTIALS = {
    'admin': 'admin'
}

# Halaman utama / login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Username atau password salah.")
    return render_template('login.html')

# Dashboard setelah login
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

# Halaman create item
@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        item_name = request.form['item_name']
        # Di sini bisa ditambahkan logika menyimpan item ke database
        print(f"Item ditambahkan: {item_name}")  # Debug ke terminal
        return redirect(url_for('success'))
    return render_template('create.html')

# Halaman sukses setelah create
@app.route('/success')
def success():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('success.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Menjalankan app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
