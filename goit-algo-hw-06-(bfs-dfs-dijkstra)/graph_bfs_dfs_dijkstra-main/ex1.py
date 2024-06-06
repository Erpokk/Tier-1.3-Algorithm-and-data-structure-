
import networkx as nx
import matplotlib.pyplot as plt


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

pos = {
    "Whiterun": (0, 0),
    "Falkreath": (-1,-4),
    "Riften": (4, -4),
    "Windhelm": (4, 1),
    "Winterhold": (3, 3.5),
    "Dawnstar": (0, 4),
    "Morthal": (-1, 2.5),
    "Solitude": (-3, 3.5),
    "Markarth": (-4, 0)
}


num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print("Amount of nodes:", num_nodes)
print("Amount of edges:", num_edges)
print("Nodes degree:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")


nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.xticks(range(-4, 4, 1))
plt.yticks(range(-4, 4, 1))

plt.show()

