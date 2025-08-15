class ImmutableVehicle:
    def __init__(self, vehicle_type, engine, color, wheels):
        self._vehicle_type = vehicle_type
        self._engine = engine
        self._color = color
        self._wheels = wheels

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @property
    def engine(self):
        return self._engine

    @property
    def color(self):
        return self._color

    @property
    def wheels(self):
        return self._wheels

    def __str__(self):
        return f"Immutable Vehicle {self.vehicle_type} with engine {self.engine}, color: {self.color}, wheels: {self.wheels}."


class ImmutableVehicleBuilder:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.engine = None
        self.color = None
        self.wheels = None

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_wheels(self, wheels):
        self.wheels = wheels
        return self

    def build(self):
        return ImmutableVehicle(self.vehicle_type, self.engine, self.color, self.wheels)


# Client code
immutable_car_builder = ImmutableVehicleBuilder("Car")
immutable_car = (immutable_car_builder
                 .set_engine("V6")
                 .set_color("Black")
                 .set_wheels(4)
                 .build())

print(immutable_car)
