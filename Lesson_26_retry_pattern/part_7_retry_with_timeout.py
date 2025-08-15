import time

def retry_with_timeout(max_attempts, base_delay, total_timeout):
    start_time = time.time()
    for attempt in range(max_attempts):
        if time.time() - start_time > total_timeout:
            print("Total timeout exceeded. Aborting retries.")
            return
        
        try:
            result = perform_network_request()
            print(result)
            return
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                delay = base_delay * (2 ** attempt)
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
    print("All attempts completed.")

# Example usage with a total timeout of 10 seconds
retry_with_timeout(max_attempts=5, base_delay=1, total_timeout=10)
