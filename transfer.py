import json

from pathlib import Path


def JSON_Change(save_slot, gold, character, progress):
    if save_slot not in (1, 2, 3):
        raise ValueError("save_slot must be 1, 2, or 3")

    game_data_path = Path(__file__).parent / "game_data.json"
    with game_data_path.open(encoding="utf-8") as file:
        game_data = json.load(file)

    slot = game_data["save_data"][save_slot - 1]
    slot["gold"] = gold
    slot["progress"] = progress
    if character is not None:
        slot["character"] = character

    with game_data_path.open("w", encoding="utf-8") as file:
        json.dump(game_data, file, indent=4)