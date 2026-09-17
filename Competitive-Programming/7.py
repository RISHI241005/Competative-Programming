# wap in python to find the no of nodes in a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = None
root.left.right = None
root.right.left = None
root.right.right = None

print("Number of nodes =", count(root))