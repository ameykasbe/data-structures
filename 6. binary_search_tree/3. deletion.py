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

    def search(self, key):
        if self.root is None:
            return None, None

        ref = self.root
        parent = None
        while(ref):
            if ref.data == key:
                print("Found=", ref.data)
                return ref, parent
            if key > ref.data:
                parent = ref
                ref = ref.right
            else:
                parent = ref
                ref = ref.left
        return None, None

    def min_value_node(self, node):
        # Requirement - At least one node to the right.
        parent = self.root
        ref = self.root.right
        while(ref.left):
            parent = ref
            ref = ref.left
        return ref, parent

    def delete_leaf(self, node, parent):
        # If node has one child or no child
        if node.right is None:
            if parent.right is node:
                parent.right = node.left
            else:
                parent.left = node.left
            return

        if node.left is None:
            if parent.right is node:
                parent.right = node.right
            else:
                parent.left = node.right
            return

    def deletion_iter(self, data):
        if self.root is None:
            print("Tree is empty.")
            return

        node, parent = self.search(data)

        # Node not found or list empty
        if node is None:
            print("Node not found.")
            return

        # If node has one child or no child
        if node.right is None or node.left is None:
            self.delete_leaf(node, parent)
            return

        # If node has two children
        inorder_pred, parent_inorder_pred = self.min_value_node(node)
        node.data = inorder_pred.data
        self.delete_leaf(inorder_pred, parent_inorder_pred)


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

    tree.deletion_iter(14)

    tree.inorder(tree.root)  # Sorted numbers
