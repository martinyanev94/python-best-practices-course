from concurrent.futures import ThreadPoolExecutor, as_completed

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(square, i) for i in range(1, 4)]
    
    for future in as_completed(futures):
        print(f"Result: {future.result()}")
