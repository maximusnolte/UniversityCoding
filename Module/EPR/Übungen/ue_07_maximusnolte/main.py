"""Greedy Search Algorithm Implementation"""

graph = {
    'A': {
        'B': (3, 2),
        'C': (1, 0),
        },
    'B': {
        'D': (4, 5),
        'E': (2, 1),
        },
    'C': {
        'D': (2, 3),
        },
    'D': {
        'F': (3, 4),
        },
    'E': {
        'F': (5, 0),
        },
    'F': {}
}

def calculate_efficiency (cost, distraction):
    """Calculate efficiency as distraction divided by (cost + 1) to avoid division by zero.
        :arg cost: The cost of the edge.
        :arg distraction: The distraction of the edge.
        :return: The efficiency value.
    """
    return distraction / (cost + 1)

def greedy_search(graph, start, goal):
    """Perform a greedy search on the graph from start to goal.
        :arg graph: The graph represented as an adjacency list with costs and distractions.
        :arg start: The starting node.
        :arg goal: The goal node.
        :return: A tuple containing the path, total cost, and total distraction.
    """

    current = start
    path = [start]
    total_cost = 0
    total_distraction = 0
    visited = {start}

    while current != goal:
        neighbors = graph[current]
        best_efficiency = -float('inf')
        next_node = None

        for neighbor, (cost, distraction) in neighbors.items():
            if neighbor not in visited:
                efficiency = calculate_efficiency(cost, distraction)
                if efficiency > best_efficiency:
                    best_efficiency = efficiency
                    next_node = neighbor
                    next_cost = cost
                    next_distraction = distraction

        if next_node is None:
            print("No path found")
            return None, None, None

        path.append(next_node)
        total_cost += next_cost
        total_distraction += next_distraction
        visited.add(next_node)
        current = next_node

    return path, total_cost, total_distraction


if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'
    path, total_cost, total_distraction = greedy_search(graph, start_node, goal_node)

    if path:
        print(f"Path found: {' -> '.join(path)}")
        print(f"Total Cost: {total_cost}")
        print(f"Total Distraction: {total_distraction}")