import random

def objective_function(x):
    return -(x**2 - 4*x + 4)

def hill_climbing(starting_point, step_size, max_iterations):
    current_point = starting_point
    current_value = objective_function(current_point)
    
    for _ in range(max_iterations):
        next_point = current_point + random.uniform(-step_size, step_size)
        next_value = objective_function(next_point)
        
        if next_value > current_value:
            current_point = next_point
            current_value = next_value
    
    return current_point, current_value

if __name__ == "__main__":
    starting_point = random.uniform(-10, 10)
    step_size = 0.1
    max_iterations = 1000
    best_point, best_value = hill_climbing(starting_point, step_size, max_iterations)
    print(f"Best point: {best_point}")
    print(f"Best value: {best_value}")
