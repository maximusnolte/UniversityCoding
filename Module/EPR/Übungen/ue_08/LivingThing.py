"""
This module defines the `LivingThing` class, a minimal representation
of a living entity with an identifier, species, maximum size and alive status.
"""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"


class LivingThing:
    """Represent a simple living entity.

    Attributes:
        id (str): Unique identifier of the living thing.
        species (str): Species or label of the living thing.
        max_size (int | float): Maximum size or size limit.
        alive (bool): Life status; True while the entity is alive.
    """

    def __init__(self, id, species, max_size):
        """Initialize a new LivingThing.

        Args:
            id (str): Unique identifier.
            species (str): Species or label.
            max_size (int | float): Maximum size.

        Returns:
            None
        """
        self.id = id
        self.species = species
        self.max_size = max_size
        self.alive = True

    def die(self):
        """Set the alive flag to False and return a confirmation message.

        This method mutates the object's internal state (`alive`) and
        returns a readable confirmation that the living thing has died.

        Returns:
            str: Message in the format "`<id> has died.`".
        """
        self.alive = False
        return f"{self.id} has died."
