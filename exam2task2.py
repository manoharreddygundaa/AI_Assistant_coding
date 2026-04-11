from collections import deque
# PrintJob holds job id, student name, and number of pages
class PrintJob:
    def __init__(self, job_id: int, student_name: str, pages: int):
        self.job_id = job_id
        self.student_name = student_name
        self.pages = pages
    def __repr__(self):
        return f"PrintJob(id={self.job_id}, student={self.student_name}, pages={self.pages})"
class PrintQueue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, job: PrintJob):
        self.queue.append(job)
        print(f"Enqueued: {job}")
    def dequeue(self):
        if not self.queue:
            print("Queue is empty. No job to process.")
            return None
        job = self.queue.popleft()
        print(f"Dequeued and processing: {job}")
        return job
    def display(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print("Current queue (front -> rear):")
        for job in self.queue:
            print(f"  {job}")
def main():
    pq = PrintQueue()
    # Add at least 5 print jobs
    jobs = [
        PrintJob(1, "Alice", 12),
        PrintJob(2, "Bob", 5),
        PrintJob(3, "Carol", 8),
        PrintJob(4, "David", 20),
        PrintJob(5, "Eva", 3),
    ]
    for job in jobs:
        pq.enqueue(job)
    print("\nInitial queue state:")
    pq.display()
    # Process jobs one by one
    print("\nProcessing jobs in FIFO order:")
    while True:
        job = pq.dequeue()
        if job is None:
            break
        print("Queue state after dequeue:")
        pq.display()
        print()
if __name__ == "__main__":
    main()
