class Projector:
    def on(self):
        return "Projector is ON."

class Screen:
    def down(self):
        return "Screen is down."

class Amplifier:
    def on(self):
        return "Amplifier is ON."

class HomeTheaterFacade:
    def __init__(self, projector: Projector, screen: Screen, amplifier: Amplifier):
        self.projector = projector
        self.screen = screen
        self.amplifier = amplifier

    def watch_movie(self):
        print(self.amplifier.on())
        print(self.projector.on())
        print(self.screen.down())
        print("You are now watching a movie!")
projector = Projector()
screen = Screen()
amplifier = Amplifier()
home_theater = HomeTheaterFacade(projector, screen, amplifier)

home_theater.watch_movie()
