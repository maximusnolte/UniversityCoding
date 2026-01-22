class NutTree:
    def __init__(self, nut_type, age):
        self.nut_type = nut_type
        self.age = age  # in years
        self.nuts_collected = 0

    def grow(self):
        self.age += 1
        print(f"The {self.nut_type} "
              f"tree has grown older and is now {self.age} years old.")

    def collect_nuts(self, amount):
        self.nuts_collected += amount
        print(f"Collected {amount} {self.nut_type} "
              f"nuts. Total collected: {self.nuts_collected}")

    def __str__(self):
        return (f"{self.nut_type} "
                f"Tree - Age: {self.age}, "
                f"Nuts Collected: {self.nuts_collected}")