class Component:
    def operation(self):
        raise NotImplementedError

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return "Composite with: " + ", ".join(results)

# Example usage
composite = Composite()
leaf1 = Leaf()
leaf2 = Leaf()

composite.add(leaf1)
composite.add(leaf2)

print(composite.operation())
