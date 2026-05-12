import json


# LOAD DATA FROM FILE
try:

    with open("inventory.json", "r") as file:
        products = json.load(file)

except FileNotFoundError:

    products = {
        "laptop": {
            "price": 5000,
            "stock": 10
        },

        "mouse": {
            "price": 500,
            "stock": 25
        }
    }


# SAVE DATA FUNCTION
def save_data():

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)


# ADD PRODUCT
def add_product():

    name = input("Enter product name: ")

    try:
        price = int(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))

    except ValueError:
        print("Please enter numbers only")
        return

    products[name] = {
        "price": price,
        "stock": stock
    }

    save_data()

    print("Product Added Successfully")


# VIEW PRODUCTS
def view_products():

    print("\n===== Product List =====")

    if not products:
        print("No Products Available")
        return

    for name, details in products.items():

        print("\nProduct Name:", name)
        print("Price:", details["price"])
        print("Stock:", details["stock"])


# UPDATE STOCK
def update_stock():

    name = input("Enter product name to update: ")

    if name in products:

        try:
            new_stock = int(input("Enter new stock quantity: "))

        except ValueError:
            print("Please enter valid number")
            return

        products[name]["stock"] = new_stock

        save_data()

        print("Stock Updated Successfully")

    else:
        print("Product Not Found")


# DELETE PRODUCT
def delete_product():

    name = input("Enter product name to delete: ")

    if name in products:

        del products[name]

        save_data()

        print("Product Deleted Successfully")

    else:
        print("Product Not Found")


# SEARCH PRODUCT
def search_product():

    name = input("Enter product name to search: ")

    if name in products:

        print("\n===== Product Found =====")
        print("Price:", products[name]["price"])
        print("Stock:", products[name]["stock"])

    else:
        print("Product Not Found")


# LOW STOCK ALERT
def low_stock_alert():

    print("\n===== Low Stock Products =====")

    found = False

    for name, details in products.items():

        if details["stock"] < 5:

            print(f"{name} has low stock: {details['stock']}")
            found = True

    if not found:
        print("No Low Stock Products")


# BILLING SYSTEM
def billing_system():

    total_bill = 0

    while True:

        name = input("Enter product name (or type done): ")

        if name.lower() == "done":
            break

        if name in products:

            try:
                quantity = int(input("Enter quantity: "))

            except ValueError:
                print("Please enter valid quantity")
                continue

            if quantity <= products[name]["stock"]:

                price = products[name]["price"]

                total = price * quantity

                total_bill += total

                products[name]["stock"] -= quantity

                print(f"{name} added to bill")
                print(f"Cost: {total}")

            else:
                print("Not enough stock available")

        else:
            print("Product Not Found")

    save_data()

    print("\n===== FINAL BILL =====")
    print("Total Amount:", total_bill)


# MAIN MENU
while True:

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Low Stock Alert")
    print("7. Billing System")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        search_product()

    elif choice == "6":
        low_stock_alert()

    elif choice == "7":
        billing_system()

    elif choice == "8":
        print("Exiting System...")
        break

    else:
        print("Invalid Choice")