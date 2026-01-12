import random

#Functions
def calculate_damage(attacker, defender):
    damage = attacker["Attack"] - defender["Defense"]
    return damage

def print_result(attacker, defender, damage):
    print(attacker["Name"], "attacks", defender["Name"], "for", damage, "damage!")
    remaining = max(defender["HP"], 0)
    print(defender["Name"], "has", remaining, "HP left.")

def fight(attacker, defender):
    damage = calculate_damage(attacker, defender)
    defender["HP"] -= damage
    print_result(attacker, defender, damage)
    return damage

#Intro
print("Welcome to the Fighting Game!")
character_one_name = input("Name character 1: ")
character_two_name = input("Name character 2: ")

#Dictionary
character_one = {
        "Name": character_one_name,
        "HP": random.randint(55,65),
        "Attack": random.randint(6,11),
        "Defense": random.randint(3,5)
    }
character_two = {
        "Name": character_two_name,
        "HP": random.randint(40,52),
        "Attack": random.randint(8,12),
        "Defense": random.randint(5,8)
    }

#Print Stats
print("\n" + character_one["Name"], "will have", character_one["HP"], "HP,", character_one["Attack"], "attack,", character_one["Defense"], "defense.")
print(character_two["Name"], "will have", character_two["HP"], "HP,", character_two["Attack"], "attack,", character_two["Defense"], "defense.")
input("Press Enter to start the fight...")

#Game Start
round_num = 1
defender = character_one
attacker = character_two
while character_one["HP"] > 0 and character_two["HP"] > 0:
    print("\nRound:", round_num)
    fight(attacker, defender)
    if defender["HP"] <= 0:
        print("\n" + defender["Name"], "was deafeated!\n" + attacker["Name"], "wins!")
        break
    attacker, defender = defender, attacker
    round_num += 1
    input("Press Enter to continue...")