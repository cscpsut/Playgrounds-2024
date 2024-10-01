from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os
app = Flask(__name__)

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Set up the database (run this once)
def setup_database():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'R@nd0mP@s$0213ll!')")
    conn.execute("INSERT INTO users (username, password) VALUES ('u1', 'password1cewr34r352')")
    conn.execute("INSERT INTO users (username, password) VALUES ('u2', 'password2c3254c2rwc2')")
    conn.commit()
    conn.close()

# Vulnerable login form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = get_db_connection()
            # Use an insecure query to allow SQL injection
            # query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}' LIMIT 1"
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            user = conn.execute(query).fetchall()
            conn.close()

            # Check if exactly one user was returned
            if len(user) == 1:
                return redirect(url_for('admin'))
            elif len(user) > 1:
                return render_template('index.html', error="Careful, you are using more than one card!")
            else:
                return render_template('index.html', error="Wrong cards!")

        except:
            return render_template('index.html', error="An error occurred while processing your request.")

    return render_template('index.html')

# Admin page where the flag is stored
@app.route('/admin')
def admin():
    return render_template('admin.html', flag=os.environ["FLAG"])

if __name__ == '__main__':
    setup_database()
    app.run(debug=False)
