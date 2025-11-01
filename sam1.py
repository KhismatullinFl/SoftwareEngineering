class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
animal1 = Animal("Feline", "Cat")
print(animal1.family, animal1.name)