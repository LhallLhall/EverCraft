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
    Travis = Monk('travis', 'Good', strength=15, dexterity=1, constitution=1, wisdom=7, intelligence=2, charisma=17)
    assert Travis.armor == 5

def test_wisdom_increases_armor():
    Travis = Monk('travis', 'Good', strength=15, dexterity=10, constitution=1, wisdom=17, intelligence=2, charisma=17)
    assert Travis.armor == 13