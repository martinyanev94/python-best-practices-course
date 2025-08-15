cache = {}

def expensive_function(n):
    if n in cache:
        print(f"Fetching from cache for: {n}")
        return cache[n]
    
    # Simulating an expensive computation
    time.sleep(2)
    result = n * n
    cache[n] = result
    print(f"Computed and cached for: {n}")
    return result

# Usage
print(expensive_function(4))  # This will take time to compute
print(expensive_function(4))  # This will fetch from cache immediately
print(expensive_function(5))  # This will take time to compute
