class Flyweight:
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        return f"Intrinsic State: {self.intrinsic_state}, Extrinsic State: {extrinsic_state}"

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, intrinsic_state):
        if intrinsic_state not in self.flyweights:
            self.flyweights[intrinsic_state] = Flyweight(intrinsic_state)
        return self.flyweights[intrinsic_state]

# Usage
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("Shared State A")
flyweight2 = factory.get_flyweight("Shared State A")

print(flyweight1.operation("Unique State 1"))
print(flyweight2.operation("Unique State 2"))
