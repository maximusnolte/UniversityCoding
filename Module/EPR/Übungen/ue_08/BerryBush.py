from EPR.Übungen.ue_08.Plant import Plant


class BerryBush(Plant):

    def __init__(self, berry_count,poison_chance, **plant_args):
        super().__init__(**plant_args)

        self.berry_count = berry_count
        self.poison_chance = poison_chance  # 10% chance that a berry is
    # poisonous