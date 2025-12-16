"""Kommandozeilen-Einstieg für die EPR_07-Algorithmen.

Beispiele
---------
Greedy-Suche von A nach H:
    python -m Module.EPR.Übungen.EPR_07 --algo greedy

Best-First (A*-ähnlich):
    python -m Module.EPR.Übungen.EPR_07 --algo best

Multi-Objective mit Risikovermeidung:
    python -m Module.EPR.Übungen.EPR_07 --algo risk --start A --goal H

Zufälliger Walk mit reproduzierbarem Seed:
    python -m Module.EPR.Übungen.EPR_07 --algo random --seed 7
"""
from __future__ import annotations

import argparse
import random
from typing import Callable, Dict

from . import (
    EXAMPLE_GRAPH,
    PathResult,
    greedy_path,
    multiobjective_path,
    next_best_path,
    random_walk,
    score_balanced,
    score_distance_first,
    score_risk_averse,
)

Algorithm = Callable[[str, str, random.Random | None], PathResult]


def _multiobjective_runner(scoring_fn):
    def _run(start: str, goal: str, _rng: random.Random | None) -> PathResult:
        return multiobjective_path(EXAMPLE_GRAPH, start, goal, scoring=scoring_fn)

    return _run


def _random_runner(start: str, goal: str, rng: random.Random | None) -> PathResult:
    return random_walk(EXAMPLE_GRAPH, start, goal, rng=rng)


ALGOS: Dict[str, Algorithm] = {
    "greedy": lambda start, goal, _rng=None: greedy_path(EXAMPLE_GRAPH, start, goal),
    "best": lambda start, goal, _rng=None: next_best_path(EXAMPLE_GRAPH, start, goal),
    "distance": _multiobjective_runner(score_distance_first),
    "balanced": _multiobjective_runner(score_balanced),
    "risk": _multiobjective_runner(score_risk_averse),
    "random": _random_runner,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Pfadsuche im Beispielgraphen A–H")
    parser.add_argument("--start", default="A", help="Startknoten (Standard: A)")
    parser.add_argument("--goal", default="H", help="Zielknoten (Standard: H)")
    parser.add_argument(
        "--algo",
        choices=sorted(ALGOS),
        default="best",
        help="Algorithmus: greedy, best, distance, balanced, risk, random",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optionaler Seed für reproduzierbare Zufallssuche",
    )
    args = parser.parse_args(argv)

    runner = ALGOS[args.algo]
    rng = random.Random(args.seed) if args.seed is not None else None
    result = runner(args.start, args.goal, rng)

    print(f"Algorithmus: {args.algo}")
    print(f"Pfad: {' -> '.join(result.path)}")
    print(f"Gesamtkosten: {result.total_weight}")
    return 0


if __name__ == "__main__":  # pragma: no cover - manuelles Ausführen
    raise SystemExit(main())
