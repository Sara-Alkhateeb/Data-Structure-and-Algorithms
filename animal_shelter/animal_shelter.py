class Animal():
    """
    A class representing an animal.

    Attributes:
        name (str): The name of the animal.
        species (str): The species of the animal ('dog' or 'cat').
    """
    def __init__(self, name, species):
        """
        Initializes an Animal instance.

        Args:
            name (str): The name of the animal.
            species (str): The species of the animal ('dog' or 'cat').
        """
        self.name = name
        self.species= species
            
class AnimalShelter():
    """
    A class representing an animal shelter that can enqueue and dequeue dogs and cats.

    Attributes:
        front (NoneType or Animal): The front of the shelter's queue.
        back (NoneType or Animal): The back of the shelter's queue.
        dogs (list): A list of dogs in the shelter.
        cats (list): A list of cats in the shelter.
    """
    def __init__(self):
        """
        Initializes an AnimalShelter instance.
        """
        self.cats_dogs = []
        
          
    def enqueue(self, animal):
        """
        Adds an animal to the shelter's queue.

        Args:
            animal (Animal): The animal to add to the queue.

        Returns:
            list: The list of animals of the same species as the added animal (either self.dogs or self.cats).
                  Returns an error message if the animal's species is not 'dog' or 'cat'.
        """
        self.cats_dogs.append(animal.species)   
        return (animal.species)

    def dequeue(self, value):
        """
        Removes an animal from the shelter's queue.

        Args:
            value (str): The species of the animal to remove ('dog' or 'cat').

        Returns:
            Animal or None: The removed animal (the oldest animal of the requested species),
                            or None if no animal of the requested species is found.
        """
        if len(self.cats_dogs) == 0 :
            return "Empty queue" 
        if value != "dog" and value != "cat":
            return None
        
        if value == self.cats_dogs[0]:
            return self.cats_dogs.pop(0)
        
        for i in range (len(self.cats_dogs)):
            if value == self.cats_dogs[i]:
             return self.cats_dogs.pop(i) 

        
        
    def __str__(self):
    # Format for the output in queue way   
        if len(self.cats_dogs) == 0:
            return 'None'
        
        cats_dog_str = '-->'.join([animal for animal in self.cats_dogs])
        return cats_dog_str + "--> None "
    

    
Animal1 = Animal("pet", "dog")
Animal2 = Animal("chanle", "cat")
Animal3 = Animal("pug", "dog")
Animal4 = Animal("pug", "dog")
Animal5 = Animal("pug", "dog")
Animal6 = Animal("pug", "cat")
al=AnimalShelter()
print(al.enqueue(Animal1))
print(al.enqueue(Animal2))
print(al.enqueue(Animal3))
print(al.enqueue(Animal4))
print(al.enqueue(Animal6))
print(al)
print(al.dequeue(Animal6.species))
print(al)
al.enqueue(Animal5)
print(al)





     

