import random


def calculate_damage(attack, defense):
    """Return damage dealt given attack and defense values.

    Ensures at least 1 damage is dealt.
    """
    damage = attack - defense
    if damage < 1:
        damage = 1
    return damage


def print_result(attacker_name, defender_name, damage, defender_hp=None):
    """Print a descriptive result of an attack.

    If `defender_hp` is provided, include the defender's remaining HP.
    """
    if defender_hp is None:
        print(f"{attacker_name} attacks {defender_name} for {damage} damage!")
    else:
        remaining = max(defender_hp, 0)
        print(f"{attacker_name} attacks {defender_name} for {damage} damage! {defender_name} has {remaining} HP left.")


def fight(attacker, defender):
    """Perform one attack from `attacker` to `defender`.

    - Calls `calculate_damage` to compute damage.
    - Applies damage to `defender['hp']`.
    - Calls `print_result` to show what happened.
    Returns the damage done.
    """
    damage = calculate_damage(attacker['attack'], defender['defense'])
    defender['hp'] -= damage
    print_result(attacker['name'], defender['name'], damage, defender['hp'])
    return damage


def main():
    print("Welcome to the Fighting Game!")
    name1 = input("Name character 1: ")
    name2 = input("Name character 2: ")

    # Randomized stats stored in dictionaries
    character_one = {
        'name': name1,
        'hp': random.randint(25, 35),
        'attack': random.randint(4, 6),
        'defense': random.randint(1, 4)
    }

    character_two = {
        'name': name2,
        'hp': random.randint(20, 30),
        'attack': random.randint(5, 7),
        'defense': random.randint(0, 3)
    }

    print(f"{character_one['name']} will have {character_one['hp']} health, {character_one['attack']} atk, and {character_one['defense']} defense.")
    print(f"{character_two['name']} will have {character_two['hp']} health, {character_two['attack']} atk, and {character_two['defense']} defense.")

    attacker, defender = character_one, character_two
    round_num = 1
    while character_one['hp'] > 0 and character_two['hp'] > 0:
        print(f"\n--- Round {round_num} ---")
        fight(attacker, defender)
        if defender['hp'] <= 0:
            print(f"\n{defender['name']} has been defeated!")
            break
        # swap roles
        attacker, defender = defender, attacker
        round_num += 1

    winner = character_one if character_one['hp'] > 0 else character_two
    print(f"\n{winner['name']} wins the fight!")


if __name__ == '__main__':
    main()
