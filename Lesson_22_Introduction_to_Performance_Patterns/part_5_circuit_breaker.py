class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_timeout):
        self.failure_threshold = failure_threshold
        self.failure_count = 0
        self.state = 'CLOSED'
        self.recovery_timeout = recovery_timeout
        self.last_failure_time = None

    def call_service(self, service_function):
        if self.state == 'OPEN':
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = 'CLOSED'
                self.failure_count = 0
            else:
                print("Circuit is open: Service will not be called.")
                return

        try:
            result = service_function()
            self.failure_count = 0  # Reset after successful call
            print("Service call succeeded:", result)
        except Exception as e:
            self.failure_count += 1
            print(f"Service call failed: {e}")
            if self.failure_count >= self.failure_threshold:
                self.state = 'OPEN'
                self.last_failure_time = time.time()

def unreliable_service():
    raise Exception("Service is down!")

cb = CircuitBreaker(failure_threshold=2, recovery_timeout=5)
for _ in range(5):
    cb.call_service(unreliable_service)
