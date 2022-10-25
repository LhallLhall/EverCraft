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


