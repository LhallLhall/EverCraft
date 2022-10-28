from evercraft.evercraft import *


def test_do_classes_exist():
    assert Monk is not None


def test_class_inheritance():
    Travis = Monk('Travis', 'Neutral')
    assert Travis.hp == 5


def test_monk_damage():
    Travis = Monk('Travis', 'Neutral')
    Pete = Character('Pete', 'Evil')
    Travis.attack(12, Pete, 'monk')
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
    Travis.attack(15, Pete, 'monk')
    Travis.xp = 1990
    Travis.attack(15, Pete, 'monk')
    Travis.xp = 2990
    Travis.attack(15, Pete, 'monk')
    Travis.attack(15, Pete, 'monk')
    assert Travis.atk_roll == 5


def test_monk_roll_increase_every_2nd_3rd():
    Travis = Monk('travis', 'Good', strength=15, dexterity=10,
                  constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(15, Pete, 'monk')
    Travis.xp = 1990
    Travis.attack(15, Pete, 'monk')
    # assert Travis.lvl == 3
    assert Travis.atk_roll == 4


def test_fighter_roll_increase_every_lvl():
    Travis = Fighter('travis', 'Good', strength=15, dexterity=10,
                     constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(15, Pete, 'fighter')
    Travis.xp = 1990
    Travis.attack(15, Pete, 'fighter')
    Travis.xp = 2990
    Travis.attack(15, Pete, 'fighter')
    # assert Travis.lvl == 4
    assert Travis.atk_roll == 5


def test_rogue_crit_triple_dmg():
    Travis = Rogue('travis', 'Good', strength=15, dexterity=15,
                   constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=20, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(20, Pete, 'rogue')
    assert Pete.hp == 1


def test_rogue_added_dex_mod():
    Travis = Rogue('travis', 'Good', strength=10, dexterity=15,
                   constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=20, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(19, Pete, 'rogue')
    assert Pete.hp == 7


def test_rogue_cant_be_evil():
    Travis = Rogue('Travis', 'Good')
    assert Travis.align == 'Evil' or Travis.align == 'Neutral'


def test_rogue_ignores_target_dex():
    Travis = Rogue('travis', 'Good', strength=10, dexterity=10,
                   constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=15,
                     constitution=20, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(11, Pete, 'rogue')
    assert Pete.hp == 9


def test_paladin_does_extra_dmg():
    Travis = Paladin('travis', 'Good', strength=10, dexterity=10,
                     constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Evil', strength=18, dexterity=15,
                     constitution=20, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(19, Pete, 'paladin')
    assert Pete.hp == 7


def test_paladin_crit_on_evil():
    Travis = Paladin('travis', 'Good', strength=10, dexterity=10,
                     constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Evil', strength=18, dexterity=15,
                     constitution=20, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(20, Pete, 'paladin')
    assert Pete.hp == 1


def test_paladin_roll_increase_every_lvl():
    Travis = Paladin('travis', 'Good', strength=10, dexterity=10,
                     constitution=10, wisdom=17, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(15, Pete, 'paladin')
    Travis.xp = 1990
    Travis.attack(15, Pete, 'paladin')
    Travis.xp = 2990
    Travis.attack(15, Pete, 'paladin')
    assert Travis.atk_roll == 3


def test_paladin_cant_be_evil():
    Travis = Paladin('travis', 'Evil', strength=10, dexterity=10,
                     constitution=10, wisdom=17, intelligence=2, charisma=17)
    assert Travis.align == 'Good'


def test_monk_versus_fighter():
    Travis = Monk('travis', 'Good', dexterity=14, wisdom=14)
    Pete = Fighter('pete', 'Good')
    Travis.attack(19, Pete, 'monk')  # monk has 3 dmg instead of 1
    Pete.xp = 990
    # not supposed to hit monk armor also checking for 10 hp on lvl up
    Pete.attack(15, Travis, 'fighter')
    assert Pete.hp == 12
    assert Travis.damage == 3
    assert Travis.armor == 14


def test_paladin_vs_rogue():
    Travis = Paladin('Travis', 'Neutral', strength=12, dexterity=17)
    Pete = Rogue('Pete', 'Evil', dexterity=14)
    Travis.attack(15, Pete, 'paladin')
    assert Pete.hp == 1
    Pete.attack(10, Travis, 'rogue')
    assert Travis.hp == 2
    Travis.attack(20, Pete, 'paladin')
    assert Pete.hp == -11
    Pete.attack(20, Travis, 'rogue')
    assert Travis.hp == -7
    assert Travis.align == 'Good'
