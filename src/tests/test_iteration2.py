from evercraft.evercraft import *


def test_do_classes_exist():
    assert Monk is not None


def test_class_inheritance():
    Travis = Monk('Travis', 'Neutral')
    assert Travis.hp == 5


def test_monk_damage():
    Travis = Monk('Travis', 'Neutral')
    Pete = Character('Pete', 'Evil')
    Travis.attack(12, Pete)
    assert Pete.hp == 2


def test_wisdom_mods_armor():
    Travis = Monk('travis', 'Good', strength=15, dexterity=1,
                  constitution=1, wisdom=7, intelligence=2, charisma=17)
    assert Travis.armor == 5


def test_wisdom_increases_armor():
    Travis = Monk('travis', 'Good', strength=15, dexterity=10,
                  constitution=1, wisdom=17, intelligence=2, charisma=17)
    assert Travis.armor == 13


def test_class_based_lvl_up():
    Travis = Monk('travis', 'Good', strength=15, dexterity=10,
                  constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(15, Pete, 'monk')
    assert Travis.hp == 11


def test_class_based_lvl_up_paladin():
    Travis = Monk('travis', 'Good', strength=15, dexterity=10,
                  constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(15, Pete, 'paladin')
    assert Travis.hp == 13


def test_does_atk_roll_increase():
    Travis = Monk('travis', 'Good', strength=15, dexterity=10,
                  constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(15, Pete, 'paladin')
    Travis.xp = 1990
    Travis.attack(15, Pete, 'paladin')
    Travis.xp = 2990
    Travis.attack(15, Pete, 'paladin')
    Travis.attack(15, Pete, 'paladin')
    assert Travis.atk_roll == 4
