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

    def search_iter(self, key):
        if self.root is None:
            print("Tree empty.")
            return

        ref = self.root
        while(ref):
            if ref.data == key:
                print("Found.")
                return
            if key > ref.data:
                ref = ref.right
            else:
                ref = ref.left
        print("Key not found.")

    def search_rec(self, key, root):
        if root is None:
            print("Key not found.")
            return
        if root.data == key:
            print("found")
            return
        if key > root.data:
            self.search_rec(key, root.right)
        else:
            self.search_rec(key, root.left)


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

    # tree.inorder(tree.root)  # Sorted numbers

    tree.search_iter(8)
