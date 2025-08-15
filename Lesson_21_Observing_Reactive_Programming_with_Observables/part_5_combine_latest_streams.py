import rx
from rx import operators as ops
import time
import random

# Simulating two observable data streams
obs1 = rx.interval(1).pipe(ops.map(lambda x: f"Stream 1: {x}"))
obs2 = rx.interval(1.5).pipe(ops.map(lambda x: f"Stream 2: {random.randint(1, 100)}"))

# Combining the latest values from both streams
combined = rx.combine_latest(obs1, obs2)

combined.subscribe(
    on_next=lambda value: print(f"Combined output: {value}"),
    on_error=lambda e: print(f"Error: {e}"),
    on_completed=lambda: print("Done combining streams!")
)

# Keep the program running to observe outputs
time.sleep(10)
