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
    print("Preorder:", end=" ")
    tree.preorder(tree.root)  # 1 2 4 5 3

    print("Inorder:", end=" ")
    tree.inorder(tree.root)  # 4 2 5 1 3

    print("Postorder:", end=" ")
    tree.postorder(tree.root)  # 4 5 2 3 1
