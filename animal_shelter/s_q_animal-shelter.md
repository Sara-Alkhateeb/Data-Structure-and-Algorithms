# Code Challenge: Class-12
# stack-and-queue 
### Problem Domain

The problem domain is it to  creating queue that will make an enqueue for element , then the dequeue will take an argument from the object to dequeue certain element from the queue.  

A queue is a First-In-First-Out (FIFO) data structure in which the first element added is the first one to be removed. The main operations performed on a queue are enqueue (add an element to the back) and dequeue (remove the front element). Other common operations include peek (return the front element without removing it) and isEmpty (check if the queue is empty).


## Whiteboard Process
![cc](../assest/wh12.png)

## Approach & Efficiency
## 1. Algorithm :
1. Creat Animal class that has initializer for the name and species to make object that will be used as an argument.
2. Creat Animalshelter class that has initializer, Enqueue , dequeue and str: 
  a. Enqueue: Create a list that will take animal.species by append it.
  b. Dequeue: Creat a for loop to pop the first animal.species that chosen ,  in addition to that there is two condition to handle the edge cases.
  c. str : creat function that will format the result.  


## 2. BigO
Here are the time complexity (big O) for various operations related queues:
enqueue: O(1)
dequeue: O(n)
str: O(n)

Here are the space complexity (big O) for various operations related to queues:
enqueue: O(n)
dequeue: O(n)
str: O(n)



## Solution
### [click here to the stack and queues code](./animal_shelter.py)
### [click here to the Test code](../tests/test_s_q_animal_shelter.py)

## Test Cases

      INPUT: Al.enqueue(cat)
             Al.enqueue(dog)
             Al.enqueue(cat)
             Al.dequeue(dog)

      OUTPUT : null<-- “cat” <-- “cat”

      INPUT: Al.dequeue(dog)
      OUTPUT: None 

      INPUT:  Al.enqueue(cat)
              Anl.dequeue(dog)
      OUTPUT: None 


### To run the code:
    -on your terminal follow these command:
       1. source .venv/bin/activate.
       2. pip install pytest.
       3. pytest.