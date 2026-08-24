# main.py
import random
print("Welcome")
days = 0
name = input("What is your name? ")
encounter = random.randint(1,100)
hit_chance = random.randint(1, 100)
bighit_chance = random.randint(1,100)
progress = 0
enemy1_hp = 30
enemy1_totalhp = 30
hp = 100
max_hp = 100
atk = 10
defe = 5
big_atk = atk * 3
print(f"Hello, {name}")
while progress < 100:
    print(f"It is day {days}. Your health is at {hp}/{max_hp}. Your progress is at {progress}%")
    if encounter > 5:
        print("You encounter an enemy!")
        while hp and enemy1_hp > 0:
            print(f"Your health is at {hp}/{max_hp} and the enemy's health is at {enemy1_hp}/{enemy1_totalhp}")
            action = input("What would you like to do?  1. attack | 2. risk attack ")
            if action == "1":
                if hit_chance >= 80:
                    enemy1_hp = enemy1_hp - atk
                    print("You dealt", atk,"damage to the enemy!")
                else:
                    print("The attack missed...")
            elif action == "2":
                if bighit_chance >= 50:
                    enemy1_hp = enemy1_hp - big_atk
                    print(f"You dealt {big_atk} damage to the enemy")
                else:
                    print("The attack missed...")
    opt1 = input("Would you like to keep progressing, rest, or check stats?   1. progress | 2. rest | 3. check stats ")
    if opt1 == "1":
        progress = progress + 1
        days = days + 1
        print("You make more progress.")
    elif opt1 == "2":
        hp = max_hp
        days = days + 1
        print("You rested for 1 day. Health fully restored!")
        
else:
    print("No one's here")
    