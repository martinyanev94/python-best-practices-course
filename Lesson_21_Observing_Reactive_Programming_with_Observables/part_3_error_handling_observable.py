import rx
from rx import operators as ops

# Create an observable that emits data and raises an error
def raise_error():
    raise ValueError("Something went wrong!")

observable = rx.from_([1, 2, 3]).pipe(
    ops.concat(rx.just(raise_error()))
)

# Catch the error and provide a fallback observable
observable.pipe(
    ops.catch(lambda e: rx.of("Recovered from error: " + str(e)))
).subscribe(
    on_next=lambda value: print(f"Received: {value}"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Done processing values!")
)
