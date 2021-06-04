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


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def level_order(self):
        if self.root is None:
            return
        queue = Queue(20)
        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            print(node.data, end=" ")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = Queue(20)
        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            else:
                node.left = new_node
                break

            if node.right:
                queue.enqueue(node.right)
            else:
                node.right = new_node
                break

    def right_view(self):
        if self.root is None:
            return
        queue = Queue(20)
        queue.enqueue(self.root)
        while(not queue.is_empty()):
            print(queue.queue[queue.rear].data, end=" ")

            for i in range(queue.size):
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)


if __name__ == "__main__":
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.root.right.right.left = Node(8)
    tree.root.right.right.right = Node(9)
    '''
          1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 
    '''

    tree.right_view()
    print("")
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.root.left.right = Node(4)
    tree.root.left.right.right = Node(5)
    tree.root.left.right.right.right = Node(6)
    '''
        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6
    '''
    tree.right_view()
