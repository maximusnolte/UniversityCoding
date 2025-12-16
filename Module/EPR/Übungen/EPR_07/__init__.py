"""Curiosity Path algorithms for Übung 07.

Das Modul stellt mehrere Optimierungsfunktionen bereit, die auf einem
gewichteten Graphen Wege zwischen zwei Knoten bestimmen. Die Beispiele
orientieren sich an dem im Übungsblatt dargestellten Graphen (Knoten A–H).

Die wichtigsten Helferfunktionen liefern zu Demonstrationszwecken bereits
DocTest-Beispiele, sodass sie mit ``python -m doctest -v Module/EPR/Übungen/EPR_07/__init__.py``
überprüft werden können.
"""
from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Callable, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple
import math
import random

Node = str
NeighborList = Mapping[Node, int]
Graph = Mapping[Node, NeighborList]


# Beispielgraph aus dem Arbeitsblatt. Alle Kanten sind ungerichtet.
# Die Koordinaten dienen nur als Heuristik für A*.
COORDINATES: Dict[Node, Tuple[int, int]] = {
    "A": (0, 2),
    "B": (0, 1),
    "C": (0, 0),
    "D": (1, 2),
    "E": (1, 1),
    "F": (1, 0),
    "G": (2, 1),
    "H": (2, 0),
}

EXAMPLE_GRAPH: Dict[Node, Dict[Node, int]] = {
    "A": {"B": 1, "D": 2},
    "B": {"A": 1, "C": 2, "D": 2, "E": 4},
    "C": {"B": 2, "F": 4},
    "D": {"A": 2, "B": 2, "E": 3, "G": 2},
    "E": {"D": 3, "B": 4, "F": 4, "G": 2},
    "F": {"C": 4, "E": 4, "H": 3},
    "G": {"D": 2, "E": 2, "H": 4},
    "H": {"F": 3, "G": 4},
}


@dataclass(frozen=True)
class PathResult:
    path: Tuple[Node, ...]
    total_weight: int

    def __str__(self) -> str:  # pragma: no cover - reine Darstellung
        return f"{' -> '.join(self.path)} (Kosten: {self.total_weight})"


def path_cost(graph: Graph, path: Sequence[Node]) -> int:
    """Berechnet die Gesamtkosten eines Pfads.

    >>> path_cost(EXAMPLE_GRAPH, ["A", "B", "C", "F", "H"])
    10
    >>> path_cost(EXAMPLE_GRAPH, ["A", "D", "G", "H"])
    8
    """

    if len(path) < 2:
        return 0
    cost = 0
    for current, nxt in zip(path, path[1:]):
        try:
            cost += graph[current][nxt]
        except KeyError as exc:  # pragma: no cover - Eingabesicherung
            raise ValueError(f"Keine Kante zwischen {current} und {nxt}") from exc
    return cost


def manhattan_heuristic(node: Node, goal: Node) -> float:
    """Einfache Heuristik auf Basis der Koordinaten.

    >>> manhattan_heuristic("A", "H")
    4.0
    """

    x1, y1 = COORDINATES[node]
    x2, y2 = COORDINATES[goal]
    return float(abs(x1 - x2) + abs(y1 - y2))


def greedy_path(graph: Graph, start: Node, goal: Node) -> PathResult:
    """Wählt iterativ den kostengünstigsten Nachbarn (Greedy).

    >>> greedy_path(EXAMPLE_GRAPH, "A", "H").path
    ('A', 'B', 'C', 'F', 'H')
    >>> greedy_path(EXAMPLE_GRAPH, "A", "H").total_weight
    10
    """

    path: List[Node] = [start]
    visited = {start}
    while path[-1] != goal:
        current = path[-1]
        options = [
            (weight, manhattan_heuristic(neighbor, goal), neighbor)
            for neighbor, weight in graph[current].items()
            if neighbor not in visited
        ]
        if not options:
            raise ValueError("Greedy-Suche steckt fest; kein unbesuchter Nachbar")
        weight, _, best_neighbor = min(options, key=lambda tpl: (tpl[0], tpl[1]))
        path.append(best_neighbor)
        visited.add(best_neighbor)
    return PathResult(tuple(path), path_cost(graph, path))


