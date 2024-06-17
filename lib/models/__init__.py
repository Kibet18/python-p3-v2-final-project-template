import sqlite3

CONN = sqlite3.connect('product.db')
CURSOR = CONN.cursor()
