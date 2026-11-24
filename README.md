# WATER JUG PROBLEM USING BREADTH-FIRST SEARCH (BFS)

## Aim:
To write a Python program to solve the Water Jug problem (capacities 8L, 5L, and 3L) using Breadth-First Search (BFS) to divide 8 liters of water into two equal parts of 4 liters each `(4, 4, 0)`.

## Equipments required:
* **Hardware** – PCs
* **Software** – VS Code / Python 3 Installation / Moodle-Code Runner

## Algorithm:
**Step 1:** Import the `deque` module from `collections` to implement the BFS queue.

**Step 2:** Define the jug capacities `(8, 5, 3)`, the initial state `(8, 0, 0)`, and the goal state `(4, 4, 0)`.

**Step 3:** Initialize a queue with the initial state and a `visited` set to track explored states.

**Step 4:** Loop while the queue is not empty; dequeue the front state and check if it matches the goal state `(4, 4, 0)`. If matched, return the solution path.

**Step 5:** Generate all valid next states by pouring water from jug `i` to jug `j` (either until jug `i` is empty or jug `j` is full). Add unvisited states to the queue and `visited` set.

**Step 6:** Print the step-by-step path from the initial state to the goal state and end the program.

## Program:
**Developed by:** L Ganesh Kanna  
**REG NO:** 212225230072 

```
python
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
```

## Output:
![alt text](<Screenshot 2026-11-24 102855.png>)

## Result:
Thus, the solution for the Water Jug problem is successfully solved in 7 steps using a Python program.
