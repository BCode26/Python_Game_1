import json
import main

def File_Change(main.save_slot):
    with open("game_data.json", encoding="utf-8") as file:
        game_data = json.load(file)

    with open("character.json", encoding="utf-8") as file:
        character_data = json.load(file)

    if main.load == 1 or main.save_slot == 1:
        save_slot = 0
    elif main.load == 2 or main.save_slot == 2:
        save_slot = 1
    elif main.load == 3 or main.save_slot == 3:
        save_slot = 2

    if main.choice == 1:
        character = "warrior"
    elif main.choice == 2:
        character = "mage"
    elif main.choice == 3:
        character = "tank"
    elif main.choice == 4:
        character = "barbarian"

    game_data["save_data"][save_slot]["character"] = character

    with open("game_data.json", "w", encoding="utf-8") as file:
        json.dump(file, game_data)