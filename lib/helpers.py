# lib/helpers.py

from models.products import Products
from models.orders import Order
from models.users import User
from datetime import datetime

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

# Product Management
def display_products():
    products = Products.get_all()
    for product in products:
        print(product)

def display_products_by_brand():
    brand = input("Enter the brand: ")
    products = Products.find_by_brand(brand)
    for product in products:
        print(product)

def create_product():
    brand = input("Enter the brand: ")
    name = input("Enter the name: ")
    price = float(input("Enter the price: "))
    stock = int(input("Enter the stock: "))
    Products.create(brand, name, price, stock)
    print("Product created successfully!")

def update_product():
    id = int(input("Enter the product ID to update: "))
    product = Products.find_by_id(id)
    if product:
        product.brand = input(f"Enter the new brand (current: {product.brand}): ") or product.brand
        product.name = input(f"Enter the new name (current: {product.name}): ") or product.name
        product.price = float(input(f"Enter the new price (current: {product.price}): ") or product.price)
        product.description = float(input(f"Enter the new stock (current: {product.description}): ") or product.description)
        product.update()
        print("Product updated successfully!")
    else:
        print("Product not found.")

def delete_product():
    id = int(input("Enter the product ID to delete: "))
    product = Products.find_by_id(id)
    if product:
        product.delete()
        print("Product deleted successfully!")
    else:
        print("Product not found.")

# Brand Management
def display_brands():
    brands = set(product.brand for product in Products.get_all())
    for brand in brands:
        print(brand)

def create_brand():
    print("To create a new brand, add a new product with that brand name.")

def update_brand():
    print("To update a brand, update the brand field of the respective products.")

def delete_brand():
    print("To delete a brand, delete all products with that brand.")

# User Management
def display_users():
    users = User.get_all()
    for user in users:
        print(user)

def display_user_by_name():
    name = input("Enter the name: ")
    user = User.find_by_name(name)
    if user:
        print(user)
    else:
        print("User not found.")

def create_user():
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")
    User.create(name, email, phone)
    print("User created successfully!")

def update_user():
    id = int(input("Enter the user ID to update: "))
    user = User.find_by_id(id)
    if user:
        user.name = input(f"Enter the new name (current: {user.name}): ") or user.name
        user.email = input(f"Enter the new email (current: {user.email}): ") or user.email
        user.phone = input(f"Enter the new phone (current: {user.phone}): ") or user.phone
        user.update()
        print("User updated successfully!")
    else:
        print("User not found.")

def delete_user():
    id = int(input("Enter the user ID to delete: "))
    user = User.find_by_id(id)
    if user:
        user.delete()
        print("User deleted successfully!")
    else:
        print("User not found.")

# Order Management
def display_orders():
    orders = Order.get_all()
    for order in orders:
        print(order)

def display_orders_by_product():
    product_id = int(input("Enter the product ID: "))
    orders = Order.find_by_product_id(product_id)
    for order in orders:
        print(order)

def display_orders_by_brand():
    brand = input("Enter the brand: ")
    products = Products.find_by_brand(brand)
    product_ids = [product.id for product in products]
    for product_id in product_ids:
        orders = Order.find_by_product_id(product_id)
        for order in orders:
            print(order)

def create_order():
    product_id = int(input("Enter the product ID: "))
    quantity = int(input("Enter the quantity: "))
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = input("Enter the status: ")
    user_id = int(input("Enter the user ID: "))
    Order.create(product_id, quantity, order_date, status, user_id)
    print("Order created successfully!")

def update_order():
    id = int(input("Enter the order ID to update: "))
    order = Order.find_by_id(id)
    if order:
        order.product_id = int(input(f"Enter the new product ID (current: {order.product_id}): ") or order.product_id)
        order.quantity = int(input(f"Enter the new quantity (current: {order.quantity}): ") or order.quantity)
        order.status = input(f"Enter the new status (current: {order.status}): ") or order.status
        order.user_id = int(input(f"Enter the new user ID (current: {order.user_id}): ") or order.user_id)
        order.update()
        print("Order updated successfully!")
    else:
        print("Order not found.")
