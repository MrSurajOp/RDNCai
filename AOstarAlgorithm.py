class AOStarNode:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.children = []
        self.parent = None

def ao_star(start_name, goal_name, graph, heuristics):
    open_list = [AOStarNode(start_name, heuristics.get(start_name, float('inf')))]
    closed_list = set()

    while open_list:
        current_node = open_list.pop(0)

        if current_node.name == goal_name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.name)

        for child_name in graph.get(current_node.name, []):
            if child_name in closed_list:
                continue
            
            child_node = AOStarNode(child_name, heuristics.get(child_name, float('inf')))
            child_node.parent = current_node
            open_list.append(child_node)

    return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    heuristics = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 0
    }
    path = ao_star('A', 'D', graph, heuristics)
    print("Path found:", path)
