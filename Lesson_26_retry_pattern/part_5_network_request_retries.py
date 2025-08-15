class TransientError(Exception):
    pass

class PermanentError(Exception):
    pass

def perform_network_request_v2():
    if random.random() < 0.7:  # 70% chance to fail
        if random.random() < 0.5:
            raise TransientError("Temporary network issue")
        else:
            raise PermanentError("Invalid request")
    return "Success"

def retry_request_with_error_handling(max_attempts, base_delay):
    for attempt in range(max_attempts):
        try:
            result = perform_network_request_v2()
            print(result)
            return
        except TransientError as e:
            print(f"Attempt {attempt + 1} failed with transient error: {e}")
            if attempt < max_attempts - 1:
                delay = base_delay * (2 ** attempt)
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
        except PermanentError as e:
            print(f"Attempt {attempt + 1} failed with permanent error: {e}")
            break
    print("All attempts complete.")

# Example usage
retry_request_with_error_handling(max_attempts=5, base_delay=1)
