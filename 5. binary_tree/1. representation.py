class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)

#            1
#        /       \
#       2          3
#     /   \       /  \
#    4    None  None  None
#   /  \
# None None
