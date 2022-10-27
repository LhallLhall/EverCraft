import math
import random


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
            value = abilities[key] if (
                key in abilities) else self.DEFAULT_ABILITIES[key]
            a = Ability(key, value, Ability.MOD_VALUES[value])
            setattr(self, key, a)
        self.armor = 10 + (self.dexterity.modifier)
        self.hp = 5 + (self.constitution.modifier)
        if self.hp <= 0:
            self.hp = 1
        self.damage = 1 + (self.strength.modifier)
        self.crit = 2 + (self.strength.modifier * 2)
        self.is_dead = False
        self.atk_roll = self.strength.modifier + self.lvl // 2

    CHAR_HP = {
        'monk': 6,
        'fighter': 10,
        'paladin': 8,
        'rogue': 5
    }

    def attack(self, roll, target, cha_class):
        if cha_class == 'rogue' and target.dexterity.modifier > 0:
            roll2 = roll + self.atk_roll + target.dexterity.modifier
        else:
            roll2 = roll + self.atk_roll
        if roll == 20:
            if cha_class == 'paladin' and target.align == 'Evil':
                target.hp -= (2 + self.damage) * 3
            else:
                target.hp -= self.crit
            self.xp += 10
        elif roll2 >= target.armor:
            if cha_class == 'paladin' and target.align == 'Evil':
                target.hp -= 2
            target.hp -= self.damage
            self.xp += 10
        self.level_up(cha_class)
        if target.hp <= 0:
            target.is_dead = True

    def level_up(self, cha_class):
        if self.xp % 1000 == 0:
            self.lvl = (math.floor(self.xp/1000) + 1)
            if cha_class == 'monk':
                self.atk_roll = self.strength.modifier + self.lvl // 2 + self.lvl // 3
            if cha_class == 'fighter' or cha_class == 'paladin':
                self.atk_roll = self.strength.modifier + (self.lvl - 1)
            self.hp = self.hp + \
                (Character.CHAR_HP[cha_class] + self.constitution.modifier)


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
        self.atk_roll = self.strength.modifier + self.lvl // 2 + self.lvl // 3

    # gets 6 hp for every level ✅
    # does 3 dmg instead of 1 (without modifier) ✅
    # adds wisdom mod (only if positive) to the armor class + dex✅
    # attack roll is increased by 1 for every 2nd and 3rd lvl (2,4,6,8,10,12 && 3,6,9,12,15) ✅


class Fighter(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, **abilities)
        self.atk_roll = self.strength.modifier + (self.lvl - 1)

    # attack roll += 1 for every lvl instead of every other lvl✅
    # get 10 hp per lvl instead of 5✅
    pass


class Rogue(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, **abilities)
        self.damage = 1 + self.dexterity.modifier
        self.crit = self.damage * 3
        if self.align == 'Good':
            option = ['Neutral', 'Evil']
            print('you done messed up big boy!')
            self.align = random.choice(option)

            # triple dmg on crit✅
            # ignores dex mod on the armor (could possibly - the armor by the mod if its this class)✅
            # add dex mod to attack instead of strength✅
            # cant have good alignment✅
    pass


class Paladin(Character):
    def __init__(self, name, align, **abilities):
        super().__init__(name, align, **abilities)
        self.atk_roll = self.strength.modifier + (self.lvl - 1)
        if self.align != 'Good':
            self.align = 'Good'

    # starts with 8 hp instead of 5 ✅
    # +2 dmg to enemies when they are "evil" ✅
    # does triple damage when you crit on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)✅
    # attack roll += 1 for every lvl✅
    # can only have "Good" alignment✅
    pass
