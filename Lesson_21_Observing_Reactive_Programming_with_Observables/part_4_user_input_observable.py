import rx
from rx import operators as ops
import time
import threading

# Simulating a user input stream
def user_input_stream(observer):
    for i in range(1, 6):
        time.sleep(1)  # Simulate delay between inputs
        observer.on_next(f"User input: {i}")
    observer.on_completed()

# Creating an observable from the user input stream
observable = rx.create(user_input_stream)

observable.subscribe(
    on_next=lambda value: print(f"Received: {value}"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Done processing user inputs!")
)
