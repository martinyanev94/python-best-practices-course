import rx
from rx import operators as ops

# Create an observable that emits data
observable = rx.from_([1, 2, 3, 4, 5])

# Subscribe to the observable
observable.subscribe(
    on_next=lambda value: print(f"Received: {value}"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Done emitting values!")
)
