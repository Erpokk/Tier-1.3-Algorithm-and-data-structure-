import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

def insert_node(arr, index):
    if index < len(arr):
        node = Node(arr[index])
        node.left = insert_node(arr, 2 * index + 1)
        node.right = insert_node(arr, 2 * index + 2)
        return node
    return None

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_color(step, total_steps):
    """Генерує колір від темного до світлого в залежності від кроку."""
    base_color = [135, 206, 250]  
    lighten_factor = step / total_steps
    new_color = [int(c * (1 - lighten_factor) + 255 * lighten_factor) for c in base_color]
    return f"#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}"

def dfs(node, total, visited, index=0):
    if node is None:
        return index
    node.color = generate_color(index, total)
    visited.append(node)
    draw_tree(root, f"DFS Step {index + 1}")
    index += 1
    index = dfs(node.left, total, visited, index)
    index = dfs(node.right, total, visited, index)
    return index

def bfs(node, total):
    queue = [node]
    index = 0
    while queue:
        current = queue.pop(0)
        current.color = generate_color(index, total)
        draw_tree(root, f"BFS Step {index + 1}")
        index += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

nums = [4, 10, 3, 5, 1, 7, 11, 15]
heapq.heapify(nums)
root = insert_node(nums, 0)
total_nodes = count_nodes(root)


visited_dfs = []
dfs(root, total_nodes, visited_dfs)

bfs(root, total_nodes)