import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current.val

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current.val

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        
        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

def sum_of_all(root):
    if root is None:
        return 0
    return root.val + sum_of_all(root.left) + sum_of_all(root.right)


# Test
root = Node(50)
for i in range(10):
    root = insert(root, random.randint(1, 100))

# min_node = min_value_node(root)
# print(f"Minimum value in the BST: {min_node.val}")
print(root)
print(min_value_node(root))
print(max_value_node(root))
print(sum_of_all(root))