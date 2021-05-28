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

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def height(self, root):
        if root is None:
            return 0

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if lheight > rheight:
            return lheight + 1
        return rheight + 1

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

    def delete(self, key):
        if self.root.data == key and self.root.left is None and self.root.right is None:
            self.root = None
            return
        key_node = None
        queue = Queue(20)

        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            if node.data == key:
                key_node = node

            if node.left:
                parent = node
                queue.enqueue(node.left)

            if node.right:
                parent = node
                queue.enqueue(node.right)

        if key_node is None:
            print("Node not found")
            return

        key_node.data = node.data
        if parent.right:
            parent.right = None
        else:
            parent.left = None

    def breadth_first_search(self, key):
        if self.root.data == key:
            return True
        queue = Queue(20)
        queue.enqueue(self.root)

        while(not queue.is_empty()):
            node = queue.dequeue()
            if node.data == key:
                return True

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

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

    print(tree.breadth_first_search(10))
    print(tree.breadth_first_search(20))
    print(tree.breadth_first_search(30))
    print(tree.breadth_first_search(40))
    print(tree.breadth_first_search(50))
    print(tree.breadth_first_search(60))
    print(tree.breadth_first_search(70))
    print(tree.breadth_first_search(80))
