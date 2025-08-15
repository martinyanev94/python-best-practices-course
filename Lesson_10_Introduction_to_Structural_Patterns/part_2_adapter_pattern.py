class OldSystem:
    def existing_method(self):
        return "Data from the old system"

class NewSystem:
    def new_method(self):
        return "Data from the new system"

class Adapter:
    def __init__(self, new_system):
        self.new_system = new_system

    def existing_method(self):
        return self.new_system.new_method()

# Usage
old_system = OldSystem()
new_system = NewSystem()
adapter = Adapter(new_system)

print(old_system.existing_method())
print(adapter.existing_method())
