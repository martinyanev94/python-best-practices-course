import rx
from rx import operators as ops
import time

# Observable emitting values
observable = rx.from_([1, 2, 3, 4, 5])

# Use a new thread to handle emissions
observable.subscribe_on(rx.scheduler.NewThreadScheduler()).subscribe(
    on_next=lambda value: print(f"Received on new thread: {value}"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Done emitting values on new thread!")
)

time.sleep(2)  # Keep the main thread alive for a moment
