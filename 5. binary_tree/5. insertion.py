class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


class Tree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if not root:
            return 0

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if lheight > rheight:
            return lheight + 1
        return rheight + 1

    def level_order_traversal(self):
        height = self.height(self.root)
        max_nodes = 2**height - 1
        queue = Queue(max_nodes)

        if self.root is None:
            return

        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            print(node.data)

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def insertion(self, data):
        height = self.height(self.root)
        max_nodes = 2**height - 1
        queue = Queue(max_nodes)

        nn = Node(data)

        if self.root is None:
            self.root = nn
            return

        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            else:
                node.left = nn
                break
            if node.right:
                queue.enqueue(node.right)
            else:
                node.right = nn
                break


if __name__ == "__main__":
    tree = Tree()
    tree.insertion(1)
    tree.insertion(2)
    tree.insertion(3)
    tree.insertion(4)
    tree.insertion(5)
    tree.level_order_traversal()

#            1
#        /       \
#       2          3
#     /   \
#    4    5
