import logging

logging.basicConfig(level=logging.INFO)

def retry_request_with_logging(max_attempts, base_delay):
    for attempt in range(max_attempts):
        try:
            result = perform_network_request()
            logging.info(f"Successful request on attempt {attempt + 1}: {result}")
            return
        except Exception as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                delay = base_delay * (2 ** attempt)
                logging.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
    logging.error("All attempts failed.")

# Example usage
retry_request_with_logging(max_attempts=5, base_delay=1)
