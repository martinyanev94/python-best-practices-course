class MusicPlayer:
    def __init__(self):
        self.state = Stopped()  # Initial state

    def change_state(self, state):
        self.state = state

    def play(self):
        new_state = self.state.play()
        if new_state:
            self.change_state(new_state)

    def pause(self):
        new_state = self.state.pause()
        if new_state:
            self.change_state(new_state)

    def stop(self):
        new_state = self.state.stop()
        if new_state:
            self.change_state(new_state)
