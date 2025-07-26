import json
import os
import random

SAVE_FILE = 'game_save.json'

class Game:
    def __init__(self):
        self.rooms = {
            'forest': {
                'description': "You are in a dark forest. Paths lead north and east.",
                'exits': {'north': 'castle', 'east': 'lake'},
                'items': ['stick'],
                'enemy': None
            },
            'castle': {
                'description': "You stand before an old castle. There's a guard here!",
                'exits': {'south': 'forest'},
                'items': ['key'],
                'enemy': {'name': 'guard', 'hp': 10, 'attack': 3}
            },
            'lake': {
                'description': "A peaceful lake. You see a boat.",
                'exits': {'west': 'forest'},
                'items': [],
                'enemy': None
            }
        }
        self.location = 'forest'
        self.inventory = []
        self.hp = 20
        self.game_over = False

    def save_game(self):
        data = {
            'location': self.location,
            'inventory': self.inventory,
            'hp': self.hp
        }
        with open(SAVE_FILE, 'w') as f:
            json.dump(data, f)
        print("Game saved.")

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
                self.location = data.get('location', 'forest')
                self.inventory = data.get('inventory', [])
                self.hp = data.get('hp', 20)
            print("Game loaded.")
        else:
            print("No saved game found.")

    def describe_location(self):
        room = self.rooms[self.location]
        print("\n" + room['description'])
        if room['items']:
            print("You see: " + ", ".join(room['items']))
        if room['enemy']:
            print(f"A wild {room['enemy']['name']} is here!")

    def move(self, direction):
        room = self.rooms[self.location]
        if direction in room['exits']:
            self.location = room['exits'][direction]
            print(f"You move {direction} to the {self.location}.")
            self.describe_location()
            if self.rooms[self.location]['enemy']:
                self.combat(self.rooms[self.location]['enemy'])
        else:
            print("You can't go that way.")

    def take_item(self, item):
        room = self.rooms[self.location]
        if item in room['items']:
            self.inventory.append(item)
            room['items'].remove(item)
            print(f"You picked up {item}.")
        else:
            print("No such item here.")

    def combat(self, enemy):
        print(f"Combat starts with {enemy['name']}!")
        while enemy['hp'] > 0 and self.hp > 0:
            action = input("Attack (a) or run (r)? ").lower()
            if action == 'a':
                damage = random.randint(1, 6)
                enemy['hp'] -= damage
                print(f"You hit {enemy['name']} for {damage} damage.")
                if enemy['hp'] <= 0:
                    print(f"You defeated the {enemy['name']}!")
                    self.rooms[self.location]['enemy'] = None
                    break
                # Enemy attacks
                enemy_damage = random.randint(1, enemy['attack'])
                self.hp -= enemy_damage
                print(f"{enemy['name']} hits you for {enemy_damage} damage. Your HP: {self.hp}")
                if self.hp <= 0:
                    print("You have been defeated... Game Over!")
                    self.game_over = True
                    break
            elif action == 'r':
                print("You run away back to the forest.")
                self.location = 'forest'
                self.describe_location()
                break
            else:
                print("Invalid action.")

    def show_inventory(self):
        if self.inventory:
            print("Inventory: " + ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")

    def check_endings(self):
        # Example endings based on inventory & location
        if self.location == 'castle' and 'key' in self.inventory:
            print("\nYou unlock the castle gates with the key and find the treasure! You win!")
            self.game_over = True
        elif self.hp <= 0:
            print("\nYou have died. Game Over.")
            self.game_over = True

    def start(self):
        print("Welcome to the Text Adventure Game!")
        self.describe_location()
        while not self.game_over:
            command = input("\nEnter command (move/take/inventory/save/load/quit): ").lower().split()
            if not command:
                continue
            cmd = command[0]

            if cmd == 'move' and len(command) > 1:
                self.move(command[1])
            elif cmd == 'take' and len(command) > 1:
                self.take_item(command[1])
            elif cmd == 'inventory':
                self.show_inventory()
            elif cmd == 'save':
                self.save_game()
            elif cmd == 'load':
                self.load_game()
            elif cmd == 'quit':
                print("Goodbye!")
                break
            else:
                print("Unknown command.")

            self.check_endings()

if __name__ == "__main__":
    game = Game()
    game.start()
