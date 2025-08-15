class Vehicle:
    def __init__(self):
        self.type = None
        self.engine = None
        self.color = None
        self.wheels = None

    def __str__(self):
        return f"Vehicle {self.type} with {self.engine}, color: {self.color}, wheels: {self.wheels}."


class VehicleBuilder:
    def __init__(self, vehicle_type):
        self.vehicle = Vehicle()
        self.vehicle.type = vehicle_type

    def add_engine(self, engine):
        self.vehicle.engine = engine
        return self

    def add_color(self, color):
        self.vehicle.color = color
        return self

    def add_wheels(self, wheels):
        self.vehicle.wheels = wheels
        return self

    def build(self):
        return self.vehicle


# Client code
car_builder = VehicleBuilder("Car")
my_car = (car_builder
          .add_engine("V6")
          .add_color("Red")
          .add_wheels(4)
          .build())

print(my_car)

truck_builder = VehicleBuilder("Truck")
my_truck = (truck_builder
            .add_engine("V8")
            .add_color("Blue")
            .add_wheels(6)
            .build())

print(my_truck)
