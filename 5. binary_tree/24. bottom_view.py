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

    def add_hash_table(self, root, hd, level, hash_table):
        if root:
            if hd not in hash_table:
                hash_table[hd] = [root.data, level]
            elif level > hash_table[hd][1]:
                hash_table[hd] = [root.data, level]

            self.add_hash_table(root.left, hd-1, level+1, hash_table)
            self.add_hash_table(root.right, hd+1, level+1, hash_table)

    def bottom_view(self):
        hash_table = dict()
        self.add_hash_table(self.root, 0, 0, hash_table)
        minimum = min(hash_table)
        maximum = max(hash_table)
        for i in range(minimum, maximum+1):
            print(hash_table[i][0], end=" ")


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

    tree.bottom_view()
    print("")
    # Bottom view of the above binary tree is
    # 4 2 6 8 7 9

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
    tree.bottom_view()
    # Bottom view of the above binary tree is
    # 2 4 5 6
    print("")

    tree = Tree()
    tree.root = Node(20)
    tree.root.left = Node(8)
    tree.root.right = Node(22)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(25)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(14)

    '''
            20
          /    \
        8       22
       /   \      \
     5      3      25
           / \      
         10    14
    '''
    tree.bottom_view()
    # 5 10 4 14 25
