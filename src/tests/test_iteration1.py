from evercraft.evercraft import Character

def test_character_there():
    assert Character is not None

def test_name_character():
    character1 = Character('Travis', 'Neutral')
    assert character1.name is not None

def test_alignment():
    character1 = Character('Travis', 'Neutral')
    assert character1.align is not None

def test_alignment_type():
    character1 = Character('Travis', 'Neutral')
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
    Travis.attack(9, Pete)
    assert Pete.hp is 5

def test_attack_is_there():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(20, Pete)
    assert Pete.hp is 3

def test_character_still_alive():
    Travis = Character('Travis', 'Neutral')
    assert Travis.is_dead == False

def test_can_character_die():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(20, Pete)
    Travis.attack(20, Pete)
    Travis.attack(15, Pete)
    assert Pete.is_dead == True

def test_child_abilities():
    Travis = Character('Travis', 'Neutral')
    assert Travis.strength == 13

def test_does_xp_exist():
    Travis = Character('Travis', 'Neutral')
    assert Travis.xp is not None

def test_will_xp_increase():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(12, Pete)
    assert Travis.xp == 10

def test_xp_more_than_once():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.attack(12, Pete)
    Travis.attack(17, Pete)
    Travis.attack(20, Pete)
    assert Travis.xp == 30

def test_is_level_there():
    Travis = Character('Travis', 'Neutral')
    assert Travis.lvl is not None

def test_if_char_lvl_up():
    Travis = Character('Travis', 'Neutral')
    Pete = Character('Pete', 'Neutral')
    Travis.xp = 2990
    Travis.attack(20, Pete)
    assert Travis.lvl is 4

def test_does_str_mod_exist():
    Travis = Character('Travis', 'Neutral')
    assert Travis.strength is not None
