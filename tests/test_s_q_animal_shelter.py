import pytest
from animal_shelter.animal_shelter import AnimalShelter, Animal


def test_enqueue():
    q = AnimalShelter()
    q.enqueue(Animal("Fluffy", "cat"))
    q.enqueue(Animal("Buddy", "dog"))
    q.enqueue(Animal("Tiger", "cat"))
    q.enqueue(Animal("Max", "dog"))
    assert (str(q), "cat-->dog-->cat-->dog--> None ")
    
def test_dequeue():
    q = AnimalShelter()
    Animal1 = Animal("pet", "dog")
    Animal2 = Animal("chanle", "cat")
    Animal3 = Animal("pug", "dog")
    Animal4 = Animal("pug", "dog")
    Animal5 = Animal("pug", "cat")
    q.enqueue(Animal1)
    q.enqueue(Animal2)
    q.enqueue(Animal3)
    q.enqueue(Animal4)
    q.enqueue(Animal5)
    assert str(q.dequeue(Animal5.species)) == "cat"
    assert str(q.dequeue(Animal4.species)) == "dog"


def test_dequeue_empty_queue():
    q = AnimalShelter()
    assert q.dequeue("dog") == "Empty queue"
    assert q.dequeue("cat") == "Empty queue"


