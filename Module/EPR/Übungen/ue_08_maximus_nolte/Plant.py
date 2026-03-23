"""
This module defines the `Plant` class, a specialization of `LivingThing`
that models a plant's size, regeneration, consumption by herbivores,
omnivores and simple reproduction behavior.
"""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import random

from EPR.Übungen.ue_08_maximus_nolte.LivingThing import LivingThing


class Plant(LivingThing):
    """Represent a plant with size, regeneration and reproduction behavior.

    A `Plant` keeps track of a current `size`, a `min_size` threshold below
    which it dies when eaten, a `food_value` that maps size to food amount,
    and a `regen_rate` used to restore size over time. It inherits common
    identity and life status from `LivingThing`.

    Attributes:
        min_size (int | float): Minimum size before the plant dies.
        size (int | float): Current size of the plant.
        food_value (int | float): Amount of food provided per unit size.
        regen_rate (int | float): Size regained when `regenerate` is called.
        id (str | None): Inherited unique identifier.
        species (str): Inherited species label.
        max_size (int | float): Inherited maximum possible size.
        alive (bool): Inherited life status.
    """

    def __init__(self, min_size, food_value, regen_rate,
                 **living_thing_args):
        """Initialize a new Plant.

        Args:
            min_size (int | float): Minimum size before plant dies.
            food_value (int | float): Food amount per unit size.
            regen_rate (int | float): Amount to increase `size` on
            regeneration.
            **living_thing_args: Keyword arguments forwarded to `LivingThing`
                (for example `id`, `species`, `max_size`).

        Returns:
            None
        """
        self.min_size = min_size
        self.size = min_size
        self.food_value = food_value
        self.regen_rate = regen_rate
        super().__init__(**living_thing_args)

    def regenerate(self):
        """Increase the plant's size by `regen_rate` up to `max_size` if alive.

        This method modifies the plant's `size` only when `alive` is True.
        The resulting size will not exceed `max_size`.

        Returns:
            None
        """
        if self.alive:
            if (self.size + self.regen_rate) < self.max_size:
                self.size += self.regen_rate
            else:
                self.size = self.max_size

    def getEaten(self, amount):
        """Reduce the plant's size by `amount`; die if below `min_size`.

        This method deducts `amount` from `size`. If the new `size` falls
        below `min_size`, the plant's `die` method is called and `None` is
        returned to indicate the plant is no longer available. Otherwise
        a confirmation is printed and the updated size is returned.

        Args:
            amount (int | float): Size amount consumed.

        Returns:
            int | float | None: The updated size if the plant survives, or
            `None` if the plant died as a result of being eaten.
        """
        self.size -= amount
        if self.size < self.min_size:
            self.die()
            return None
        print(f"{self.id} has been eaten for {amount} size.")
        return self.size

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
                    id=None,
                    min_size=self.min_size,
                    food_value=self.food_value,
                    regen_rate=self.regen_rate,
                    max_size=self.max_size,
                    species=self.species
                )
        return None
