
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
        self.front = None
        self.back = None
        self.dogs = []
        self.cats = []

    def is_empty(self):
        """
        Checks whether the shelter is empty.

        Returns:
            bool: True if the shelter is empty, False otherwise.
        """
        return self.front is None 
          
    def enqueue(self, animal):
        """
        Adds an animal to the shelter's queue.

        Args:
            animal (Animal): The animal to add to the queue.

        Returns:
            list: The list of animals of the same species as the added animal (either self.dogs or self.cats).
                  Returns an error message if the animal's species is not 'dog' or 'cat'.
        """
        if animal.species == 'dog':
            self.dogs.append(animal.species)
            return self.dogs

        elif animal.species == 'cat':
            self.cats.append(animal.species)
            return self.cats

        else :
            return "You should only use : dog , cat"

           

    def dequeue(self, value):
        """
        Removes an animal from the shelter's queue.

        Args:
            value (str): The species of the animal to remove ('dog' or 'cat').

        Returns:
            Animal or None: The removed animal (the oldest animal of the requested species),
                            or None if no animal of the requested species is found.
        """
        if value != self.dogs[0] and value != self.cats[0]:
            return None
        
        elif value == self.dogs[0]:
            return self.dogs.pop(0)
        
        elif value == self.cats[0]:
            return self.cats.pop(0)
        
    def __str__(self):
        output = "None"
        if self.front is not None:
            output = f"[{self.front.species}]"
            current = self.front.next
            while current is not None:
                output += f"<-[{current.species}]"
                current = current.next
        dog_len = len(self.dogs)
        cat_len = len(self.cats)
        if dog_len == cat_len:
            for i in range(dog_len):
                output += f"<-[{self.dogs[i]}]<-[{self.cats[i]}]"
        elif dog_len > cat_len:
            for i in range(cat_len):
                output += f"<-[{self.dogs[i]}]<-[{self.cats[i]}]"
            for i in range(cat_len, dog_len):
                output += f"<-[{self.dogs[i]}]"
        else:
            for i in range(dog_len):
                output += f"<-[{self.dogs[i]}]<-[{self.cats[i]}]"
            for i in range(dog_len, cat_len):
                output += f"<-[{self.cats[i]}]"
        return output


    
Animal1 = Animal("pet", "dog")
Animal2 = Animal("chanle", "cat")
Animal3 = Animal("pug", "dog")

al=AnimalShelter()
print(al.enqueue(Animal1))
print(al.enqueue(Animal2))
print(al.enqueue(Animal3))
print(al)
print(al.dequeue(Animal3.species))
print(al)
Animal4 = Animal("pug", "cat")
print(al.enqueue(Animal4))
print(al)





     

