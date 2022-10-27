class Animal:
    att_mod = 4
    def __init__(self, legs, flies):
        self.leg = legs
        self.flies = flies
        self.has_fur = True

    def had_birthday(self):
        print(self.att_mod)

class Insect(Animal):
    att_mod = 6 # Insect.att_mod
    def __init__(self, l, bool):
        super().__init__(l, bool)
        self.leg = l * 2
        self.flies = bool


a = Animal(4, True)
i = Insect(6, False)
a.had_birthday() # Animal.had_birthday(a)
i.had_birthday() # Animal.had_birthday(i)