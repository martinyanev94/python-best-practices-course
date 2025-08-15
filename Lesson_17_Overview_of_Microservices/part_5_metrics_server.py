from prometheus_client import start_http_server, Summary

# Start the HTTP server to expose metrics
start_http_server(8000)

# Create a metric to track response time
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request():
    # Simulate request processing logic
    time.sleep(1)

while True:
    process_request()
