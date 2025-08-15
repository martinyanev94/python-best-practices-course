import threading
import time
import queue

def producer(q):
    for i in range(5):
        item = f"item-{i}"
        q.put(item)
        print(f"Produced: {item}")
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Sentinel to stop the consumer
            break
        print(f"Consumed: {item}")
        time.sleep(2)

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Stopping the consumer
consumer_thread.join()
