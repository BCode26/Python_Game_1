import time
import random
import sys
i = 1
spin = random.randint(0, 36)
money = 100
print("Are you really bored?")
time.sleep(1)
print("WELL, NOW YOU CAN PLAY ROULETTE!")
time.sleep(0.17)
print("NO SCAM")
time.sleep(0.17)
print("NO UNHAPPINESS")
time.sleep(0.17)
print("NO FAIL")
time.sleep(0.17)
print("NO BAKE")
time.sleep(0.17)
for i in range (0, 17):
    print("HA")
    time.sleep(0.17)
print("Now, let's play!")
print(f"You have $100 to start")
gold = 100
def Roulette(gold):
    while i in range(0, 1000):
        print("You have $",gold)
        if gold < 0:
            print("You are out of money!")
            print("The casino kills you!")
            break
        bet = input("What would you like to bet on? (number, color) ")
        if bet == "number":
            number = int(input("What number would you like to bet on? (0-36) "))
            amount = int(input("How much would you like to bet? "))
            if number < 0 or number > 36:
                print("Invalid number")
                continue
            if spin == number:
                print("You won! The number was", spin)
                print("You gained $", amount * 35)
                gold += amount * 35
            else:
                print("You lost! The number was", spin)
                print("You lost $", amount)
                gold -= amount
        elif bet == "color":
            color = input("What color would you like to bet on? (red, black, green) ")
            if color not in ["red", "black", "green"]:
                print("Invalid color")
                continue
            amount = int(input("How much would you like to bet? "))
            if spin % 2 == 0 and color == "red":
                print("You won! The number was", spin)
                print("You gained $", amount * 2)
                gold += amount * 2
            elif spin % 2 == 1 and color == "black":
                print("You won! The number was", spin)
                print("You gained $", amount * 2)
                gold += amount * 2
            elif spin == 0 and color == "green":
                print("You won! The number was", spin)
                print("You gained $", amount * 35)
                gold += amount * 35
            else:
                print("You lost! The number was", spin)
                print("You lost $", amount)
                gold -= amount
        else:
                    print("Invalid bet")
                    continue
        go = input("Would you like to play again? (yes/no) ")
        if go == "no":
            break
        