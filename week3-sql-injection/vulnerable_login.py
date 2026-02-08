from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')

# Insert admin and user accounts
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
c.execute("INSERT INTO users (username, password) VALUES ('user', 'userpass')")
conn.commit()

conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # SQL Injection vulnerability using f-strings
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(query)
        user = c.fetchone()
        conn.close()
        if user:
            return redirect(url_for('welcome'))
        else:
            return 'Invalid credentials!'
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return 'Welcome! You have successfully logged in.'

if __name__ == '__main__':
    app.run(debug=True)
