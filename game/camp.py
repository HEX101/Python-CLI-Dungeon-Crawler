from game.shop import shop
from game.dungeon import enter_dungeon
from game.helpers import create_menu, BreakOutException
from game.inventory import player, Player

def camp_menu():

    print("Welcome to the Camp!")

    menu_title = "\n--- Camp Menu ---"
    menu_options = [
        ("Enter Dungeon", enter_dungeon),
        ("Gear", gear_menu),
        ("Inventory", Player().display_inventory),
        ("Shop", shop),
        ("Save and Exit to Main Menu", None)
    ]
    while True:
        selected_function = create_menu(menu_title, menu_options)
        if selected_function:
            selected_function()

        elif selected_function == None:
            # Saving logic

            raise BreakOutException()               # kinda a hack I think but I couldnt find a better way of doing it

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
