class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self._age = age  # Encapsulated
        self.sound = "Generic animal sound"
        self.habitat = "Unknown"

    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        print(f"{self.name} is moving.")

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, new_age):
        if new_age < 0:
            print("Age cannot be negative.")
        else:
            self._age = new_age


class Mammal(Animal):
    def __init__(self, name, species, age, fur_color, num_legs):
        super().__init__(name, species, age)
        self.fur_color = fur_color
        self.num_legs = num_legs

    def give_birth(self):
        print(f"{self.name} gives birth to live young.")

    def lactate(self):
        print(f"{self.name} is lactating.")


class Bird(Animal):
    def __init__(self, name, species, age, wing_span, can_fly):
        super().__init__(name, species, age)
        self.wing_span = wing_span
        self.can_fly = can_fly

    def lay_eggs(self):
        print(f"{self.name} lays eggs.")

    def fly(self):
        print(f"{self.name} is flying.")


class Reptile(Animal):
    def __init__(self, name, species, age, scale_type, is_cold_blooded):
        super().__init__(name, species, age)
        self.scale_type = scale_type
        self.is_cold_blooded = is_cold_blooded

    def lay_eggs(self):
        print(f"{self.name} lays eggs.")

    def bask_in_sun(self):
        print(f"{self.name} is basking in the sun.")



# Example usage
if __name__ == "__main__":
    lion = Mammal("Simba", "Lion", 5, "Golden", 4)
    eagle = Bird("Eddie", "Eagle", 3, 180, True)
    snake = Reptile("Slither", "Snake", 2, "Smooth", True)

    animals = [lion, eagle, snake]

    for animal in animals:
        print(f"\n{animal.name} ({animal.species}):")
        animal.make_sound()
        animal.eat()
        animal.sleep()
        animal.move()

        if isinstance(animal, Mammal):
            animal.give_birth()
            animal.lactate()
            
        elif isinstance(animal, Bird) or isinstance(animal, Reptile):
            animal.lay_eggs()

        # Access and modify age using getter and setter
        print(f"{animal.name} is {animal.get_age()} years old.")
        animal.set_age(animal.get_age() + 1)
        print(f"{animal.name} is now {animal.get_age()} years old.")

    print("\nPolymorphism Example:")
    for animal in animals:
        animal.make_sound()
