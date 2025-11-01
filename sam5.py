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
        
class NicknameAnimal(Animal):
    def __init__(self, family, name, nickname):
        super().__init__(family, name)
        self.nickname = nickname

    def text2(self):
        print(f" This {self.name} of the {self.family} family has the nickname {self.nickname}")
       
animal1 = ColorAnimal("Feline", "Cat", "Black")
animal1.text()
animal1.text2()
animal2 = NicknameAnimal("Feline", "Cat", "Ryzhyk")
animal2.text()
animal2.text2()