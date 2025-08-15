import time
import random

def perform_network_request():
    # Simulating a network request that has a chance of failing
    if random.random() < 0.7:  # 70% chance to fail
        raise Exception("Network error")
    return "Success"

def retry_request(max_attempts, base_delay):
    for attempt in range(max_attempts):
        try:
            result = perform_network_request()
            print(result)
            return
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:  # Avoid sleeping on the last try
                delay = base_delay * (2 ** attempt)  # Exponential backoff
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
    print("All attempts failed.")

# Example usage
retry_request(max_attempts=5, base_delay=1)  # 5 attempts, starting with a delay of 1 second
