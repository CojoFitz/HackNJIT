import random
import animals
import requests
from animals import Animals

animalsList = ['cat', 'dog', 'koala', 'fox', 'birb', 'red_panda', 'panda', 'racoon', 'kangaroo']

def FactsAndImages():
    userAnimal = ""
    while userAnimal not in animalsList:
        userAnimal = input("Please input an animal: ")
    animal = Animals(userAnimal)
    x = (animal.fact())
    y = (animal.image())
    return ("Random fact: " + x + "\n\n" + "Image Link: " + y)
       
print(FactsAndImages())
