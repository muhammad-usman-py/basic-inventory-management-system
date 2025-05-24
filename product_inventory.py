
class product:
    def __init__(self, sku, name, price, quantity):
        self.P_id = sku
        self.name = name
        self.price = price
        self.quantity = quantity


class inventory:
    def __init__(self):
        self.items = {}

    def add_product(self):
        sku = (input("Enter the SKU of product:\n"))
        if sku in self.items:
            print(f"SKU {sku} already exists. Try updating instead.")
            return

        name = input("Enter the name of product:\n")
        while True:
            price = float(input("Enter the price of product:\n"))
            quantity = int(input("Enter the quantity of product:\n"))
            if quantity < 0:
                print("Quantity cannot be negative")
            elif price < 0:
                print("Price cannot be negative")
            else:
                break
        pdc = product(sku, name, price, quantity)
        self.items[sku] = (pdc)
        print(f"Added: {sku} → {pdc.__dict__}")

    def remove_product(self):
        sku = (input("Enter the SKU of product to remove:\n"))
        if sku in self.items:
            del self.items[sku]
            print(f"Removed: {sku}")
        else:
            print(f"Product {sku} not found in inventory.")

    def update_stock(self):
        sku = input("Enter the SKU of product:\n")
        if sku in self.items:
            new_qty = int(input("Enter new quantity of this product:\n"))
            self.items[sku].quantity = new_qty
            print(f"Updated: {sku} → new quantity: {new_qty}")

        else:
            print(f"Product {sku} not found in inventory.")

    def get_product(self):
        # Read SKU as a string, not int:
        sku = input("Enter the SKU of product:\n").strip()

        if sku in self.items:
            prod = self.items[sku]
            # Print out the attributes of the product instance:
            print(f"Product Found → SKU: {sku} | Name: {prod.name} | Price: {prod.price} RS. | Quantity: {prod.quantity}")
        else:
            print(f"Product {sku} not found in inventory.")


    def list_all_items(self):
        for sku, prod in self.items.items():
            print(f"{sku} | {prod.name} | {prod.price} RS. | {prod.quantity}")


produc1 = inventory()
print("-"*40)


while True:
    while True:
        ch = input("Do you want to add product, yes/no?:\n").strip().lower()
        if ch == "yes":
            produc1.add_product()
        else:
            print("Product added successfully ")
            break

    print("1.Remove product")
    print("2.Update stock")
    print("3.Get product")
    print("4.List all items")
    print("5.Not intereseted wana Exit ?")
    print("-"*40)
    choice = input("Enter your choice:\n").strip()
    if choice == "1":
        produc1.remove_product()
    elif choice == "2":
        produc1.update_stock()
    elif choice == "3":
        produc1.get_product()
    elif choice == "4":
        produc1.list_all_items()
    elif choice == "5":
        print("Thanks for using the inventory system!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

    again = input("Do you want to manage inventory again ? (yes/no):\n ")
    if again.lower() != "yes":
        print("Thanks for using the inventory system!")
        break
