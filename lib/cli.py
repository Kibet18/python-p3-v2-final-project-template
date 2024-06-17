from models import brand, user, product, order

def add_brand():
    name = input("Enter brand name: ")
    product_id = input("Enter product ID: ")
    brand.add_brand(name, product_id)
    print(f'Brand {name} added.')

def update_brand():
    id = input("Enter brand ID: ")
    name = input("Enter new brand name: ")
    product_id = input("Enter new product ID: ")
    brand.update_brand(id, name, product_id)
    print(f'Brand with ID {id} updated.')

def delete_brand():
    id = input("Enter brand ID to delete: ")
    brand.delete_brand(id)
    print(f'Brand with ID {id} deleted.')

def list_brands():
    brands = brand.list_brands()
    for b in brands:
        print(f'Brand ID: {b[0]}, Name: {b[1]}, Product ID: {b[2]}')

def add_user():
    username = input("Enter username: ")
    order_id = input("Enter order ID: ")
    user.add_user(username, order_id)
    print(f'User {username} added.')

def update_user():
    id = input("Enter user ID: ")
    username = input("Enter new username: ")
    order_id = input("Enter new order ID: ")
    user.update_user(id, username, order_id)
    print(f'User with ID {id} updated.')

def delete_user():
    id = input("Enter user ID to delete: ")
    user.delete_user(id)
    print(f'User with ID {id} deleted.')

def list_users():
    users = user.list_users()
    for u in users:
        print(f'User ID: {u[0]}, Username: {u[1]}, Order ID: {u[2]}')

def add_order():
    product_id = input("Enter product ID: ")
    order.add_order(product_id)
    print(f'Order for product {product_id} added.')

def update_order():
    id = input("Enter order ID: ")
    product_id = input("Enter new product ID: ")
    order.update_order(id, product_id)
    print(f'Order with ID {id} updated.')

def delete_order():
    id = input("Enter order ID to delete: ")
    order.delete_order(id)
    print(f'Order with ID {id} deleted.')

def list_orders():
    orders = order.list_orders()
    for o in orders:
        print(f'Order ID: {o[0]}, Product ID: {o[1]}')

def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    cost = input("Enter product cost: ")
    product.add_product(name, description, cost)
    print(f'Product {name} added.')

def update_product():
    id = input("Enter product ID: ")
    name = input("Enter new product name: ")
    description = input("Enter new product description: ")
    cost = input("Enter new product cost: ")
    product.update_product(id, name, description, cost)
    print(f'Product with ID {id} updated.')

def delete_product():
    id = input("Enter product ID to delete: ")
    product.delete_product(id)
    print(f'Product with ID {id} deleted.')

def list_products():
    products = product.list_products()
    for p in products:
        print(f'Product ID: {p[0]}, Name: {p[1]}, Description: {p[2]}, Cost: {p[3]}')

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Add Brand")
        print("2. Update Brand")
        print("3. Delete Brand")
        print("4. List Brands")
        print("5. Add User")
        print("6. Update User")
        print("7. Delete User")
        print("8. List Users")
        print("9. Add Order")
        print("10. Update Order")
        print("11. Delete Order")
        print("12. List Orders")
        print("13. Add Product")
        print("14. Update Product")
        print("15. Delete Product")
        print("16. List Products")
        print("17. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_brand()
        elif choice == '2':
            update_brand()
        elif choice == '3':
            delete_brand()
        elif choice == '4':
            list_brands()
        elif choice == '5':
            add_user()
        elif choice == '6':
            update_user()
        elif choice == '7':
            delete_user()
        elif choice == '8':
            list_users()
        elif choice == '9':
            add_order()
        elif choice == '10':
            update_order()
        elif choice == '11':
            delete_order()
        elif choice == '12':
            list_orders()
        elif choice == '13':
            add_product()
        elif choice == '14':
            update_product()
        elif choice == '15':
            delete_product()
        elif choice == '16':
            list_products()
        elif choice == '17':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()