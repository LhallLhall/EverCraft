class Abilities:
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10

class Character(Abilities):
    def __init__(self, name, align):
        self.name = name
        self.align = align
        self.armor = 10
        self.hp = 5
        self.is_dead = False
        Abilities.__init__(self)
        self.strength = Abilities.strength + 3

    def attack(self, roll, target):
        if roll == 20:
            target.hp -= 2
        elif roll > target.armor:
            target.hp -= 1
        if target.hp <= 0:
            target.is_dead = True
    