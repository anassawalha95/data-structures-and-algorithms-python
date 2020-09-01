import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')

from data_structures_and_algorithms_python.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_brackets_1():
    str_val = '{}'
    expected = True
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_2():
    str_val = '{}(){}'
    expected = True
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_3():
    str_val = '()[[Extra Characters]]'
    expected = True
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_4():
    str_val = '(){}[[]]'
    expected = True
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_5():
    str_val = '{}{Code}[Fellows](())'
    expected = True
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_6():
    str_val = '[({}]'
    expected = False
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_7():
    str_val = '(]('
    expected = False
    actual = multi_bracket_validation(str_val)
    assert expected == actual

def test_brackets_8():
    str_val = '{(})'
    expected = False
    actual = multi_bracket_validation(str_val)
    assert expected == actual