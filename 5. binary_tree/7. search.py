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

    def height(self, root):
        if not root:
            return 0

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if lheight > rheight:
            return lheight + 1
        return rheight + 1

    def level_order(self):
        height = self.height(self.root)
        nodes_last = 2**(height - 1)
        queue = Queue(nodes_last)

        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            print(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
            return

        height = self.height(self.root)
        nodes_last = 2**(height - 1)
        queue = Queue(nodes_last)

        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            else:
                node.left = Node(data)
                break
            if node.right:
                queue.enqueue(node.right)
            else:
                node.right = Node(data)
                break

    def search(self, root, key):
        if root:
            if root.data == key:
                return root
            left = self.search(root.left, key)
            if left:
                return left
            right = self.search(root.right, key)
            return right

    def node_exists(self, root, key):
        if root:
            if root is None:
                return False
            if root.data == key:
                return True
            left = self.node_exists(root.left, key)
            if left:
                return True
            right = self.node_exists(root.right, key)
            return right
        return False


if __name__ == "__main__":
    tree = Tree()

    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)

    print(tree.search(tree.root, 3).data)
    print(tree.search(tree.root, 8))

    print(tree.node_exists(tree.root, 3))
    print(tree.node_exists(tree.root, 8))
