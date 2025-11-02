items={'laptop':{'price':800,'quantity':1}}
def main_menu():
    while True:
        print("Shopping Cart Menu")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
            pass
        elif choice == "2":
            remove_item()
            pass
        elif choice == "3":
            update_quantity()
            pass
        elif choice == "4":
            view_cart()
            pass
        elif choice == "5":
            checkout()
            pass
        elif choice == "6":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")
        print("--"*10)


def add_item():
    try:
        name=input("Item name: ")
    except ValueError:
        print("Invalid input")
        return
    try:
        price=float(input("item price: "))
        quantity=int(input("item quantity: "))
    except ValueError:
        print("Invalid input")
        return
    if name and price and quantity:
        items[name] = {'price': price, 'quantity': quantity}
    else:
        print("Invalid input, try again")

def remove_item():
    name=input("Choose the name of item you would like to delete")
    if name in items:
        del items[name]
    else:
        print("Item not found")
def update_quantity():
    name=input("Choose the name of item you would like to update")
    if name in items:
        quantity=input("Enter new quantity: ")
        items[name]['quantity']=quantity
    else:
        print("Item not found")

def view_cart():
    print("--- Cart summary ---")
    for name, info in items.items():
        print(f"Item: {name}, Price: {info['price']}, Quantity: {info['quantity']}")
    print("-------------------------")

def checkout():
    total=0
    for info in items.values():
        total+=int(info['price'])*int(info['quantity'])
    print(f"Total amount : {total}")
    if total > 1000:
        total = total * 0.9
        print("A 10% discount has been applied.")
        print(f"Amount to pay: {total} after discount.")

main_menu()

