import reactivex as rx
from reactivex import operators as ops

def observe():
    source = rx.interval(1).pipe(ops.map(lambda x: f"Update: {x}"))
    source.subscribe(lambda value: print(value))

if __name__ == "__main__":
    observe()
