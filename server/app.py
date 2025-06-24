from flask import Flask, render_template, request, redirect, session, url_for, flash
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
app.secret_key = os.urandom(24)

def get_db_connection():
    conn = sqlite3.connect('../foodapp.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/restaurants')
def show_restaurants():
    conn = get_db_connection()
    restaurants = conn.execute('SELECT * FROM restaurants').fetchall()
    conn.close()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/<int:restaurant_id>/menu')
def view_menu(restaurant_id):
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM restaurants WHERE id = ?', (restaurant_id,)).fetchone()
    menu_items = conn.execute('SELECT * FROM menu_items WHERE restaurant_id = ?', (restaurant_id,)).fetchall()
    conn.close()
    return render_template('menu.html', restaurant=restaurant, menu_items=menu_items)

@app.route('/cart')
def view_cart():
    return render_template('cart.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                         (username, email, password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect('/login')
        except sqlite3.IntegrityError:
            flash('Username or email already exists!', 'error')
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect('/')
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect('/')

if __name__ == '__main__':
    if os.environ.get("FLASK_ENV") == "development":
        print("🚀 Starting Flask App locally...")
        print("🔗 Open http://localhost:5000/ in your browser")
        app.run(debug=True)
    else:
        from waitress import serve
        print("🚀 Starting production server with Waitress...")
        serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
