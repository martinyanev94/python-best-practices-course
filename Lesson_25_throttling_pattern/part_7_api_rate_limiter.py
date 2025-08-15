import requests
import time

class APIRateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.limiter = RateLimiter(max_requests, time_window)

    def request(self, url: str):
        while not self.limiter.allow_request(time.time()):
            print("Rate limit exceeded, waiting...")
            time.sleep(1)
        response = requests.get(url)
        return response.json()

# Example usage
api_limiter = APIRateLimiter(max_requests=3, time_window=5)  # 3 requests every 5 seconds

for i in range(10):
    response = api_limiter.request("https://jsonplaceholder.typicode.com/posts")
    print(response)
