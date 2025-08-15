from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(arg):
    # Time-consuming function logic here
    return result
