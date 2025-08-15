import rx
from rx import operators as ops

# Create an observable that emits data
observable = rx.from_([1, 2, 3, 4, 5])

# Transform emitted values with `map`
observable.pipe(
    ops.map(lambda x: x * 10)
).subscribe(
    on_next=lambda value: print(f"Transformed value: {value}"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Done transforming values!")
)
