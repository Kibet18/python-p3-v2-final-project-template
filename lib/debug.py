#!/usr/bin/env python3
# lib/debug.py

# reset_database.py
from models.__init__ import CONN, CURSOR
from models.orders import Order
from models.products import Product
from models.users import User
from datetime import datetime

def reset_database():
    Product.drop_table()
    Product.create_table()

    # Create seed data
    Product.create("Apple", "iPhone 13", 45999.99 )
    Product.create("Samsung", "Galaxy S21", 12999.99)
    Product.create("Tenco", "Pixel 5", 26999.99)
    Product.create("Realme", "C55", 23999.99)
    Product.create("Vivo", "Y03", 18999.99)
    Product.create("Huawei", "P40 Pro", 25999.99)
    Product.create("Vivo", "Y02t", 12999.99, 35)
    Product.create("Infinix", "V60 ThinQ", 30999.99)
    Product.create("Redmi", "A3", 13999.99)
    Product.create("Nokia", "8.3 5G", 11999.99)
    Product.create("Tenco", "Spark20", 45999.99)
    Product.create("Redmi", "12c", 26999.99)
    Product.create("Samsung", "Galaxy S27", 25999.99)
    Product.create("Apple", "iPhone 15", 30999.99)
    Product.create("Oppo", "Find X3 Pro", 35999.99)
    Product.create("Apple", "iPhone 11", 35999.99)
    Product.create("Samsung", "Galaxy S24", 18999)
    Product.create("Realme", "C51", 13999.99)
    Product.create("Vivo", "Y27s", 26999.99)
    Product.create("Huawei", "P40 Pro", 23999.99)
    Product.create("Vivo", "V29", 30999.99)
    Product.create("Samsung", "Galaxy S23", 13999.99)
    Product.create("Infinix", "V60 ThinQ", 45999.99)
    Product.create("Redmi", "13c", 18999.99)
    Product.create("Nokia", "8.3 5G", 13999.99, 30)
    Product.create("Tenco", "U20 5G", 23999.99, 15)
  
    
    Order.drop_table()
    Order.create_table()

    # Create seed data
    Order.create(1, 10, datetime.now(), 'pending', 1)
    Order.create(2, 20, datetime.now(), 'shipped', 2)
    Order.create(3, 10, datetime.now(), 'delivered', 3)
    Order.create(4, 30, datetime.now(), 'canceled', 4)
    Order.create(5, 20, datetime.now(), 'pending', 5)
    
    User.drop_table()
    User.create_table()
    
    User.create("John Doe", "john@gmail.com", 789675434)
    User.create("Jane Smith", "jane@gmail.com", 9876543210)
    User.create("Ivy Kerubo", "sokoro@gmail.com", 7654321098)
    User.create("Gideon Bett", "giddy@gmail.com", 5432109876)
    User.create("Angela Mukami", "angie@gmail.com", 3210987654)
    User.create("Eliza Kangeo", "lizzy@gmail.com", 1098765432)
  

# Run reset_database
if __name__ == "__main__":
    reset_database()

