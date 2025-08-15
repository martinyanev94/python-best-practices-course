import concurrent.futures
import random
import time

def service_call(service_id):
    delay = random.uniform(0.1, 1.5)
    time.sleep(delay)
    return f"Service {service_id} finished in {delay:.2f} seconds"

def bulkhead_pattern():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(service_call, i): i for i in range(5)}
        for future in concurrent.futures.as_completed(futures):
            service_id = futures[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Service {service_id} failed with exception: {e}")

bulkhead_pattern()
