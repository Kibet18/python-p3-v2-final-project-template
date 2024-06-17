# cli.py

from helpers import (
    exit_program,
    display_products,
    display_products_by_brand,
    create_product,
    update_product,
    delete_product,
    display_brands,
    create_brand,
    update_brand,
    delete_brand,
)

def main():
    current_menu = "main"
    while True:
        if current_menu == "main":
            main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                current_menu = "products"
            elif choice == "2":
                current_menu = "brand"
            elif choice == "3":
                exit_program()
            else:
                print("Invalid choice. Please try again.")
        
        elif current_menu == "products":
            current_menu = product_menu()
        
        elif current_menu == "brand":
            current_menu = brand_menu()

def main_menu():
    print("Welcome to Product Inventory Management System (PIMS)")
    print("Please select a category:")
    print("1. Product Management")
    print("2. Brand Management")
    print("3. Exit the system")

def product_menu():
    while True:
        print("\nProduct Management Menu:")
        print("1. Display all products")
        print("2. Display products by brand")
        print("3. Create product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Return to main menu")
        print("7. Go to Brand Management")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_products()
        elif choice == "2":
            display_products_by_brand()
        elif choice == "3":
            create_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            return "main"
        elif choice == "7":
            return "brand"
        else:
            print("Invalid choice. Please try again.")

def brand_menu():
    while True:
        print("\nBrand Management Menu:")
        print("1. Display all brands")
        print("2. Create brand")
        print("3. Update brand")
        print("4. Delete brand")
        print("5. Return to main menu")
        print("6. Go to Product Management")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_brands()
        elif choice == "2":
            create_brand()
        elif choice == "3":
            update_brand()
        elif choice == "4":
            delete_brand()
        elif choice == "5":
            return "main"
        elif choice == "6":
            return "product"
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
