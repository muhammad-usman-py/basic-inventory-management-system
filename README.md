# 🏬 Inventory Management System

A simple Python program that allows users to manage products in an inventory. It supports adding new products, removing existing ones, updating stock quantities, retrieving product details, and listing all items. The system uses two classes (`Product` and `Inventory`) to encapsulate data and behavior.

---

## ✨ Features

- ➕ **Add Product**  
  - Enter SKU, name, price, and quantity  
  - Prevents duplicate SKUs  
  - Validates that price and quantity are non-negative  
- ➖ **Remove Product**  
  - Delete a product by SKU if it exists  
- 🔄 **Update Stock**  
  - Change the quantity of an existing product  
- 🔍 **Get Product**  
  - Retrieve and display details (name, price, quantity) by SKU  
- 📋 **List All Items**  
  - Display every product’s SKU, name, price, and quantity  
- 🚪 **Exit**  
  - Cleanly exit the program when finished  

---

## 🧾 Code Overview

```python
class product:
    def __init__(self, sku, name, price, quantity):
        self.P_id = sku
        self.name = name
        self.price = price
        self.quantity = quantity


class inventory:
    def __init__(self):
        # Dictionary to store products (key = SKU, value = product instance)
        self.items = {}

    def add_product(self):
        sku = input("Enter the SKU of product:\n")
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
        self.items[sku] = pdc
        print(f"Added: {sku} → {pdc.__dict__}")

    def remove_product(self):
        sku = input("Enter the SKU of product to remove:\n")
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
        sku = input("Enter the SKU of product:\n").strip()
        if sku in self.items:
            prod = self.items[sku]
            print(
                f"Product Found → SKU: {sku} | Name: {prod.name} | "
                f"Price: {prod.price} RS. | Quantity: {prod.quantity}"
            )
        else:
            print(f"Product {sku} not found in inventory.")

    def list_all_items(self):
        for sku, prod in self.items.items():
            print(f"{sku} | {prod.name} | {prod.price} RS. | {prod.quantity}")
```

---

## 🚀 Usage

1. ▶️ **Run the program** in a terminal or command prompt:  
   ```bash
   python your_script_name.py
   ```
2. 🔧 **Add Products Phase**  
   - The program will repeatedly ask:  
     ```
     Do you want to add product, yes/no?:
     ```  
   - Enter **yes** to add a product (input SKU, name, price, quantity).  
   - Enter **no** (or anything else) to finish adding products and proceed to the main menu.

3. 🛠️ **Main Inventory Menu**  
   Choose one of the following options by entering its number:  
   ```
   1. Remove product
   2. Update stock
   3. Get product
   4. List all items
   5. Exit
   ```  
   - **Remove product**: Deletes a product by SKU.  
   - **Update stock**: Enters a new quantity for an existing product.  
   - **Get product**: Displays details of a single product by SKU.  
   - **List all items**: Shows every product in inventory.  
   - **Exit**: Closes the program.

4. 🔄 **Repeat or Exit**  
   - After performing an action, you’ll be asked:  
     ```
     Do you want to manage inventory again? (yes/no):
     ```  
   - Enter **yes** to return to the main menu.  
   - Enter **no** (or anything else) to exit completely.

---

## 📝 Notes

- 🔑 **SKU (String)**:  
  - Must be unique. Duplicate SKUs are not allowed and will display a warning.  
- 💲 **Price (Float)**:  
  - Must be non-negative. The input will be rejected until a valid value is entered.  
- 📦 **Quantity (Integer)**:  
  - Must be non-negative. The input will be rejected until a valid value is entered.  
- 📂 **Storage**:  
  - Products are stored in an in-memory dictionary (`self.items`) with key = SKU and value = `product` instance.  
  - Data is not persisted to disk—inventory resets when the program ends.  
- ❗ **Error Handling**:  
  - Attempts to remove, update, or get a non-existent SKU produce a “not found” message.  
  - Invalid menu selections prompt for a valid choice.  
- 🤖 **Extensibility**:  
  - You can easily add methods for saving/loading from a file, searching by name, or categorizing products.  
