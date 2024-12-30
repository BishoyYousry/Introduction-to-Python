class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return self.quantity
        else:
            print(f"Not enough stock for {self.name}")
            return self.quantity

    def restock(self, quantity):
        self.quantity += quantity
        return self.quantity

    def disply_info(self):
        print(f"Product name is {self.name}, the amount available is {self.quantity}, and its price is {self.price}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"{name} product is added to the inventory.")

    def get_total_val(self):
        total_value = 0
        for product in self.products:
            total_value += product.get_price() * product.quantity  # Get the total value of inventory
        return total_value

    def display_inventory(self):
        for product in self.products:
            product.disply_info()


inventory = Inventory()

inventory.add_product("Dell G3", 15000, 3)
inventory.add_product("Dell G5", 22000, 3)


print(f"Total inventory value: {inventory.get_total_val()}")

inventory.display_inventory()


product1 = inventory.products[0] 
product1.sell(1)


product2 = inventory.products[1] 
product2.restock(2) 

inventory.display_inventory()
