import random

from EPR.Übungen.ue_08.LivingThing import LivingThing
class Animal(LivingThing):

    def __init__(self, max_age, size_mult, food_consumption, max_food,
                days_to_starve, mating_cooldown, mating_age, healing_rate,
                 gender,
                 species, day_spawned,
                 **living_thing_args):
        super().__init__(**living_thing_args)
        self.food_level = 0
        self.poisoned = False
        self.max_food = max_food
        self.max_age = max_age
        self.mating_age = mating_age
        self.size_mult = size_mult
        self.food_consumption = food_consumption
        self.days_to_starve = days_to_starve
        self.mating_cooldown = mating_cooldown
        self.gender = gender
        self.species = species
        self.health = 100
        self.healing_rate = healing_rate
        self.day_spawned = day_spawned
        self.mateable = False
        self.current_age = 0

    def eat(self, food_restored):
        self.food_level += food_restored

    def mate(self, partner):
        pass

    def getInjured(self, damage):
        if self.health - damage <= 0:
            self.die()
        else:
            self.health -= damage

    def age(self, current_day):
        age = current_day - self.day_spawned
        if age >= self.max_age:
            if random.random() < 0.6:
                self.die()
                return None
            self.current_age = age
            return age
        else:
            if random.random() < 0.02:
                self.die()
                return None
            else:
                if self.age >= self.mating_age:
                    self.mateable = True
                self.current_age = age
                return age


    def calculateSize(self):
        return self.size_mult * self.current_age

    def heal(self):
        if self.food_level == self.max_food and not self.poisoned:
            if self.health + self.healing_rate <= 100:
                self.health += self.healing_rate
            else:
                self.health = 100
        else:
            self.health -= self.healing_rate

