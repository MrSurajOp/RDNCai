import heapq

class Node:
    def __init__(self, name, cost=0, heuristic=0):
        self.name = name
        self.cost = cost
        self.heuristic = heuristic
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star(start_name, goal_name, graph, heuristics):
    open_list = []
    closed_list = set()
    start_node = Node(start_name, cost=0, heuristic=heuristics.get(start_name, float('inf')))
    heapq.heappush(open_list, (start_node.cost + start_node.heuristic, start_node))

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.name == goal_name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.name)

        for neighbor, cost in graph.get(current_node.name, {}).items():
            if neighbor in closed_list:
                continue
            
            g_cost = current_node.cost + cost
            h_cost = heuristics.get(neighbor, float('inf'))
            neighbor_node = Node(neighbor, cost=g_cost, heuristic=h_cost)
            neighbor_node.parent = current_node

            if not any(node.name == neighbor and node.cost <= g_cost for _, node in open_list):
                heapq.heappush(open_list, (g_cost + h_cost, neighbor_node))

    return None

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    heuristics = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }
    path = a_star('A', 'D', graph, heuristics)
    print("Path found:", path)
