import product as pr

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    #inventory-shi arsebuli produqtebis dabechdva
    def products_list(self):
        if not self.inventory:
            print("Inventory is empty")
        else:
            for name, product in self.inventory.items():
                print(f"Name: {name}, Quantity: {product.quantity}, Price: {product.price}")

    #produqtis damateba
    def add_product(self, product):
        if product.name in self.inventory:
            self.inventory[product.name].quantity += product.quantity
        else:
            self.inventory[product.name] = product

    #inventory-s txt failad shenaxva
    def save_inventory(self, filename):
        try:
            with open(filename, 'w') as f:
                for product in self.inventory.values():
                    f.write(product.to_string())
            print("Inventory saved successfully")
        except Exception as e:
            print(f"Error while saving inventory: {e}")

    #inventory-s txt failis chatvirtva
    def load_inventory(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    name, quantity, price = line.strip().split(',')
                    self.add_product(pr.Product(name, int(quantity), float(price)))
            print("Inventory loaded successfully")
        except FileNotFoundError:
            print("Inventory file not found")
        except Exception as e:
            print(f"Error while loading inventory: {e}")

    #produqtis washla inventory-dan
    def remove_product(self, name, quantity):
        if name in self.inventory:
            if self.inventory[name].quantity >= quantity:
                self.inventory[name].quantity -= quantity
                if self.inventory[name].quantity == 0:
                    del self.inventory[name]
                print(f"{quantity} {name} removed from inventory")
            else:
                print("There is less " + name)
        else:
            print("Product not found :(")