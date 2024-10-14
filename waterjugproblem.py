from collections import deque

def water_jug_problem(capacity_jug1, capacity_jug2, target_volume):
    queue = deque()
    visited = set()
    initial_state = (0, 0)
    queue.append((initial_state, []))
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()
        jug1, jug2 = current_state

        if jug1 == target_volume or jug2 == target_volume:
            return path + [current_state]

        next_states = [
            (capacity_jug1, jug2),  # Fill jug1
            (jug1, capacity_jug2),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (jug1 - min(jug1, capacity_jug2 - jug2), jug2 + min(jug1, capacity_jug2 - jug2)),  # Pour jug1 into jug2
            (jug1 + min(jug2, capacity_jug1 - jug1), jug2 - min(jug2, capacity_jug1 - jug1))   # Pour jug2 into jug1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [current_state]))

    return None

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    solution = water_jug_problem(jug1_capacity, jug2_capacity, target)
    if solution:
        print(f"Solution found: {solution}")
    else:
        print("No solution found.")
