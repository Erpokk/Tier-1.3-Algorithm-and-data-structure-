def dijkstra(graph, start):
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(current_vertex)

    return distances

graph = {
    "Whiterun": {"Falkreath": 10, "Riften": 18, "Windhelm": 11, "Winterhold": 14, "Dawnstar": 11, "Morthal": 9, "Solitude": 15, "Markarth": 20},
    "Falkreath": {"Riften": 20, "Markarth": 17, "Whiterun": 10  },
    "Riften": {"Windhelm": 15, "Falkreath":20, "Whiterun": 18 },
    "Windhelm": {"Winterhold": 6, "Riften": 15, "Whiterun": 9}, 
    "Winterhold": {"Dawnstar": 8, "Whiterun": 14, "Windhelm":6 },
    "Dawnstar": {"Solitude": 10, "Morthal": 8, "Whiterun": 11, "Winterhold": 8  },
    "Solitude": {"Markarth": 14, "Morthal": 5, "Dawnstar": 10 },
    "Markarth": {"Falkreath": 17, "Morthal": 15, "Whiterun": 20, "Solitude":14 },
    "Morthal": {"Solitude": 5, "Dawnstar": 8, "Markarth": 15, "Whiterun": 9 }
}
start_city = "Morthal"
for vertex in graph:
    if vertex != start_city:
        print(f"The shortest way from {start_city} to '{vertex}': {dijkstra(graph, start_city)[vertex]}")