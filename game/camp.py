from game.shop import shop
from game.dungeon import enter_dungeon
from game.helpers import create_menu
from game.inventory import player, Player

def camp_menu():

    print("Welcome to the Camp!")

    menu_title = "\n--- Camp Menu ---"
    menu_options = [
        ("Enter Dungeon", enter_dungeon),
        ("Gear", gear_menu),
        ("Inventory", Player().display_inventory),
        ("Shop", shop),
        ("Save and Exit to Main Menu", save_and_exit)
    ]
    while True:
        selected_function = create_menu(menu_title, menu_options)
        selected_function()
            
def gear_menu():

    menu_title = "\n--- Gear Menu ---"
    menu_options = [
        ("Change Armor", lambda: player.change_gear("armor")),
        ("Change Ring", lambda: player.change_gear("ring")),
        ("Change Sword", lambda: player.change_gear("sword")),
        ("Exit Gear Menu", lambda: False),
    ]
    while True:
        selected_function = create_menu(menu_title, menu_options)
        if selected_function == menu_options[-1][1]:
            break
        selected_function()

def save_and_exit():
    # save_game_state()                     # Placeholder function
    return False