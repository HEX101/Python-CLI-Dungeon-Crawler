import csv
import random
import sys

def choose_random_item():
    with open('CSVs/rareItems.csv', 'r') as file:
        reader = csv.DictReader(file)
        items = list(reader)

        random_item = random.choice(items)
        return random_item
    
def next_room(room_num):            # I rlly should put this in dungeon.py it does no good here
    x = random.random()

    if room_num % 10 == 0:
        room_type = "Boss"
    elif room_num != 1 and x > 0.7:
        room_type = "Loot"
    else:
        room_type = "Monster"
    return room_type

def create_menu(title, options):
    while True:
        print("\n" + title)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option[0]}")
        choice = input(f"Enter your choice (1-{len(options)}): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1][1]
        
        print("Invalid choice. Please try again.")

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def quit_game():
    print("Thank you for playing Dungeon Explorers. Goodbye!")
    exit()