import random
import animals
import requests
import matplotlib
from animals import Animals

animalsList = ['cat', 'dog', 'koala', 'fox', 'birb', 'red_panda', 'panda', 'racoon', 'kangaroo']
deasy={'cat': [["How many paws does a cat have?", "4"], ["Does cats have night vision?", "yes"]], 'dog': [["How many paws does a dog have?", "4"],["What is a dog's best sense? (taste, smell, vision, hearing, touch)", "smell"]], 'koala': [["What country has koalas?", "australia"], ["What food does a koala eat? (eucalypt leaves or bamboo)", "eucalypt leaves"]], 'fox': [["What was the name of the fox in Dora?", "swiper"], ["Do foxes have whiskers?", "yes"]], 'panda': [["What continent does pandas reside in?", "asia"], ["What do pandas eat?", "bamboo"]], 'racoon': [["How many paws does a racoon have?", "4"], ["Does raccoons have fur?", "yes"]], 'kangaroo': [["What country has kangaroos?", "australia"], ["Does kangaroos have pouches?", "yes"]]} 
dhard={'cat': [["A group of cats is called a", "clowder"], ["How many chromosomes does a cat have?", "38"]], 'dog': [["How many times better are dog's sense of smell compared to humans?", "40"], ["How many chromosomes does a dog have?", "78"]], 'koala': [["What colors are koalas?", "grey"], ["Are koalas carnivores or herbivores?", "herbivores"]], 'fox': [["Are foxes omnivores, herbivores, or carnivores?", "omnivores"], ["What genus does foxes belong to?", "vulpes"]], 'panda': [["What is the average weight of a panda? (200lb, 5lb, 2000lb)", "200lb"], ["What is the typical habitat of a panda?", "forest"]], 'racoon': [["Are racoons social animals?", "no"], ["Are racoons nocturnal?", "yes"]], 'kangaroo': [["Are kangaroos are the largest marsupials on earth?", "yes"], ["A group of kangaroos is called", "mob"]]}
nums = [0,1]
def Trivia():
    userDiff = input("Enter easy for easy and hard for hard: ")
    userAnimal = input("Please input an amimal: ")
    if userDiff == "easy" or userDiff == "Easy":
        randNum = random.choice(nums)
        compQuestion = deasy[userAnimal][randNum][0]
        print(compQuestion)
        compAnswer = input("Answer: ")
        if compAnswer == deasy[userAnimal][randNum][1]:
            return "Nice Job"
        else:
            return("Better luck next time, The answer is " + deasy[userAnimal][randNum][1])
    elif userDiff == "hard" or userDiff == "Hard":
        randNum = random.choice(nums)
        compQuestion = dhard[userAnimal][randNum][0]
        print(compQuestion)
        compAnswer = input("Answer: ")
        if compAnswer == dhard[userAnimal][randNum][1]:
            return "Nice Job"
        else:
            return("Better luck next time, The answer is " + dhard[userAnimal][randNum][1])
    else:
        return "Invalid Input"
    
Trivia()
