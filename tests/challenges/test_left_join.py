import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.challenges.left_join.left_join import left_join

def test_left_join_one():

    dec1 = {'fond':'enamored','warth':'anger','diligent':'employed',
        'outift':'garp','guide':'usher'}

    dec2 = {'fond':'averse','warth':'delight','diligent':'idle',
        'guide':'follow','flow':'jam'}
    
    expected = {'fond': ['enamored', 'averse'], 'warth': ['anger', 'delight'],
     'diligent': ['employed', 'idle'], 'outift': ['garp', None], 'guide': ['usher', 'follow']}

    assert expected == left_join(dec1,dec2)

def test_left_join_tow():

    dec1 = {'aziz':26,'saleh':24,}

    dec2 = {'aziz':'Abedalaziz Alhoot',}
    
    expected = {'aziz': [26, 'Abedalaziz Alhoot'], 'saleh': [24, None]}

    assert expected == left_join(dec1,dec2)

def test_left_join_three():

    dec1 = {'aziz':26,'saleh':24,}

    dec2 = {}

    expected = {'aziz': [26,None], 'saleh': [24, None]}

    assert expected == left_join(dec1,dec2)

def test_left_join_four():

    dec1 = {'aziz':26,'saleh':24}

    dec2 = {'Emad':24,'Dana':24}

    expected = {'aziz': [26, None], 'saleh': [24, None]}

    assert expected == left_join(dec1,dec2)

def test_left_join_five():
    
    dec1 = {}

    dec2 = {'Emad':24,'Dana':24}

    expected = {}

    assert expected == left_join(dec1,dec2)