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

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

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

    def height(self, root, diameter):
        if root is None:
            return 0
        lheight = self.height(root.left, diameter)
        rheight = self.height(root.right, diameter)
        if lheight + rheight + 1 > diameter.diameter:
            diameter.diameter = lheight + rheight + 1
        if lheight > rheight:
            return lheight + 1
        return rheight + 1


class Diameter:
    def __init__(self):
        self.diameter = 0


if __name__ == "__main__":
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    diameter = Diameter()
    print(tree.height(tree.root, diameter))
    print("Diameter = ", diameter.diameter)
