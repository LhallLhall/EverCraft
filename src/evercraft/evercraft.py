import math

class Abilities:
    def __init__(self, stre, dex, const, wis, inte, cha):
        self.strength = stre
        self.dexterity = dex
        self.constitution = const
        self.wisdom = wis
        self.intelligence = inte
        self.charisma = cha

class Character(Abilities):
    def __init__(self, name, align):
        self.name = name
        self.align = align
        self.xp = 0 
        self.lvl = 1
        self.armor = 10
        self.hp = 5
        self.is_dead = False
        # Abilities.__init__(self)
        # self.strength = Abilities.strength + 3

    def attack(self, roll, target):
        if roll == 20:
            target.hp -= 2
            self.xp += 10
            if self.xp % 1000 == 0:
                self.lvl = (math.floor(self.xp/1000) + 1)
        elif roll >= target.armor:
            target.hp -= 1
            self.xp += 10
        if target.hp <= 0:
            target.is_dead = True
    