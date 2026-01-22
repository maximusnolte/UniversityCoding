import random

from EPR.Übungen.ue_08.LivingThing import LivingThing
class Animal(LivingThing):

    def __init__(
            self,
            # Identität / Herkunft
            gender,
            day_spawned,
            # Lebenszyklus
            max_age,
            mating_age,
            # Fortpflanzung
            mating_start_cooldown,
            # Energie & Ernährung
            max_food,
            food_consumption,
            days_to_starve,
            # Körper & Gesundheit
            size_mult,
            healing_rate,
            # Meta
            **living_thing_args
    ):
        super().__init__(**living_thing_args)
        # Identität
        self.gender = gender
        self.day_spawned = day_spawned
        # Lebenszyklus
        self.max_age = max_age
        self.current_age = 0
        self.mating_age = mating_age
        # Fortpflanzung
        self.mating_start_cooldown = mating_start_cooldown
        self.mating_cooldown = 0
        self.mateable = False
        # Energie & Ernährung
        self.max_food = max_food
        self.food_level = max_food
        self.food_consumption = food_consumption
        self.days_to_starve = days_to_starve
        # Körper & Gesundheit
        self.size_mult = size_mult
        self.health = 100
        self.healing_rate = healing_rate
        self.poisoned = False


    def eat(self, food_restored):
        if self.food_level + food_restored > self.max_food:
            self.food_level = self.max_food
        else:
            self.food_level += food_restored

    def getInjured(self, damage):
        if self.health - damage <= 0:
            self.health = 0
            self.die()
        else:
            self.health -= damage

    def heal(self):
        if self.food_level >= (self.max_food / 2) and not self.poisoned:
            if self.health + self.healing_rate <= 100:
                self.health += self.healing_rate
            else:
                self.health = 100
        elif self.poisoned:
            self.health -= self.healing_rate

    def calculateSize(self):
        if self.current_age * self.size_mult >= self.max_size:
            return self.max_size
        return self.size_mult * self.current_age

    def age(self, current_day):
        age = current_day - self.day_spawned
        if age >= self.max_age:
            if random.random() < 0.6:
                self.die()
                return None
            self.current_age = age
            return age
        else:
            if random.random() < 0.002:
                self.die()
                return None
            else:
                if age >= self.mating_age and self.mating_cooldown == 0:
                    self.mateable = True
                self.current_age = age
                return age

    def mate(self, partner):
        if self.gender:
            self.mateable = False
            self.mating_cooldown = self.mating_start_cooldown
            print(f"Animal {self.id} has mated with Animal {partner.id}., "
                  f"cooldown is now {self.mating_cooldown} for self")

        elif partner.gender:
            partner.mateable = False
            partner.mating_cooldown = partner.mating_start_cooldown
            print(f"Animal {self.id} has mated with Animal {partner.id}., "
                  f"cooldown is now {partner.mating_cooldown} for partner")

        gender = random.choice([True, False])
        return self.__class__(
            id=None,
            max_age= (self.max_age + partner.max_age) // 2,
            size_mult= (self.size_mult + partner.size_mult) // 2,
            food_consumption=self.food_consumption,
            food_level=self.max_food,
            max_food=self.max_food,
            days_to_starve=self.days_to_starve,
            mating_start_cooldown=self.mating_start_cooldown,
            mating_age=self.mating_age,
            healing_rate=self.healing_rate,
            gender=gender,
            species=self.species,
            day_spawned=None
        )