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

def add_order(product_id):
    execute_query('INSERT INTO orders (product_id) VALUES (?)', (product_id,))

def update_order(id, product_id):
    execute_query('UPDATE orders SET product_id = ? WHERE id = ?', (product_id, id))

def delete_order(id):
    execute_query('DELETE FROM orders WHERE id = ?', (id,))

def list_orders():
    return fetch_all('SELECT * FROM orders')