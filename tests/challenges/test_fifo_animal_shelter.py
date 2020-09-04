import sys
sys.path.append('/home/aziz/401/data-structures-and-algorithms-python')
from data_structures_and_algorithms_python.challenges.fifo_animal_shelter.fifo_animal_shelter import Queue, AnimalShelter, Cat, Dog

def test_enqueu_cat_dog():
    animals = AnimalShelter()
    alex = Dog('alex')
    aln = Dog('Aln')
    soso = Cat('Soso')
    sno = Cat('Son')
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(soso)
    animals.enqueue(sno)

    expected = ('alex', 'Aln', 'Soso', 'Son')
    actual = alex.name ,aln.name, soso.name, sno.name
    assert expected == actual

def test_enqueu_any_value():
    animals = AnimalShelter()
    expected = 'You Should Add Cat or Dog Only'
    actual = animals.enqueue('any')
    assert expected == actual

def test_dequeue_cat():
    animals = AnimalShelter()
    alex = Dog('alex')
    aln = Dog('Aln')
    soso = Cat('Soso')
    sno = Cat('Son')
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(soso)
    animals.enqueue(sno)

    expected = 'Soso'
    actual = animals.dequeue('cat')
    assert expected == actual

def test_dequeue_dog():
    animals = AnimalShelter()
    alex = Dog('alex')
    aln = Dog('Aln')
    soso = Cat('Soso')
    sno = Cat('Son')
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(soso)
    animals.enqueue(sno)

    expected = 'alex'
    actual = animals.dequeue('dog')
    assert expected == actual

def test_dequeue_any():
    animals = AnimalShelter()
    aln = Dog('Aln')
    soso = Cat('Soso')
    animals.enqueue(aln)
    animals.enqueue(soso)

    expected = None
    actual = animals.dequeue('any')
    assert expected == actual
