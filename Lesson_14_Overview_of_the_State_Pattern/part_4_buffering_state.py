class Buffering(State):
    def play(self):
        print("Buffering... Please wait...")
        return Playing()  # Transition back to playing when done

    def pause(self):
        print("Can't pause. Music is buffering!")

    def stop(self):
        print("Stopping the buffering...")
        return Stopped()
