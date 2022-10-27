from evercraft.evercraft import *


def test_character_there():
    assert Character is not None


def test_name_character():
    character1 = Character('Travis', 'Neutral')
    assert character1.name is not None


def test_alignment():
    character1 = Character('Travis', 'Neutral')
    assert character1.align is not None


def test_alignment_type():
    # josh i hope you see this. we have zero clue how this works
    character1 = Character('Travis', 'Good')
    assert (character1.align is not 'Good') or (character1.align is not 'Evil')


def test_is_armor_there():
    character1 = Character('Travis', 'Neutral')
    assert character1.armor is not None


def test_armor_level():
    character1 = Character('Travis', 'Neutral')
    assert character1.armor == 10


def test_does_armor_have_hp():
    character1 = Character('Travis', 'Neutral')
    assert character1.hp is not None


def test_armor_hp_amount():
    character1 = Character('Travis', 'Neutral')
    assert character1.hp == 5


def test_attack():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(9, Pete, 'monk')
    assert Pete.hp is 5


def test_attack_is_there():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(20, Pete, 'monk')
    assert Pete.hp is 3


def test_character_still_alive():
    Travis = Character('Travis', 'Neutral')
    assert Travis.is_dead == False


def test_can_character_die():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(20, Pete, 'monk')
    Travis.attack(20, Pete, 'monk')
    Travis.attack(15, Pete, 'monk')
    assert Pete.is_dead == True

# def test_child_abilities():
#     Travis = Character('Travis', 'Neutral')
#     assert Travis.strength == 13


def test_does_xp_exist():
    Travis = Character('Travis', 'Neutral')
    assert Travis.xp is not None


def test_will_xp_increase():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(12, Pete, 'monk')
    assert Travis.xp == 10


def test_xp_more_than_once():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(12, Pete, 'monk')
    Travis.attack(17, Pete, 'monk')
    Travis.attack(20, Pete, 'monk')
    assert Travis.xp == 30


def test_is_level_there():
    Travis = Character('Travis', 'Neutral')
    assert Travis.lvl is not None


def test_if_char_lvl_up():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.xp = 2990
    Travis.attack(20, Pete, 'monk')
    assert Travis.lvl is 4


def test_does_str_mod_exist():
    Travis = Character('Travis', 'Neutral')
    assert Travis.strength is not None

# def test_check_if_abilities_are_there():
#     a = Abilities(12,9,20,4,17,12)
#     assert a.strength == 12

# def test_check_abilities_const():
#     a = Abilities(12,9,20,4,17,12)
#     assert a.constitution == 20

# def test_check_abilities_dex():
#     a = Abilities(12,9,20,4,17,12)
#     assert a.dexterity == 9

# def test_check_ability_int():
#     a = Abilities(12,9,20,4,17,12)
#     assert a.intelligence == 17

# def test_check_ability_wis():
#     a = Abilities(12,9,20,4,17,12)
#     assert a.wisdom == 4


def test_roll_to_set_strength():
    travis = Character('travis', 'Good', strength=15, dexterity=1,
                       constitution=1, wisdom=7, intelligence=2, charisma=17)
    assert travis.strength.value == 15


def test_does_mod_exist():
    travis = Character('travis', 'Good', strength=15, dexterity=1,
                       constitution=1, wisdom=7, intelligence=2, charisma=17)
    assert travis.strength.modifier == 2


def test_modify_armor():
    travis = Character('travis', 'Good', strength=15, dexterity=1,
                       constitution=1, wisdom=7, intelligence=2, charisma=17)
    assert travis.armor == 5


def test_modify_hp():
    travis = Character('travis', 'Good', strength=15, dexterity=1,
                       constitution=1, wisdom=7, intelligence=2, charisma=17)
    assert travis.hp == 1


def test_does_hp_mess_up():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Pete.attack(20, Travis, 'fighter')
    Pete.attack(20, Travis, 'fighter')
    assert Travis.hp == 1


def test_attack_does_dmg():
    Travis = Character('Travis', 'Good', strength=15, dexterity=1,
                       constitution=12, wisdom=7, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(19, Pete, 'monk')
    Travis.attack(19, Pete, 'monk')
    Pete.attack(19, Travis, 'fighter')
    # assert Travis.hp ==
    assert Pete.is_dead == True


def test_roll_gets_mod_by_str():
    Travis = Character('Travis', 'Good', strength=15, dexterity=1,
                       constitution=12, wisdom=7, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.attack(18, Pete, 'monk')
    assert Pete.hp == 1


def test_hp_increase_on_level():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.xp = 990
    Travis.attack(18, Pete, 'monk')
    assert Travis.hp == 11


def test_hp_math_is_good():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.xp = 990
    Pete.xp = 990
    Travis.attack(20, Pete, 'monk')
    Pete.attack(13, Travis, 'fighter')
    assert Pete.hp == 13


def test_fleshed_out_hp():
    Travis = Character('Travis', 'Good', strength=15, dexterity=1,
                       constitution=12, wisdom=7, intelligence=2, charisma=17)
    Pete = Character('Pete', 'Neutral', strength=18, dexterity=7,
                     constitution=9, wisdom=7, intelligence=19, charisma=15)
    Travis.xp = 990
    Travis.attack(9, Pete, 'monk')
    Travis.xp = 1990
    Travis.attack(12, Pete, 'monk')
    assert Travis.hp == 20
