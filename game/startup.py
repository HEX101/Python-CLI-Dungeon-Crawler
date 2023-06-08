import time
from game.camp import camp_menu
from game.helpers import create_menu, quit_game, hide_cursor, show_cursor

def main_menu():
    print("Welcome to Dungeon Explorers!")

    menu_title = "--- Main Menu ---"
    menu_options = [
        ("Load Save File", load_save_file),
        ("New Game", new_game_menu),
        ("Quit", quit_game)
    ]

    while True:
        selected_function = create_menu(menu_title, menu_options)
        if selected_function:
            selected_function()
        else:
            break

def load_save_file():
    # My desire to write the code for saving is non existent
    print("TODO")

def new_game_menu():
    menu_title = "\n--- New Game - Difficulty Selection ---"
    menu_options = [
    ("Adventurer - The easiest difficulty", lambda: new_game("Adventurer")),
    ("Heroic - Enemies have more HP and hit harder", lambda: new_game("Heroic")),
    ("Nightmare - Enemies have even more HP and hit even harder", lambda: new_game("Nightmare")),
    ]
    while True:
        selected_function = create_menu(menu_title, menu_options)
        if selected_function:
            selected_function()
        else:
            break

def new_game(difficulty):
    save_name = input("\nWhat is your name adventurer: ")                     # To be used for the save file name
    print(f"\nStarting a new game with difficulty: {difficulty}\n")
    time.sleep(1)
    hide_cursor()
    startup()

def startup():
    typingSpeed = 0.05

    intro_text = "In a land shrouded in mystery and danger,\n" \
                "a group of brave adventurers has gathered,\n" \
                "ready to embark on a perilous quest."          # Bullshit exposition that likely will go nowhere and probably should be moved into a TXT
    for char in intro_text:
        print(char, end='', flush=True)
        time.sleep(typingSpeed)

    time.sleep(1)
    print("\n")

    story_text = "Long ago, an ancient curse befell the realm,\n" \
                "plunging it into eternal darkness.\n" \
                "Legends speak of a powerful artifact hidden deep within\n" \
                "the treacherous depths of an ancient dungeon."

    for char in story_text:
        print(char, end='', flush=True)
        time.sleep(typingSpeed)

    time.sleep(1)
    print("\n")

    story_continued = "You and your fellow explorers have dedicated your lives\n" \
                    "to seeking out this artifact and lifting the curse.\n" \
                    "Armed with your wits, skills, and a burning determination,\n" \
                    "you now stand at the entrance of the fabled dungeon,\n" \
                    "ready to face the unknown."

    for char in story_continued:
        print(char, end='', flush=True)
        time.sleep(typingSpeed)

    time.sleep(1)
    print("\n")

    game_start_text = "Prepare to delve into the depths of the dungeon,\n" \
                    "where unimaginable dangers and untold treasures await!\n" \
                    "May fortune favor the bold!\n"
    for char in game_start_text:
        print(char, end='', flush=True)
        time.sleep(typingSpeed)

    time.sleep(1)
    show_cursor()
    camp_menu()