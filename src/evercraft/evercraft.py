import math

class Ability:

# math.floor((level - 10) / 2)

    MOD_VALUES = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5,
    }
    def __init__(self, name, value, modifier):
        self.name = name
        self.value = value
        self.modifier = modifier


class Character:
    DEFAULT_ABILITIES = {
        'strength': 10,
        'dexterity': 10,
        'constitution': 10,
        'wisdom': 10,
        'intelligence': 10,
        'charisma': 10,
    }
    def __init__(self, name, align, **abilities):
        self.name = name
        self.align = align
        self.xp = 0 
        self.lvl = 1

        for key in self.DEFAULT_ABILITIES:
            # if_true if condition else if_false
            value = abilities[key] if (key in abilities) else self.DEFAULT_ABILITIES[key]
            a = Ability(key, value, Ability.MOD_VALUES[value])
            setattr(self, key, a)
        self.armor = 10 + (self.dexterity.modifier)
        self.hp = 5 + (self.constitution.modifier)
        if self.hp <= 0:
            self.hp = 1
        self.damage = 1 + (self.strength.modifier)
        self.crit = 2 + (self.strength.modifier * 2)
        self.is_dead = False

        # Abilities.__init__(self)
        # self.strength = Abilities.strength + 3

    def attack(self, roll, target):
        roll2 = roll + (self.strength.modifier)
        if roll == 20:
            target.hp -= self.crit
            self.xp += 10
            if self.xp % 1000 == 0:
                self.lvl = (math.floor(self.xp/1000) + 1)
                self.hp = self.hp + (5 + self.constitution.modifier)
        elif roll2 >= target.armor:
            target.hp -= self.damage
            self.xp += 10
            if self.xp % 1000 == 0:
                self.lvl = (math.floor(self.xp/1000) + 1)
                self.hp = self.hp + (5 + self.constitution.modifier)
        if target.hp <= 0:
            target.is_dead = True
    

# todo Overall Changes
# * there will be changes to health
# * there will be changes to attack roll and dmg
# * 

class Monk(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, **abilities)
        self.damage = 3 + (self.strength.modifier)
        if self.wisdom.modifier > 0:
            self.armor = 10 + (self.dexterity.modifier + self.wisdom.modifier)
        else:
            self.armor = 10 + (self.dexterity.modifier)
        
    # gets 6 hp for every level
    # does 3 dmg instead of 1 (without modifier) ✅
    # adds wisdom mod (only if positive) to the armor class + dex✅
    # attack roll is increased by 1 for every 2nd and 3rd lvl (2,4,6,8,10,12 && 3,6,9,12,15)

class Fighter(Character):
    # attack roll += 1 for every lvl instead of every other lvl
    # get 10 hp per lvl instead of 5
    pass

class Rogue(Character):
    # triple dmg on crit
    # ignores dex mod on the armor (could possibly - the armor by the mod if its this class)
    # add dex mod to attack instead of strength
    # cant have good alignment
    pass

class Paladin(Character):
    # starts with 8 hp instead of 5
    # +2 dmg to enemies when they are "evil"
    # does triple damage when you crit on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
    # attack roll += 1 for every lvl
    # can only have "Good" alignment
    pass