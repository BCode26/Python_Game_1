import roulette
import slots
import time 
import blackjack

def Casino():
    print("Welcome to the Casino!")
    time.sleep(1)
    print("What game would you like to play? (roulette, slots, blackjack,)")
    game = input("Enter the game you would like to play (type exit to quit): ")
    if game == "roulette":
        roulette.Roulette(gold)
    elif game == "slots":
        slots.Slots()
    elif game == "blackjack":
        blackjack.Blackjack(gold)
    else:
        print("Invalid game")
gold = 100
if __name__ == "__main__":
    Casino()
