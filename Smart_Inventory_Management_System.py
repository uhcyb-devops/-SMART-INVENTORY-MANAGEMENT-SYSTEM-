import random
import json
from datetime import datetime
import time

# ================= WELCOME SCREEN =================

def welcome_screen():
    print("==================================================================")
    print("        SMART INVENTORY MANAGEMENT SYSTEM         ")
    print("==================================================================")
    print("             Developed by: Shahzaib               ")
    print("==================================================================")


# ================= LOADING SCREEN =================

def loading_screen():
    print("\nLoading System...")
    time.sleep(1)
    print("Welcome to the Dashboard!")


# ================= LOGIN PAGE =================

def login_admin():

    username = "admin"
    password = "1234"

    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == username and entered_password == password:
        print("\nLogin Successful!")
        return True

    else:
        print("\nInvalid Username or Password!")
        return False


# ================= PRODUCT DATA =================

catalog = []

inventory = []

sales = []

FILE_NAME = "products.json"
SALES_FILE = "sales.json"


# Load products from file

def load_products():
    global catalog
    try:
        with open(FILE_NAME, "r") as file:
            catalog = json.load(file)
    except FileNotFoundError:
        catalog = []

# Save products to file

def save_products():

    with open(FILE_NAME, "w") as file:
        json.dump(catalog, file, indent=5)

# Load sales from file

def load_sales():
    global sales
    try:
        with open(SALES_FILE, "r") as file:
            sales = json.load(file)

    except FileNotFoundError:
        sales = []

# Save sales to file

def save_sales():
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=5)

# ================= MAIN MENU =================

