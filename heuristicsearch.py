import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal, h_func):
    open_set = []
    closed_set = set()
    start_node = Node(start, None, 0, h_func(start))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.name == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_node.name)

        for neighbor, cost in get_neighbors(current_node.name):
            if neighbor in closed_set:
                continue
            
            g_cost = current_node.g + cost
            h_cost = h_func(neighbor)
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

            if any(node.name == neighbor and node.g <= g_cost for node in open_set):
                continue
            
            heapq.heappush(open_set, neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]

def get_neighbors(node):
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    return graph.get(node, [])

def heuristic(node):
    heuristics = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }
    return heuristics.get(node, float('inf'))

start_node = 'A'
goal_node = 'D'
path = a_star_search(start_node, goal_node, heuristic)

print("Path from {} to {}: {}".format(start_node, goal_node, path))
