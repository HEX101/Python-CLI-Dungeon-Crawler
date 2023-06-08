import csv
from game.inventory import Item, player
from game.constants import HEALING_POTION_COST, ARMOR_CSV, SWORDS_CSV
from game.helpers import create_menu


def shop():
    print("\nWelcome to the Shop!")

    menu_title = "\n--- Shopping Menu ---"
    menu_options = [
        ("Healing Potions", lambda: buy_healing_potions(player)),
        ("Swords", lambda: buy_gear("swords", SWORDS_CSV)),
        ("Armor", lambda: buy_gear("armor", ARMOR_CSV)),
        ("Exit", lambda: None),
        ]
    while True:
        selected_function = create_menu(menu_title, menu_options)
        if selected_function == menu_options[-1][1]:
            break
        selected_function()

def buy_healing_potions(player):
    healing_potion = Item("Healing Potion", "Restores health")

    quantity = int(input(f"\nHow many healing potions would you like to buy? Each one costs {HEALING_POTION_COST} gold coins and you have {player.gold} gold coins: "))
    player.buy_item(healing_potion, HEALING_POTION_COST, quantity)


def buy_gear(gear_type, gear_list_csv):
    print(f"\n{gear_type.capitalize()}:")
    gear_list = read_csv_file(gear_list_csv)
    if gear_list:
        print_gear_list(gear_list, gear_type)
        choice = input(f"Enter the number of the {gear_type} you want to buy (1-{len(gear_list)}), or enter 0 to go back: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(gear_list):
                selected_gear = gear_list[choice - 1]
                print("You have purchased the", selected_gear["name"], gear_type + ".")
                # Add logic to add to inv ect
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")
    else:
        print(f"No {gear_type} available at the moment.")

def print_gear_list(gear_list, gear_type): 
    for index, gear in enumerate(gear_list, start=1):
        print(f"{index}. {gear['name']}")

def read_csv_file(filename):
    data = []
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        print("Error: {} file not found.".format(filename))
    return data

def print_sword_list(swords):
    for i, sword in enumerate(swords, start=1):
        print(f"{i}. {sword['name']} - Damage: {sword['damage']}")
        print(f"{sword['description']}\n")

def print_armor_list(armor):
    for i, item in enumerate(armor, start=1):
        print(f"{i}. {item['name']} - Defense: {item['defense']}")