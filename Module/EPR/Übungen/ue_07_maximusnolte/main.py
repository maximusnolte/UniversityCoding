"""Greedy Search Algorithm Implementation for a Graph with Cost and Distraction Metrics."""

import timeit

def calculate_efficiency (cost, distraction):
    """Calculate efficiency as distraction divided by (cost + 1) to avoid division by zero.
        :arg cost: The cost of the edge.
        :arg distraction: The distraction of the edge.
        :return: The efficiency value.
    """
    return distraction / (cost + 1)

def choose_best_neighbor(neighbors, visited):
    """Choose the neighbor with the highest efficiency that hasn't been visited yet.
        :arg neighbors: The list of neighbors.
        :arg visited: The set of visited nodes.
        :return: The best neighbor
    """
    best_efficiency = -float('inf')
    best = None

    for neighbor, (cost, distraction) in neighbors.items():
        if neighbor not in visited:
            eff = calculate_efficiency(cost, distraction)
            if eff > best_efficiency:
                best_efficiency = eff
                best = (neighbor, cost, distraction)

    return best


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
        result = choose_best_neighbor(graph[current], visited)
        if result is None:
            return None, None, None

        next_node, next_cost, next_distraction = result

        path.append(next_node)
        total_cost += next_cost
        total_distraction += next_distraction
        visited.add(next_node)
        current = next_node

    return path, total_cost, total_distraction


if __name__ == "__main__":
    g = {
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
    START_NODE = 'A'
    GOAL_NODE = 'F'

    time = timeit.timeit(
        lambda: greedy_search(g, START_NODE, GOAL_NODE),
        number=10_000
    )

    print(f"Greedy runtime (10k runs): {time} seconds")
