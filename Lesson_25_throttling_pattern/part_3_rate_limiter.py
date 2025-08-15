import time
from collections import deque

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = deque()

    def allow_request(self, request_time: float) -> bool:
        # Remove requests that are outside the time window
        while self.requests and self.requests[0] <= request_time - self.time_window:
            self.requests.popleft()

        # Allow the request if we have not yet hit the limit
        if len(self.requests) < self.max_requests:
            self.requests.append(request_time)
            return True
        return False

# Example usage
limiter = RateLimiter(max_requests=5, time_window=10)  # 5 requests allowed every 10 seconds
for i in range(10):
    if limiter.allow_request(time.time()):
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(1)  # Simulating a wait time between requests
