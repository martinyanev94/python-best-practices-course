import time

class TokenBucket:
    def __init__(self, capacity: int, fill_rate: int):
        self.capacity = capacity
        self.fill_rate = fill_rate
        self.tokens = capacity
        self.last_check = time.time()

    def add_tokens(self):
        now = time.time()
        elapsed = now - self.last_check
        added_tokens = elapsed * self.fill_rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_check = now

    def allow_request(self) -> bool:
        self.add_tokens()
        if self.tokens > 0:
            self.tokens -= 1
            return True
        return False

# Example usage
bucket = TokenBucket(capacity=10, fill_rate=1)  # 10 tokens max, 1 token per second refill

for i in range(15):
    if bucket.allow_request():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(1)  # Simulating a wait time between requests