def next_best_path(graph: Graph, start: Node, goal: Node) -> PathResult:
    """Best-First-Suche mit Heuristik (ähnlich A*).

    >>> next_best_path(EXAMPLE_GRAPH, "A", "H").path
    ('A', 'D', 'G', 'H')
    >>> next_best_path(EXAMPLE_GRAPH, "A", "H").total_weight
    8
    """

    frontier: List[Tuple[float, int, Tuple[Node, ...]]] = []
    heappush(frontier, (manhattan_heuristic(start, goal), 0, (start,)))
    best_seen: MutableMapping[Tuple[Node, ...], int] = {(start,): 0}

    while frontier:
        priority, cost_so_far, path = heappop(frontier)
        current = path[-1]
        if current == goal:
            return PathResult(path, cost_so_far)
        for neighbor, edge_cost in graph[current].items():
            if neighbor in path:
                continue
            new_cost = cost_so_far + edge_cost
            new_path = path + (neighbor,)
            estimate = new_cost + manhattan_heuristic(neighbor, goal)
            if best_seen.get(new_path, math.inf) <= new_cost:
                continue
            best_seen[new_path] = new_cost
            heappush(frontier, (estimate, new_cost, new_path))
    raise ValueError("Kein Pfad gefunden")


ScoringFunction = Callable[[int, int, int], float]


def score_distance_first(total: int, steps: int, max_edge: int) -> float:
    """Bewertet fast ausschließlich die Länge.

    >>> score_distance_first(10, 4, 3)
    10.0
    """

    return float(total)


def score_balanced(total: int, steps: int, max_edge: int) -> float:
    """Balanciert Gesamtkosten und Anzahl der Schritte.

    >>> score_balanced(10, 4, 3)
    12.0
    """

    return total + 0.5 * steps


def score_risk_averse(total: int, steps: int, max_edge: int) -> float:
    """Bestrafte riskante Kanten (hohe Einzelgewichte).

    >>> score_risk_averse(10, 4, 4)
    14.0
    """

    return float(total + max_edge)


def multiobjective_path(
    graph: Graph,
    start: Node,
    goal: Node,
    scoring: ScoringFunction = score_distance_first,
) -> PathResult:
    """Sucht einen Pfad mithilfe einer frei wählbaren Bewertungsfunktion.

    >>> multiobjective_path(EXAMPLE_GRAPH, "A", "H", score_distance_first).path
    ('A', 'D', 'G', 'H')
    >>> multiobjective_path(EXAMPLE_GRAPH, "A", "H", score_balanced).path
    ('A', 'D', 'G', 'H')
    """

    frontier: List[Tuple[float, int, int, Tuple[Node, ...]]] = []
    heappush(frontier, (0.0, 0, 0, (start,)))
    seen: MutableMapping[Tuple[Node, ...], float] = {(start,): 0.0}

    while frontier:
        score, total, max_edge, path = heappop(frontier)
        current = path[-1]
        if current == goal:
            return PathResult(path, total)
        for neighbor, edge_cost in graph[current].items():
            if neighbor in path:
                continue
            new_total = total + edge_cost
            new_max = max(max_edge, edge_cost)
            new_path = path + (neighbor,)
            new_score = scoring(new_total, len(new_path) - 1, new_max)
            if seen.get(new_path, math.inf) <= new_score:
                continue
            seen[new_path] = new_score
            heappush(frontier, (new_score, new_total, new_max, new_path))
    raise ValueError("Kein Pfad gefunden")


def random_walk(
    graph: Graph,
    start: Node,
    goal: Node,
    rng: random.Random | None = None,
    max_steps: int = 20,
) -> PathResult:
    """Zufällige Exploration mit reproduzierbarem Seed.

    >>> rng = random.Random(7)
    >>> random_walk(EXAMPLE_GRAPH, "A", "H", rng=rng).path
    ('A', 'D', 'B', 'E', 'F', 'H')
    """

    rng = rng or random.Random()
    current = start
    path = [current]
    for _ in range(max_steps):
        if current == goal:
            break
        neighbors = list(graph[current])
        if goal in neighbors:
            current = goal
            path.append(current)
            break
        unvisited = [n for n in neighbors if n not in path]
        pool = unvisited or neighbors
        current = rng.choice(pool)
        path.append(current)
    else:
        raise ValueError("Maximale Schrittzahl erreicht, Ziel nicht gefunden")
    return PathResult(tuple(path), path_cost(graph, path))


__all__ = [
    "COORDINATES",
    "EXAMPLE_GRAPH",
    "PathResult",
    "path_cost",
    "manhattan_heuristic",
    "greedy_path",
    "next_best_path",
    "score_distance_first",
    "score_balanced",
    "score_risk_averse",
    "multiobjective_path",
    "random_walk",
]
