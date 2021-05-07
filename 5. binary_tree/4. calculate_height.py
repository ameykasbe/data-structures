class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

#            1
#        /       \
#       2          3
#     /   \
#    4    5

    print(tree.height(tree.root))
