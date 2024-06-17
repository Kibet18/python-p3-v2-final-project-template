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

def add_product(name, description, cost):
    execute_query('INSERT INTO products (name, description, cost) VALUES (?, ?, ?)', (name, description, cost))

def update_product(id, name, description, cost):
    execute_query('UPDATE products SET name = ?, description = ?, cost = ? WHERE id = ?', (name, description, cost, id))

def delete_product(id):
    execute_query('DELETE FROM products WHERE id = ?', (id,))

def list_products():
    return fetch_all('SELECT * FROM products')

def get_product(id):
    return fetch_one('SELECT * FROM products WHERE id = ?', (id,))