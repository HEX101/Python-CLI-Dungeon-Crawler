import random
import time
from game.helpers import next_room, create_menu
from game.inventory import player


def enter_dungeon():
    player_health = 100
    room_num = 0

    print("\nEntering the Dungeon...")
    time.sleep(1)
    print("You venture deep into the dark and treacherous dungeon.")

    continue_in_dungeon(player_health, room_num)


def handle_boss(player_health):
    print("You killed the boss")

def handle_loot(room_num):
    gold_found = (random.randint(10, 20)) 
    gold_found += round(gold_found * (room_num / 50))
    print(f"You found {gold_found} gold coins")
    player.gold += gold_found

def handle_monster(player_health):
    print("You killed the monster")

def post_fight(player_health, room_num):
    print(f"Your current health: {player_health}")

    menu_title = "\n--- Post Fight Menu ---"
    menu_options = [
        ("Enter Next Room", lambda: continue_in_dungeon(player_health, room_num)),
        ("Use an Item", use_item),
        ("Leave the dungeon", lambda: None),
    ]
    while True:
        selected_function = create_menu(menu_title, menu_options)
        if selected_function == menu_options[-1][1]:
            break
        selected_function()

def continue_in_dungeon(player_health, room_num):
    while True:
        room_num += 1
        room_type = next_room(room_num)
        if room_type == "Boss":
            print("\nYou have encountered a fearsome Boss!")
            handle_boss(player_health)
        elif room_type == "Loot":
            print("\nYou have found a room filled with valuable Loot!")
            handle_loot(room_num)
        else:
            print("\nYou have encountered a fierce Monster!")
            handle_monster(player_health)

        if not post_fight(player_health, room_num):
            break

def use_item():                 # Placeholder function
    print("TODO")