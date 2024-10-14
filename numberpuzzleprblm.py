from collections import deque

def solve_puzzle(initial_state, target_state):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def state_to_str(state):
        return ''.join(map(str, state))
    
    queue = deque()
    visited = set()
    queue.append((initial_state, []))
    visited.add(state_to_str(initial_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == target_state:
            return path
        
        empty_pos = current_state.index(0)
        row, col = empty_pos // 3, empty_pos % 3

        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = list(current_state)
                new_pos = new_row * 3 + new_col
                new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
                new_state_tuple = tuple(new_state)
                new_state_str = state_to_str(new_state_tuple)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_tuple, path + [new_state]))

    return None

initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
target_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
solution = solve_puzzle(initial_state, target_state)

if solution:
    print(f"Solution found in {len(solution)} steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
