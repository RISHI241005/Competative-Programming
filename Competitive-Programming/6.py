# Height of a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return (left if left > right else right) + 1

# build the tree as in C program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = None
root.left.right = None
root.right.left = None
root.right.right = None

print("Height of tree =", height(root))