import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')

from data_structures_and_algorithms_python.data_structures.hashtable.hashtable import HashTable

def test_add_key_vlaue():
    table = HashTable()
    table.set('listen','listen value')

    expected = ('listen','listen value')
    actual = table.map[table.hash('listen')].head.value
    assert expected == actual


def test_retrive_vlaue():
    table1 = HashTable()
    table1.set('listen','listen value')

    expected = 'listen value'
    actual = table1.get('listen')
    assert expected == actual


def test_return_none():
    table1 = HashTable()
    table1.set('listen','listen value')

    expected = None
    actual = table1.get('aziz')
    assert expected == actual

def test_collision():
    table = HashTable()
    table.set('listen','listen value')
    table.set('silent','silent value')

    expected = ('listen','listen value')
    actual = table.map[table.hash('listen')].head.value

    expected2 = ('silent','silent value')
    actual2 = table.map[table.hash('silent')].head.next.value

    assert expected == actual
    assert expected2 == actual2


def test_retrive_value_from_bucket_collision():
    table = HashTable()
    table.set('listen','listen value')
    table.set('silent','silent value')

    expected = 'listen value'
    actual = table.get('listen')

    expected2 = 'silent value'
    actual2 = table.get('silent')

    assert expected == actual
    assert expected2 == actual2

def test_hash():
    table = HashTable()
    expcted = 157
    actual = table.hash('silent')

    assert expcted == actual

def test_contain():
    table = HashTable()
    table.set('silent','silent value')

    expected = True
    actual = table.contain('silent')

    expected = False
    actual = table.contain('saleh')

    assert expected == actual