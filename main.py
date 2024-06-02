import input as inp
import inventory as inv
import product as pr

def main():
    inv_manager = inv.InventoryManager()

    while True:
        print("\n1. Products List")
        print("2. Add Product")
        print("3. Save Inventory")
        print("4. Load Inventory")
        
        print("5. Remove Product")
        print("6. Exit\n")

        num = inp.get_input("Enter a number: ", "int")
        

        if num == 1:
            inv_manager.products_list()

        elif num == 2:
            name = input("Enter product name: ")
            quantity = inp.get_input("Enter product quantity: ", "int")  
            price = inp.get_input("Enter product price: ", "float")
            product = pr.Product(name, quantity, price)
            inv_manager.add_product(product)

        elif num == 3:
            #filename = "inventory.txt"
            filename = input("Enter filename: ")
            inv_manager.save_inventory(filename)

        elif num == 4:
            #filename = "inventory.txt"
            filename = input("Enter filename: ")
            inv_manager.load_inventory(filename)
        
        elif num == 5:
            name = input("Enter product name to remove: ")
            quantity = inp.get_input("Enter quantity to remove: ", "int")
            inv_manager.remove_product(name, quantity)

        elif num == 6:
            print("Closing the program...")
            break
        else:
            print("Please try again")


if __name__ == "__main__":
    main()
