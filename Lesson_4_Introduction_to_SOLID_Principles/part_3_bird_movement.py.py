class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        print("I can't fly")

def make_bird_fly(bird):
    bird.fly()
class Bird:
    def move(self):
        print("I'm moving")

class FlyingBird(Bird):
    def move(self):
        print("I'm flying")

class FlightlessBird(Bird):
    def move(self):
        print("I'm walking")

def make_bird_move(bird):
    bird.move()

if __name__ == "__main__":
    make_bird_move(FlyingBird())
    make_bird_move(FlightlessBird())
