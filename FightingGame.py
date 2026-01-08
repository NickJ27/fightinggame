import math
import random
def calculate_damage():
    
def fight(character_one, character_two):




#Intro
print("Welcome to the Fighting Game!")
character_one_name = input("Name character 1: ")
character_two_name = input("Name character 2: ")

#Random Stats
char_one_health = random.randint(25,35)
char_one_def = random.randint(1,4)
char_one_atk = random.randint(4,6)
char_two_health = random.randint(20,30)
char_two_def = random.randint(0,3)
char_two_atk = random.randint(5,7)

#Dictionary
character_one = {"name" : character_one_name, char_one_health, char_one_def, char_one_atk}
character_two = [character_two_name, char_two_health, char_two_def, char_two_atk]

#Print Stats
print(character_one[0], "will have", character_one[1], "health,", character_one[3], "atk, and", character_one[2], "defense.")
print(character_two[0], "will have", character_two[1], "health,", character_two[3], "atk, and", character_two[2], "defense.")

