"""
Dieses Modul definiert die Klasse `BerryBush`, eine Spezialisierung von
`Plant`, die eine Wahrscheinlichkeit für
giftige Beeren verwaltet.
"""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import random

from EPR.Übungen.ue_08.Plant import Plant


class BerryBush(Plant):
    """Repräsentiert einen Beerstrauch.

    Ein `BerryBush` erweitert `Plant` um eine Wahrscheinlichkeit,
    dass eine Beere giftig ist.

    Attribute:
        poison_chance (float): Wahrscheinlichkeit im Bereich 0.0–1.0, dass
            eine geerntete Beere giftig ist.
        (Geerbt von `Plant`): min_size, size, food_value, regen_rate, id,
            species, max_size, alive.
    """

    def __init__(self, poison_chance, **plant_args):
        """Initialisiere einen neuen `BerryBush`.

        Args:
            poison_chance (float): Wahrscheinlichkeit (0.0–1.0), dass eine
                Beere giftig ist.
            **plant_args: Weitergeleitete Schlüsselwortargumente an den
                `Plant`-Konstruktor (z. B. `id`, `species`, `min_size`,
                `food_value`, `regen_rate`, `max_size`).

        Returns:
            None
        """
        super().__init__(**plant_args)

        self.poison_chance = poison_chance

    def reproduce(self):
        """Attempt to reproduce by creating a new Plant instance.

        Reproduction is attempted only when the plant has reached
        `max_size`. There is a probabilistic check (50% chance) to decide
        whether a new offspring is produced. The offspring receives the
        same parameters (species, min_size, food_value, regen_rate, max_size)
        and an `id` of `None`.

        Returns:
            Plant | None: A new `Plant` instance if reproduction occurs,
            otherwise `None`.
        """
        if self.size == self.max_size:
            if random.random() < 0.5:
                return self.__class__(
                    poison_chance=self.poison_chance,
                    id=None,
                    min_size=self.min_size,
                    food_value=self.food_value,
                    regen_rate=self.regen_rate,
                    max_size=self.max_size,
                    species=self.species
                )
        return None
