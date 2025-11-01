class Animal:
    def __init__(self, family, name):
        self.family = family
        self.name = name
    def text(self):
        print(f"{self.name} belong to the {self.family} family")

class ColorAnimal(Animal):
    def __init__(self, family, name, color):
        super().__init__(family, name)
        self.color = color

    def text2(self):
        print(f" This {self.name} of the {self.family} family is {self.color} in color")
        
animal1 = ColorAnimal("Feline", "Cat", "Black")
animal1.text()
animal1.text2()