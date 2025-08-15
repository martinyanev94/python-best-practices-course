class InventoryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, name, quantity):
        new_item = Item(name, quantity)
        self.model.append(new_item)
        self.view.display_item(new_item)

    def update_item(self, name, amount):
        for item in self.model:
            if item.name == name:
                item.update_quantity(amount)
                self.view.display_item(item)
                return
        self.view.show_message("Item not found.")
