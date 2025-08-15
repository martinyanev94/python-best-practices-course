class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_time):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.failure_count = 0
        self.last_failure_time = 0

    def call_service(self, function, *args, **kwargs):
        if self.failure_count >= self.failure_threshold:
            if time.time() - self.last_failure_time > self.recovery_time:
                self.failure_count = 0
            else:
                raise Exception("Circuit is open. Try again later.")
        
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as e:
            self.last_failure_time = time.time()
            self.failure_count += 1
            raise e
