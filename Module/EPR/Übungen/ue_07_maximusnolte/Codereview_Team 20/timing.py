"""
Measures execution time of Greedy Search and Recursive Weighted-Sum Search
on a graph with costs and distraction values. Prints runtimes in seconds.
"""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import search_algorythms
import timeit

if __name__ == "__main__":
    # --- Graph definition ---
    g = {
        'A': {'B': (3, 2), 'C': (1, 0)},
        'B': {'D': (4, 5), 'E': (2, 1)},
        'C': {'D': (2, 3)},
        'D': {'F': (3, 4)},
        'E': {'F': (5, 0)},
        'F': {}
    }
    START_NODE = 'A'
    GOAL_NODE = 'F'

    # --- Measure runtime of greedy search ---
    greedy_time = timeit.timeit(
        lambda: search_algorythms.greedy_search(g, START_NODE, GOAL_NODE),
        number=10_000
    )
    print(f"Greedy runtime (10k runs): {greedy_time:.6f} seconds")

    # --- Measure runtime of recursive weighted-sum search ---
    rec_time = timeit.timeit(
        lambda: search_algorythms.recursive_weighted_search(g, START_NODE, GOAL_NODE),
        number=1_000
    )
    print(f"Recursive Weighted Sum runtime (1k runs): {rec_time:.6f} seconds")