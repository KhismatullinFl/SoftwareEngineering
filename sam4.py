class Animal:
    def __init__(self, family, name):
        self._family = family
        self.__name = name
    def text(self):
        print(f"{self.__name} belong to the {self._family} family")
animal1 = Animal("Feline", "Cat")
print(animal1._family)
animal1.text()