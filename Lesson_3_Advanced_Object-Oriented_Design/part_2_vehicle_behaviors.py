class DriveBehavior:
    def drive(self):
        return "Driving on the road"

class FlyBehavior:
    def fly(self):
        return "Flying in the sky"

class Car:
    def __init__(self):
        self.behavior = DriveBehavior()

    def perform_drive(self):
        return self.behavior.drive()

class Airplane:
    def __init__(self):
        self.behavior = FlyBehavior()

    def perform_fly(self):
        return self.behavior.fly()

car = Car()
print(car.perform_drive())

airplane = Airplane()
print(airplane.perform_fly())
