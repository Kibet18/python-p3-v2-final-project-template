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

def add_brand(name, product_id):
    execute_query('INSERT INTO brands (name, product_id) VALUES (?, ?)', (name, product_id))

def update_brand(id, name, product_id):
    execute_query('UPDATE brands SET name = ?, product_id = ? WHERE id = ?', (name, product_id, id))

def delete_brand(id):
    execute_query('DELETE FROM brands WHERE id = ?', (id,))

def list_brands():
    return fetch_all('SELECT * FROM brands')

def get_brand(id):
    return fetch_one('SELECT * FROM brands WHERE id = ?', (id,))