import time
import subprocess as sub
import sys
print("Hello!")
print("This is the game launcher for my games.")
time.sleep(1)
print("Select the game you want to play:")
games = {
    "1": "rpg_original.py",
    "2": "casino.py"
}
print(" 1. RPG Game")
print(" 2. Casino Games")
game = input("Enter the number of the game you want to launch: ")
if game in games:
    print("Launching...")
    time.sleep(3)
    sub.run([sys.executable, str(games[game])])
else:
    print("Invalid game choice.")
