# wap in python to find the no of leaf nodes in a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return leaf(root.left) + leaf(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = None
root.left.right = None
root.right.left = None
root.right.right = None

print("Number of leaf nodes =", leaf(root))