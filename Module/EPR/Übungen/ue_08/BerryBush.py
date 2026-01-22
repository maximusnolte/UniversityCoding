"""
Dieses Modul definiert die Klasse `BerryBush`, eine Spezialisierung von
`Plant`, die eine Wahrscheinlichkeit für
giftige Beeren verwaltet.
"""

from EPR.Übungen.ue_08.Plant import Plant


class BerryBush(Plant):
    """Repräsentiert einen Beerstrauch.

    Ein `BerryBush` erweitert `Plant` um eine Wahrscheinlichkeit, dass eine Beere giftig ist.

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
