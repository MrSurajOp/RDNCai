from collections import deque

def is_valid(state):
    left_m, left_c, boat, right_m, right_c = state
    if left_m < left_c and left_m > 0:
        return False
    if right_m < right_c and right_m > 0:
        return False
    return True

def generate_next_states(state):
    possible_states = []
    left_m, left_c, boat, right_m, right_c = state

    if boat == 1:  # Boat is on the left bank
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:  # Valid moves
                    new_left_m = left_m - m
                    new_left_c = left_c - c
                    new_right_m = right_m + m
                    new_right_c = right_c + c
                    if is_valid((new_left_m, new_left_c, 0, new_right_m, new_right_c)):
                        possible_states.append((new_left_m, new_left_c, 0, new_right_m, new_right_c))
    else:  # Boat is on the right bank
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:  # Valid moves
                    new_left_m = left_m + m
                    new_left_c = left_c + c
                    new_right_m = right_m - m
                    new_right_c = right_c - c
                    if is_valid((new_left_m, new_left_c, 1, new_right_m, new_right_c)):
                        possible_states.append((new_left_m, new_left_c, 1, new_right_m, new_right_c))
    
    return possible_states

def solve_missionary_cannibal():
    initial_state = (3, 3, 1, 0, 0)
    target_state = (0, 0, 0, 3, 3)
    
    if not is_valid(initial_state):
        raise ValueError("Initial state is invalid!")

    queue = deque()
    visited = set()
    queue.append(([initial_state], []))
    visited.add(initial_state)

    while queue:
        current_path, actions = queue.popleft()
        current_state = current_path[-1]

        if current_state == target_state:
            return actions

        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((
                    current_path + [next_state],
                    actions + [f"Move {'M' * next_state[0]}C{'C' * next_state[1]} {'to' if next_state[2] == 1 else 'from'} {'right' if next_state[2] == 1 else 'left'} bank"]
                ))

    return None

solution = solve_missionary_cannibal()

if solution:
    print("Solution found:")
    for action in solution:
        print(action)
else:
    print("No solution found.")