def main_menu():

    while True:

        print("-------------------------------------------------")
        print("                    MAIN MENU         ")
        print("-------------------------------------------------")

        print("""
1. Inventory Management
2. Sales & Billing
3. Exit
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            inventory_management()

        elif choice == "2":
            sales_billing()

        elif choice == "3":
            print("\nThank You For Using Smart Inventory Management System.")
            print("System Closed Successfully!")
            return

        else:
            print("\nInvalid Choice!")


# ================= INVENTORY MANAGEMENT =================

def inventory_management():

    while True:

        print("---------------------------------------------------------")
        print("            INVENTORY MANAGEMENT      ")
        print("---------------------------------------------------------")

        print("""
1. Product Catalog
2. View Inventory
3. Back
""")

        choice = input("Enter your Choice: ")

        if choice == "1":
            product_catalog()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            return

        else:
            print("Invalid Choice!")


# ================= PRODUCT CATALOG =================

def product_catalog():

    while True:

        print("============================================================")
        print("              PRODUCT CATALOG              ")
        print("============================================================")

        print("""
1. Add Product
2. View Products
3. Delete Product
4. Back
""")
        choice = input("Enter Choice: ")
        if choice == "1":

            if len(catalog) == 0:
                product_id = 1
            else:
                product_id = max(product["id"] for product in catalog) + 1

            product_name = input("Enter Product Name: ")
            product_price = float(input("Enter Product Price: "))
            product_quantity = int(input("Enter Product Quantity: "))

            product = {
                "id": product_id,
                "name": product_name,
                "price": product_price,
                "quantity": product_quantity
            }
            catalog.append(product)

            save_products()

            print("\nProduct Added Successfully And Saved!")

        elif choice == "2":

            if len(catalog) == 0:

                print("\nNo Products Available.")

            else:

                print("\nAvailable Products\n")

                for product in catalog:

                    print(f"""
ID       : {product['id']}
Name     : {product['name']}
Price    : Rs.{product['price']}
Quantity : {product['quantity']}
----------------------------------------
""")

            input("Press Enter To Continue...")

        elif choice == "3":

            if len(catalog) == 0:
                print("\nNo Products Available.")
                input("Press Enter To Continue...")
                continue

            delete_search = input("\nEnter Product Name or ID to Delete: ")

            product_to_delete = None

            for product in catalog:
                if str(product["id"]) == delete_search or product["name"].lower() == delete_search.lower():
                    product_to_delete = product
                    break

            if product_to_delete is None:
                print("\nProduct Not Found!")
                input("Press Enter To Continue...")
                continue

            print(f"\nFound: {product_to_delete['name']} - Rs.{product_to_delete['price']} (Stock: {product_to_delete['quantity']})")

            confirm_delete = input(f"Are you sure you want to delete '{product_to_delete['name']}'? (y/n): ")

            if confirm_delete.lower() == "y":
                catalog.remove(product_to_delete)
                save_products()
                print(f"\n'{product_to_delete['name']}' has been deleted successfully!")
            else:
                print("\nDelete Cancelled.")

            input("Press Enter To Continue...")

        elif choice == "4":
            break

        else:
            print("Invalid Choice!")


# ================= VIEW INVENTORY =================

def view_inventory():

    print("==========================================================")
    print("             VIEW INVENTORY        ")
    print("==========================================================")

    if len(inventory) == 0:
        print("Inventory is Empty.")

    else:
        for item in inventory:
            print(item)

    input("\nPress Enter To Continue...")

# ================= SALES & BILLING =================

def sales_billing():

    while True:

        print("\n======================================================")
        print("              SALES & BILLING      ")
        print("========================================================")

        print("""
1. Smart Shop
2. Sales History
3. Back
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            smart_shop()

        elif choice == "2":
            sales_history()

        elif choice == "3":
            break

        else:
            print("Invalid Choice!")


# ================= SMART SHOP =================

def smart_shop():

    while True:

        print("\n====================================================")
        print("                 SMART SHOP        ")
        print("======================================================")

        if len(catalog) == 0:
            print("No Products Available!")
            input("\nPress Enter To Continue...")
            break

        search = input("\nEnter Product Name or ID to Search (0 to Back): ")

        if search == "0":
            break

        selected_product = None

        for product in catalog:
            if str(product["id"]) == search or product["name"].lower() == search.lower():
                selected_product = product
                break

        if selected_product is None:
            print("\nProduct Not Found! Please Try Again.")
            input("Press Enter To Continue...")
            continue

        product_name = selected_product["name"]
        price = selected_product["price"]
        stock = selected_product["quantity"]

        print(f"\nFound: {product_name} - Rs.{price} (Stock: {stock})")

        confirm = input("Do you want to buy this product? (y/n): ")

        if confirm.lower() != "y":
            continue

        quantity = int(input("Enter Quantity: "))

        if quantity > stock:
            print(f"\nOnly {stock} in stock! Selling {stock} instead of {quantity}.")
            quantity = stock

        if quantity == 0:
            print("No stock available for this product!")
            continue

        total = price * quantity

        print("""
Discount Available
1. Student Discount (10%)
2. Member Discount (15%)
3. No Discount
""")

        discount = input("Choose Discount: ")

        if discount == "1":
            discount_amount = total * 0.10

        elif discount == "2":
            discount_amount = total * 0.15

        else:
            discount_amount = 0

        final_bill = total - discount_amount

        # Update Stock
        selected_product["quantity"] -= quantity
        save_products()

        receipt_no = random.randint(1000, 9999)
        today = datetime.now()

        sale_record = {
            "receipt_no": receipt_no,
            "date": today.strftime('%d-%m-%Y'),
            "time": today.strftime('%H:%M:%S'),
            "product": product_name,
            "price": price,
            "quantity": quantity,
            "subtotal": total,
            "discount": discount_amount,
            "total": final_bill
        }

        sales.append(sale_record)
        save_sales()

        print("\n=======================================================")
        print("                CUSTOMER RECEIPT")
        print("=======================================================")
        print(f"Receipt No : {receipt_no}")
        print(f"Date       : {today.strftime('%d-%m-%Y')}")
        print(f"Time       : {today.strftime('%H:%M:%S')}")
        print("-------------------------------------------------------")
        print(f"Product    : {product_name}")
        print(f"Price      : Rs.{price}")
        print(f"Quantity   : {quantity}")
        print("-------------------------------------------------------")
        print(f"Subtotal   : Rs.{total}")
        print(f"Discount   : Rs.{discount_amount:.0f}")
        print(f"Total Bill : Rs.{final_bill:.0f}")
        print("Payment    : Paid")
        print("=======================================================")

        input("\nPress Enter To Continue...")

        
# ================= SALES HISTORY =================

def sales_history():

    print("\n============================================================")
    print("              SALES HISTORY         ")
    print("==============================================================")

    if len(sales) == 0:
        print("\nNo Sales History Available.")

    else:
        for sale in sales:
            print(f"""
Receipt No : {sale['receipt_no']}
Date       : {sale['date']}
Time       : {sale['time']}
----------------------------------------
Product    : {sale['product']}
Price      : Rs.{sale['price']}
Quantity   : {sale['quantity']}
----------------------------------------
Subtotal   : Rs.{sale['subtotal']}
Discount   : Rs.{sale['discount']:.0f}
Total      : Rs.{sale['total']:.0f}
========================================
""")

    input("\nPress Enter To Continue...")

load_products()
load_sales()
welcome_screen()
loading_screen()

if login_admin():
    main_menu()
else:
    print("Access Denied!")