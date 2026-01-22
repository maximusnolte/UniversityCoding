"""Greedy and Recursive Weighted-Sum Search Implementation for Graphs with Cost and Distraction Metrics."""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

def calculate_efficiency (cost, distraction):
    """Calculate efficiency as distraction divided by (cost + 1) to avoid division by zero.
        :arg cost: The cost of the edge.
        :arg distraction: The distraction of the edge.
        :return: The efficiency value.

    >>> calculate_efficiency(0, 5)
    5.0
    >>> calculate_efficiency(4, 2)
    0.4
    >>> calculate_efficiency(3, 0)
    0.0
    """
    return distraction / (cost + 1)

def weighted_sum(cost, distraction, alpha=1.0, beta=1.0):
    """
    Calculate a scalar optimization value using a weighted sum approach.
    The objective is to minimize the returned value.
    Costs are minimized, while distraction is maximized by subtraction.
    Formula:    f(cost, distraction) = alpha * cost - beta * distraction

        :param cost: Total cost of the path (to be minimized)
        :param distraction: Total distraction value of the path (to be maximized)
        :param alpha: Weight factor for the cost
        :param beta: Weight factor for the distraction
        :return: Scalar optimization value (lower is better)

    >>> weighted_sum(6, 7)
    -1.0
    >>> weighted_sum(10, 3)
    7.0
    >>> weighted_sum(0, 0)
    0.0
    """
    return alpha * cost - beta * distraction

def lexicographic(cost, distraction):
    """
    Perform lexicographic multi-objective optimization.

    Primary objective:
        -Minimize total cost
    Secondary objective (only if costs are equal):
        -Maximize total distraction

        :param cost: Total cost of the path
        :param distraction: Total distraction value of the path
        :return: Tuple (cost, -distraction)

    >>> lexicographic(6, 7) < lexicographic(10, 100)
    True
    >>> lexicographic(6, 5) < lexicographic(6, 7)
    False
    >>> lexicographic(3, 1) < lexicographic(3, 0)
    True
    """
    return (cost, -distraction)

def dominates(cost1, distraction1, cost2, distraction2):
    """
    Check whether the first path Pareto dominates the second path.

    A path dominates another path if it is:
        -no worse in all objectives, and
        -strictly better in at least one objective.

    Cost is minimized, distraction is maximized.

        :param cost1: Cost of the first path
        :param distraction1: Distraction of the first path
        :param cost2: Cost of the second path
        :param distraction2: Distraction of the second path
        :return: True if the first path dominates the second path

    >>> dominates(6, 7, 10, 3)
    True
    >>> dominates(6, 7, 6, 7)
    False
    >>> dominates(10, 5, 6, 7)
    False
    """
    return (
        cost1 <= cost2 and
        distraction1 >= distraction2 and
        (cost1 < cost2 or distraction1 > distraction2)
    )

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
        Greedy runtime (10k runs): 0.017274 seconds

    >>> neighbors = {'B': (3, 2), 'C': (1, 0)}
    >>> choose_best_neighbor(neighbors, set())
    ('B', 3, 2)
    >>> choose_best_neighbor(neighbors, {'B'})
    ('C', 1, 0)
    >>> choose_best_neighbor(neighbors, {'B', 'C'}) is None
    True
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

def recursive_weighted_search(graph, current, goal, visited = None, alpha = 1.0, beta = 1.0):
    """
        Find the path from current to goal that minimizes the weighted sum (alpha*cost - beta*distraction)
        using recursion. Each node may be visited at most once.

            :param graph: adjacency dictionary, e.g., {'A': {'B': (3,2), 'C': (1,0)}, ...}
            :param current: current node
            :param goal: goal node
            :param visited: set of visited nodes (internal)
            :param alpha: weight for cost
            :param beta: weight for distraction
            :return: tuple (path, total_cost, total_distraction) or (None, None, None) if no path exists
            Recursive Weighted Sum runtime (1k runs): 0.002639 seconds

        >>> g = {
        ...     'A': {'B': (3, 2), 'C': (1, 0)},
        ...     'B': {'D': (4, 5), 'E': (2, 1)},
        ...     'C': {'D': (2, 3)},
        ...     'D': {'F': (3, 4)},
        ...     'E': {'F': (5, 0)},
        ...     'F': {}
        ... }
        >>> recursive_weighted_search(g, 'A', 'F')
        (['A', 'B', 'D', 'F'], 10, 11)
        >>> recursive_weighted_search(g, 'A', 'E')
        (['A', 'B', 'E'], 5, 3)
        >>> recursive_weighted_search(g, 'F', 'A')
        (None, None, None)
        """
    if visited is None:
        visited = set()
    visited.add(current)

    if current == goal:
        return [current], 0, 0

    best_path = None
    best_cost = None
    best_distraction = None
    best_score = float('inf')

    for neighbour, (cost, distraction) in graph.get(current, {}).items():
        if neighbour not in visited:
            result = recursive_weighted_search(graph, neighbour, goal, visited, alpha, beta)
            if result[0] is not None:
                path, total_cost, total_distraction = result
                total_cost += cost
                total_distraction += distraction
                score = alpha * total_cost - beta * total_distraction
                if score < best_score:
                    best_score = score
                    best_path = [current] + path
                    best_cost = total_cost
                    best_distraction = total_distraction

    visited.remove(current)

    if best_path is None:
        return None, None, None

    return best_path, best_cost, best_distraction

if __name__ == "__main__":

    import doctest
    doctest.testmod()
    print("doctests ausgeführt")
