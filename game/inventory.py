from collections import Counter

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.inventory = []
            self.gold = 100                             # debug shit for real game prob set to like 15 or smth.
            self.HP = 100
            self.max_HP = 100
            self.gear = {
                'ring': None,
                'armor': None,
                'sword': None
            }
            armor = Item("Quilted Armor", "armor")
            sword = Item("Iron Shortsword", "sword")

            self.add_item(armor)
            self.add_item(sword)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped {item.name}.")
        else:
            print(f"{item.name} is not in your inventory.")

    def display_inventory(self):
        if not self.inventory:
            print("\nYour inventory is empty.")
        else:
            print("\nInventory:")
            item_counts = Counter(item.name for item in self.inventory)
            for item_name, count in item_counts.items():
                if count > 1:
                    print(f"- {item_name}: {count}")
                else:
                    print(f"- {item_name}")

    def count_items(self, item):
        count = sum(1 for i in self.inventory if i.name == item.name)
        return count
    
    def buy_item(self, item, cost, quantity):
        if self.gold >= quantity * cost:
            self.gold -= quantity * cost
            for _ in range(quantity):
                self.add_item(item)
            print(f"\nYou have purchased {quantity} {item.name} for {quantity * cost} gold coins.")
            item_amount = self.count_items(item)
        else:
            print("You don't have enough gold coins to make this purchase.")


    def change_gear(self, gear_type):
        if gear_type not in self.gear:
            print(f"Invalid gear type: {gear_type}")
            return

        if self.gear[gear_type] is not None:
            print(f"Current {gear_type.capitalize()}: {self.gear[gear_type].name}")
        else:
            print(f"\nNo {gear_type} equipped.")

        print(f"\nAvailable {gear_type.capitalize()} options:")
        
        matches = [item.name for item in self.inventory if item.description == gear_type]
        if not matches:
            print(f"You don't own any {gear_type}{'s' if gear_type in ['ring', 'sword'] else ''}")
            return
        else:
            for index, name in enumerate(matches, start=1):
                print(f"{index}. {name}")
            print(f"{index+1}. No {gear_type}")


        choice_valid = False
        selected_index = None

        while not choice_valid:
            selected_gear = input(f"Enter your choice (1-{index+1}): ")
            try:
                selected_index = int(selected_gear)
                if 1 <= selected_index <= index + 1:
                    choice_valid = True
                else:
                    print("Invalid gear selection. Please enter a valid choice.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if selected_index == index + 1:
            self.gear[gear_type] = None
            print(f"You have unequipped {gear_type}.")
        else:
            selected_item = next(item for item in self.inventory if item.name == matches[selected_index - 1] and item.description == gear_type)
            self.gear[gear_type] = selected_item
            print(f"You have equipped {selected_item.name} as your {gear_type}.")


player = Player()                       # is putting this here a bad idea? I dont want to accidently run it and then overide the old instance of player. It also probaly shouldnt be a global variable.