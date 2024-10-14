def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'H'],
        'E': ['B'],
        'F': ['C', 'I'],
        'G': ['C'],
        'H': ['D'],
        'I': ['F']
    }
    
    print("DFS starting from vertex 'A':")
    dfs(graph, 'A')
