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


def print_text_with_typing_effect(text, typing_speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print("\n")
    time.sleep(1)

def startup():
    typing_speed = 0.05

    with open('other_files/story.txt', 'r') as file:
        story_text = file.read()

    print_text_with_typing_effect(story_text, typing_speed)

    show_cursor()
    camp_menu()