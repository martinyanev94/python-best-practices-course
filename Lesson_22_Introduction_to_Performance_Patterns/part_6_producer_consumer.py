from queue import Queue
import threading
import time

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")
        time.sleep(2)  # Simulate a time-consuming task
        q.task_done()

queue = Queue()
threading.Thread(target=worker, daemon=True).start()

for item in range(5):
    print(f"Producing {item}")
    queue.put(item)

print("Waiting for all tasks to finish...")
queue.join()  # Wait until all items have been processed
print("All tasks finished.")
