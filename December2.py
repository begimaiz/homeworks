class Animal:
    def __init__(self, name):
        self.name = name
        self.extinct = False
        self.weight = 0
        self.colours = []

    def set_extinct(self, is_extinct):
        self.extinct = is_extinct

    def set_weight(self, weight):
        self.weight = weight

    def set_colours(self, colours):
        self.colours = colours

    def get_characteristics(self):
        return self.extinct, self.weight, self.colours


class Vertebrate(Animal):
    def __init__(self, name,  number_of_vertebrates):
        super().__init__(name)
        self.number_of_vertebrates = number_of_vertebrates

    def set_number_of_vertebrates(self, number_of_vertebrates):
        self.number_of_vertebrates = number_of_vertebrates

    def get_characteristics(self):
        return self.extinct, self.weight, self.colours, self.number_of_vertebrates


class Invertebrate(Animal):
    pass


class Mammal (Vertebrate):
    def __init__(self, name,  number_of_vertebrates=None, number_of_nipples=None):
        super().__init__(name,  number_of_vertebrates)
        self.number_of_nipples = number_of_nipples

    def set_number_of_nipples(self, number_of_nipples):
        self.number_of_nipples = number_of_nipples

    def get_characteristics(self):
        return self.name, self.extinct, self.weight, self.colours, self.number_of_vertebrates, self.number_of_nipples


def create_animal():
    Mammal1 = Mammal('Cat', 42, 2)
    Mammal1.set_weight(52)
    Mammal1.set_number_of_nipples(8)
    Mammal1.set_colours(['white', 'black'])
    Mammal1.set_extinct(False)
    Mammal1.set_number_of_vertebrates(30)
    Mamal2 = Mammal('dog')
    print(Mammal1.get_characteristics())
    print(Mamal2.get_characteristics())
