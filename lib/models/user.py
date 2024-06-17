import sqlite3

DATABASE = 'shop.db'

def execute_query(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_all(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def fetch_one(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result

def add_user(username, order_id):
    execute_query('INSERT INTO users (username, order_id) VALUES (?, ?)', (username, order_id))

def update_user(id, username, order_id):
    execute_query('UPDATE users SET username = ?, order_id = ? WHERE id = ?', (username, order_id, id))

def delete_user(id):
    execute_query('DELETE FROM users WHERE id = ?', (id,))

def list_users():
    return fetch_all('SELECT * FROM users')

def get_user(id):
    return fetch_one('SELECT * FROM users WHERE id = ?', (id,))