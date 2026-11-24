from collections import deque

def solve_water_jug():
    capacities = (8, 5, 3)
    initial_state = (8, 0, 0)
    goal_state = (4, 4, 0)

    queue = deque([(initial_state, [initial_state])])
    visited = set([initial_state])

    while queue:
        current, path = queue.popleft()

        if current == goal_state:
            return path

        for i in range(3):
            for j in range(3):
                if i != j and current[i] > 0 and current[j] < capacities[j]:
                    pour_amount = min(current[i], capacities[j] - current[j])
                    next_state = list(current)
                    next_state[i] -= pour_amount
                    next_state[j] += pour_amount
                    next_state = tuple(next_state)

                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, path + [next_state]))
    return None

if __name__ == "__main__":
    solution = solve_water_jug()
    if solution:
        print(f"Solution found in {len(solution) - 1} steps:\n")
        for step, state in enumerate(solution):
            print(f"Step {step}: Jug A = {state[0]}L, Jug B = {state[1]}L, Jug C = {state[2]}L  -->  {state}")
