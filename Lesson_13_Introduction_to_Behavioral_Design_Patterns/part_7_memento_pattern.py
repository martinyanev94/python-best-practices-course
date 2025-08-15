class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self):
        self.state = ""

    def set_state(self, state):
        self.state = state

    def save_state_to_memento(self):
        return Memento(self.state)

    def restore_state_from_memento(self, memento):
        self.state = memento.state


class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


# Using the Memento pattern
originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
caretaker.add_memento(originator.save_state_to_memento())

originator.set_state("State 2")
caretaker.add_memento(originator.save_state_to_memento())

originator.set_state("State 3")

# Restoring to State 1
restored_memento = caretaker.get_memento(0)
originator.restore_state_from_memento(restored_memento)
print(f"Restored State: {originator.state}")
