import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    prior_q = [(0, start)]
    visited = set()

    while prior_q:
        cur_dis, cur_vertex = heapq.heappop(prior_q)
        if cur_vertex in visited:
            continue

        visited.add(cur_vertex)

        for neighbor, weight in graph[cur_vertex].items():
            distance = cur_dis + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(prior_q, (distance, neighbor))

    return distances

graph = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 3: 5},
    3: {}
}

start_vertex = 0
distances = dijkstra(graph, start_vertex)
print(distances)