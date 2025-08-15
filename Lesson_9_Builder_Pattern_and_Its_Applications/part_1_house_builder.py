class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls}, {self.roof}, {self.windows}, and {self.doors}."


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_walls(self, walls):
        self.house.walls = walls
        return self

    def add_roof(self, roof):
        self.house.roof = roof
        return self

    def add_windows(self, windows):
        self.house.windows = windows
        return self

    def add_doors(self, doors):
        self.house.doors = doors
        return self

    def build(self):
        return self.house


# Client code
builder = HouseBuilder()
my_house = (builder
            .add_walls("Brick Walls")
            .add_roof("Gable Roof")
            .add_windows("Double Glazed Windows")
            .add_doors("Front Door")
            .build())

print(my_house)
