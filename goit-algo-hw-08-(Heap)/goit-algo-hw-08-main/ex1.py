import heapq

def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0 
    
    heapq.heapify(cable_lengths)  
    total_cost = 0

    while len(cable_lengths) > 1:  
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second
        total_cost += cost
        heapq.heappush(cable_lengths, cost)
    return total_cost


cable_lengths = [8, 4, 6, 12]  
total_cost = min_cost_to_connect_cables(cable_lengths)
print("Мінімальні загальні витрати на об'єднання кабелів:", total_cost)
