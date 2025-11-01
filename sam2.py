class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
    def text(self):
        print(f"{self.name} belong to the {self.family} family")
animal1 = Animal("Feline", "Cat")
animal1.text()