import json
import random
from functools import wraps
import os

# Decorator: save game after each move
def save_progress(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.save_game()
        return result
    return wrapper

class InvalidChoiceError(Exception):
    pass

class Player:
    def __init__(self, name, health=100, inventory=None, current_scene='start'):
        self.name = name
        self.health = health
        self.inventory = inventory or []
        self.current_scene = current_scene

class Scene:
    def __init__(self, id, description, choices, enemy=None, loot=None):
        self.id = id
        self.description = description
        self.choices = choices  # dict: choice_text -> next_scene_id
        self.enemy = enemy  # tuple like (name, damage)
        self.loot = loot or []  # list of items

class Game:
    def __init__(self, scenes_file='scenes.json', save_file='savegame.json'):
        self.scenes: dict[str, Scene] = {}
        self.load_scenes(scenes_file)
        self.save_file = save_file
        self.player: Player = None

    def load_scenes(self, fname):
        with open(fname, 'r', encoding='utf‑8') as f:
            data = json.load(f)
        for sid, info in data.items():
            self.scenes[sid] = Scene(sid, info['description'], info['choices'], info.get('enemy'), info.get('loot'))

    def new_game(self, player_name):
        self.player = Player(player_name)

    def load_game(self):
        if not os.path.exists(self.save_file):
            print("No save file found.")
            return False
        with open(self.save_file, 'r', encoding='utf‑8') as f:
            d = json.load(f)
        self.player = Player(d['name'], d['health'], d['inventory'], d['current_scene'])
        print(f"Loaded game for {self.player.name}")
        return True

    def save_game(self):
        state = {
            'name': self.player.name,
            'health': self.player.health,
            'inventory': self.player.inventory,
            'current_scene': self.player.current_scene
        }
        with open(self.save_file, 'w', encoding='utf‑8') as f:
            json.dump(state, f)
        print("[Game saved]")

    @save_progress
    def move(self, choice_text):
        scene = self.scenes[self.player.current_scene]
        if choice_text not in scene.choices:
            raise InvalidChoiceError("Invalid choice.")
        print(f"\n→ {choice_text}")
        next_id = scene.choices[choice_text]
        self.player.current_scene = next_id
        self.process_scene()

    def process_scene(self):
        scene = self.scenes[self.player.current_scene]
        print(f"\n{scene.description}")
        # optional fight
        if scene.enemy:
            name, dmg = scene.enemy
            print(f"You encounter a {name}! It hits you for {dmg} damage.")
            self.player.health -= dmg
            print(f"Your health: {self.player.health}")
        # optional loot generator
        if scene.loot:
            for item in self.loot_generator(scene.loot):
                self.player.inventory.append(item)
                print(f"You find loot: {item}")
        if self.player.health <= 0:
            print("You died! Game over.")
            exit()

    def display_choices(self):
        scene = self.scenes[self.player.current_scene]
        for idx, ch in enumerate(scene.choices, 1):
            print(f"{idx}. {ch}")

    def loot_generator(self, loot_list):
        for item in loot_list:
            yield item

    def play(self):
        print(f"Welcome, {self.player.name}! Adventure begins...\n")
        while True:
            scene = self.scenes[self.player.current_scene]
            self.process_scene()
            if not scene.choices:
                print("The End!")
                break
            print("\nWhat do you do?")
            self.display_choices()
            inp = input("> ").strip()
            try:
                idx = int(inp) - 1
                choice = list(scene.choices.keys())[idx]
                self.move(choice)
            except (ValueError, IndexError, InvalidChoiceError) as e:
                print("Invalid input. Choose again.")

if __name__ == "__main__":
    game = Game()
    if not game.load_game():
        name = input("Enter your name: ")
        game.new_game(name)
    game.play()
