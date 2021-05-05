class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = capacity - 1
        self.size = 0  # Actual size = Number of elements present
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue full.")
            exit(1)
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        print("Enqueued:", data)

    def dequeue(self):
        if self.is_empty():
            print("Empty queue.")
            exit(1)
        temp = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return temp

    def print_queue(self):
        temp = self.front
        for i in range(self.size):
            print(self.queue[temp + i], end=" ")


if __name__ == "__main__":
    q = Queue(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    # q.enqueue(60) # Queue overflow
    # q.print_queue() # Print Queue
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())
    # print("Dequeued:", q.dequeue()) # Queue empty
    # print("Dequeued:", q.dequeue()) # Queue empty
    # print("Dequeued:", q.dequeue()) # Queue empty

    q.print_queue()
