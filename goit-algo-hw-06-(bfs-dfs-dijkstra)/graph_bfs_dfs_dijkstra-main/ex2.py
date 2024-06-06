from collections import deque
import networkx as nx

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])

    while queue:
        (vertex, path) = queue.popleft()
        if vertex == goal:
            return path
        for neighbor in graph[vertex]:
            if neighbor not in path:  
                queue.append((neighbor, path + [neighbor]))
    return []

def dfs_recursive(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs_recursive(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path

G = nx.Graph()

G.add_edge("Whiterun", "Falkreath", weight=10)
G.add_edge("Whiterun", "Riften", weight=18)
G.add_edge("Whiterun", "Windhelm", weight=11)
G.add_edge("Whiterun", "Winterhold", weight=14)
G.add_edge("Whiterun", "Dawnstar", weight=11)
G.add_edge("Whiterun", "Morthal", weight=9)
G.add_edge("Whiterun", "Solitude", weight=15)
G.add_edge("Whiterun", "Markarth", weight=20)
G.add_edge("Falkreath", "Riften", weight=20)
G.add_edge("Riften", "Windhelm", weight=15)
G.add_edge("Windhelm", "Winterhold", weight=6)
G.add_edge("Winterhold", "Dawnstar", weight=8)
G.add_edge("Dawnstar", "Solitude", weight=10)
G.add_edge("Solitude", "Markarth", weight=14)
G.add_edge("Markarth", "Falkreath", weight=17)
G.add_edge("Morthal", "Solitude", weight=5)
G.add_edge("Morthal", "Dawnstar", weight=8)
G.add_edge("Morthal", "Markarth", weight=15)

start_node = 'Riften'
goal_node = 'Solitude'
path = bfs_path(G, start_node, goal_node)
if path:
    print("Way from", start_node, "to", goal_node, ":", path)
else:
    print("Pass not found")

path = dfs_recursive(G, start_node, goal_node)
if path:
    print("Way from", start_node, "to", goal_node, ":", path)
else:
    print("Pass not found")
