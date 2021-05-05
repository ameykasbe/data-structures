class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        nn = Node(data)
        if self.front is None and self.rear is None:
            self.front = self.rear = nn
            print("Enqueued:", data)
            return
        self.rear.next = nn
        self.rear = nn
        print("Enqueued:", data)

    def dequeue(self):
        if self.is_empty():
            print("Queue empty.")
            exit(1)
        temp = self.front
        data = temp.data
        self.front = self.front.next
        temp = None

        if self.front is None:
            self.rear = None
        return data

    def print_queue(self):
        if self.is_empty():
            print("Printing queue: Queue empty.")
            exit(1)
        ref = self.front
        print("Printing queue: ", end=" ")
        while(ref is not None):
            print(ref.data, end=" ")
            ref = ref.next


if __name__ == "__main__":
    q = Queue()
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
    print("Dequeued:", q.dequeue())
    # print("Dequeued:", q.dequeue()) # Queue empty
    # print("Dequeued:", q.dequeue()) # Queue empty
    # print("Dequeued:", q.dequeue()) # Queue empty

    q.print_queue()
