class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def insert_iter(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        ref = self.root
        while(ref):
            if ref.data == data:
                return
            if data > ref.data:
                if ref.right is None:
                    ref.right = node
                    return
                else:
                    ref = ref.right
            else:
                if ref.left is None:
                    ref.left = node
                    return
                else:
                    ref = ref.left

    def insert_rec(self, root, data):
        if root is None:
            root = Node(data)
            return
        if data == root.data:
            return
        if data > root.data:
            if root.right is None:
                root.right = Node(data)
                return
            else:
                self.insert_rec(root.right, data)
        else:
            if root.left is None:
                root.left = Node(data)
                return
            else:
                self.insert_rec(root.left, data)


if __name__ == "__main__":
    tree = Tree()

#            8
#        /       \
#       3          10
#     /   \         \
#    1     6         14
#         /  \      /
#        4    7    13

    tree.root = Node(8)
    tree.root.left = Node(3)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(4)
    tree.root.left.right.right = Node(7)
    tree.root.right = Node(10)
    tree.root.right.right = Node(14)
    tree.root.right.right.left = Node(13)

    tree.inorder(tree.root)  # Sorted numbers
    print("\n")

    tree.insert_iter(5)

    tree.inorder(tree.root)  # Sorted numbers
