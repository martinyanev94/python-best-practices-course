class VendingMachine:
    def __init__(self):
        self.state = WaitingForSelection()

    def change_state(self, state):
        self.state = state

    def select_item(self, item):
        self.state.select_item(item)

    def dispense(self):
        self.state.dispense()
class WaitingForSelection(State):
    def select_item(self, item):
        print(f"Item {item} has been selected.")
        return Dispensing()

class Dispensing(State):
    def dispense(self):
        print("Dispensing your item... Enjoy!")
        return WaitingForSelection()
