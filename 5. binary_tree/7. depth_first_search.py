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

    def depth_first_search(self, key, root):
        if root:
            if root.data == key:
                return True
            l = self.depth_first_search(key, root.left)
            if l:
                return True
            r = self.depth_first_search(key, root.right)
            return r
        return False


if __name__ == "__main__":
    tree = Tree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    tree.insert(70)

    print(tree.depth_first_search(10, tree.root))
    print(tree.depth_first_search(20, tree.root))
    print(tree.depth_first_search(30, tree.root))
    print(tree.depth_first_search(40, tree.root))
    print(tree.depth_first_search(50, tree.root))
    print(tree.depth_first_search(60, tree.root))
    print(tree.depth_first_search(70, tree.root))
    print(tree.depth_first_search(80, tree.root))
