import sqlite3

DATABASE = 'shop.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS brands (
    id INTEGER PRIMARY KEY,
    name TEXT,
    product_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    order_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    product_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    cost INTEGER
)
''')

conn.commit()
conn.close()