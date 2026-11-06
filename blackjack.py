import random
import time
import sys

def Blackjack(gold):
    print("Welcome to Blackjack!")
    time.sleep(1)
    game = True
    while gold > 0 and game:
        print(f"You have ${gold}")
        time.sleep(1)
        bet = int(input("How much would you like to bet? "))
        if bet > gold:
            print("You don't have enough money!")
            continue
        player_card = [random.randint(1, 13), random.randint(1, 13)]
        dealer_card = [random.randint(1, 13), random.randint(1, 13)]
        print(f"Your cards are {10 if player_card[0] >= 11 else player_card[0]} and {10 if player_card[1] >= 11 else player_card[1]}.")
        dealer_show = random.choice(dealer_card)
        print(f"You can see that the dealer has {10 if dealer_show >= 11 else dealer_show}.")
        while game:
            while True:
                if dealer_stand and stand and total < 21:
                    if sum(player_card) > sum(dealer_card):
                        print("You win!")
                        gold += bet
                        go = input("Would you like to play again? (yes/no) ")
                        if go == "no":
                            game = False
                            break
                    elif sum(player_card) < sum(dealer_card):
                        print("You lose!")
                        gold -= bet
                        go = input("Would you like to play again? (yes/no) ")
                        if go == "no":
                            game = False
                            break
                    else:
                        print("It's a tie!")
                        go = input("Would you like to play again? (yes/no) ")
                        if go == "no":
                            game = False
                            break
                total = sum(player_card)
                if total > 21:
                    print("You bust! You lose!")
                    gold -= bet
                    go = input("Would you like to play again? (yes/no) ")
                    if go == "no":
                        game = False
                    else:
                        continue
                if total == 21:
                    print("You got a blackjack! You win!")
                    time.sleep(1)
                    print("You gained $", bet * 1.5)
                    gold += bet * 1.5
                    go = input("Would you like to play again? (yes/no) ")
                    if go == "no":
                        game = False
                hit = input("Hit or Stand? ") == "Hit"
                if hit:
                    player_card.append(random.randint(1, 13))
                    print(f"You now have a {10 if player_card[-1] >= 11 else player_card[-1]}")
                # Dealer's turn
                else:
                    print(f"You stand.")
                    time.sleep(1)
                    stand = True
                dealer_total = sum(dealer_card)
                if dealer_total > 21:
                        print("Dealer busts! You win!")
                        gold += bet
                        go = input("Would you like to play again? (yes/no) ")
                        if go == "no":
                            game = False
                            break
                elif dealer_total == 21:
                        print("Dealer got a blackjack! You lose!")
                        gold -= bet
                        go = input("Would you like to play again? (yes/no) ")
                        if go == "no":
                            game = False
                            break
                else:
                    dealer_total = sum(dealer_card)
                    while dealer_total < 15:
                        dealer_card.append(random.randint(1, 13))
                        dealer_total = sum(dealer_card)
                        print(f"Dealer now has a {10 if dealer_card[-1] >= 11 else dealer_card[-1]}")
                        time.sleep(1)
                    dealer_stand = True
    if gold <= 0:
        print("You are out of money!")
        print("The casino kills you!")
        sys.exit()

gold = 100
Blackjack(gold)
