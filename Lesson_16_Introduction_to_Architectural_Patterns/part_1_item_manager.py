class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.name}: {self.quantity}"
