from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'rahasia123'

# Simulasi database
USERS = {'admin': 'admin123'}
ITEMS = []  # Menyimpan item berupa dict {'name': ..., 'description': ...}

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash("Login gagal! Username atau password salah.")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', items=ITEMS)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        
        if name and description:
            ITEMS.append({'name': name, 'description': description})
            return redirect(url_for('success'))
        else:
            flash("Semua field wajib diisi!")
    
    return render_template('create.html')

@app.route('/success')
def success():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('success.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
