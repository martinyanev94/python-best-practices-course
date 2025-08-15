class State:
    def handle(self):
        pass


class Standing(State):
    def handle(self):
        print("The character is standing.")


class Running(State):
    def handle(self):
        print("The character is running.")


class Jumping(State):
    def handle(self):
        print("The character is jumping.")


class Character:
    def __init__(self):
        self.state = Standing()

    def set_state(self, state):
        self.state = state

    def perform_action(self):
        self.state.handle()


# Using the State pattern
character = Character()

character.perform_action()  # Standing
character.set_state(Running())
character.perform_action()  # Running
character.set_state(Jumping())
character.perform_action()  # Jumping
