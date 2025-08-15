class State:
    def play(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

class Playing(State):
    def play(self):
        print("Already playing! Enjoy the music.")

    def pause(self):
        print("Pausing the music...")
        return Paused()

    def stop(self):
        print("Stopping the music...")
        return Stopped()

class Paused(State):
    def play(self):
        print("Resuming the music...")
        return Playing()

    def pause(self):
        print("Already paused!")

    def stop(self):
        print("Stopping the music...")
        return Stopped()

class Stopped(State):
    def play(self):
        print("Starting the music...")
        return Playing()

    def pause(self):
        print("Can't pause. The music is stopped!")

    def stop(self):
        print("Already stopped!")
