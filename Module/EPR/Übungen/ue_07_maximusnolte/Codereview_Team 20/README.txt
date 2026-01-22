# Project Documentation

## Overview

This project implements two search algorithms for graphs with cost and distraction metrics:

- Greedy Search: chooses the next neighbor with the highest efficiency (distraction / (cost + 1)).
- Recursive Weighted-Sum Search: recursively finds the path that minimizes the weighted sum alpha * cost - beta * distraction.

Both algorithms are applied to graphs where each edge has a cost and a distraction value.

---

## Files

### search_algorythms.py

Contains the implementation of the search algorithms and supporting functions.

- calculate_efficiency(cost, distraction): Calculate efficiency as distraction divided by (cost + 1). Returns the efficiency value.
- weighted_sum(cost, distraction, alpha=1.0, beta=1.0): Calculate a scalar optimization value using a weighted sum. Returns alpha*cost - beta*distraction.
- lexicographic(cost, distraction): Lexicographic multi-objective optimization. Returns (cost, -distraction).
- dominates(cost1, distraction1, cost2, distraction2): Check whether the first path Pareto dominates the second path. Returns True or False.
- choose_best_neighbor(neighbors, visited): Choose the neighbor with the highest efficiency not in visited. Returns (neighbor, cost, distraction).
- greedy_search(graph, start, goal): Perform greedy search from start to goal. Returns (path, total_cost, total_distraction).
- recursive_weighted_search(graph, current, goal, visited=None, alpha=1.0, beta=1.0): Recursively find the path minimizing weighted sum alpha*cost - beta*distraction. Returns (path, total_cost, total_distraction) or (None, None, None).

### timing.py

Measures execution time of greedy_search and recursive_weighted_search on a sample graph with costs and distraction values. Prints runtimes in seconds.

---

## Usage

1. Run `search_algorythms.py` to execute doctest examples:
2. Run `timing.py` to measure algorithm runtimes:
