# main.py
import time
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.atk = 10
        self.defe = 5
        self.gold = 0
        self.sword = 0
        self.armor = 0
        self.magic = 0
        self.inv_space = 10
        self.staff = 0
        self.kills = 0
        self.hp_potion = 0
        self.hit_chance = random.randint(1, 100)
        self.bighit_chance = random.randint(1, 100)
    def Battle(self, enemy, hp, atk, defe, max_hp, hp_potion):
        while enemy.enemy_hp > 0 and hp > 0:
            print(f"Your health is at {hp}/{max_hp}. The enemy's health is at {enemy.enemy_hp}/{enemy.enemy_totalhp}.")
            action = input("What would you like to do?  1. attack | 2. risk attack | 3. item | 4. run ")
            if action == "1":
                self.hit_chance = random.randint(1, 100)
                if self.hit_chance >= 20:
                    enemy.enemy_hp -= atk
                    print("You dealt", atk, "damage to the enemy!")
                    time.sleep(2)
                else:
                    print("The attack missed...")
                    time.sleep(1)
            elif action == "2":
                self.bighit_chance = random.randint(1, 100)
                if self.bighit_chance >= 50:
                    enemy.enemy_hp -= atk * 3
                    print(f"You dealt {atk * 3} damage to the enemy")
                    time.sleep(2)
                else:
                    print("The attack missed...")
                    time.sleep(1)
            elif action == "3":
                if hp_potion > 0:
                    heal = hp + random.randint(30, 70)
                    hp_potion -= 1
                    if hp > max_hp:
                        hp = max_hp
                    print(f"You used a health potion and healed {heal} health!")
                    time.sleep(2)
                else:
                    print("You don't have any health potions!")
                    time.sleep(1)
            elif action == "4":
                run_chance = random.randint(1,80)
                if run_chance >= enemy.enemy_hp * 2:
                    print("You successfully ran away!")
                    encounter = random.randint(1,100)
                    time.sleep(1)
                    break
                else:
                    print("You failed to run away...")
            enemyhit_chance = random.randint(1,100)
            if enemyhit_chance >= 50:
                hp -= (enemy.enemy_atk - defe)
                print("The enemy attacked you and..!")
                time.sleep(0.5)
                print(f"dealt {enemy.enemy_atk - defe} damage!")
                time.sleep(1)
            else:
                print("The enemy attacked and...!")
                time.sleep(0.5)
                print("missed...")
                time.sleep(1)
    def Shop(self, gold, sword, armor, staff, hp_potion):
            print(f"You have {gold} gold.")
            while i in range(0, 1000):
                shop_choice = input("What would you like to buy?  1. sword | 2. health potion | 3. armor | 4. staff | 5. leave ")
                if shop_choice == "1":
                    if gold >= 30:
                        sword += 1
                        gold -= 30
                        print("You bought a wooden sword!")
                    else:
                        print("You don't have enough gold!")
                elif shop_choice == "2":
                    if gold >= 15:
                        hp_potion += 1
                        gold -= 15
                        print("You bought a health potion!")
                    else:
                        print("You don't have enough gold!")
                elif shop_choice == "3":
                    if gold >= 50:
                        armor += 1
                        gold -= 50
                        print("You bought wooden armor!")
                    else:
                        print("You don't have enough gold!")
                elif shop_choice == "4":
                    if gold >= 80:
                        staff += 1
                        gold -= 80
                        print("You bought a staff!")
                    else:
                        print("You don't have enough gold!")
                elif shop_choice == "5":
                    print("You left the shop.")
                    break
    def check_stats(self, hp, max_hp, atk, defe, gold, progress, sword, armor, staff, hp_potion):
            print(f"Health: {hp}/{max_hp}")
            print(f"Attack: {atk}")
            print(f"Defense: {defe}")
            print(f"Gold: {gold}")
            print(f"Sword level: {sword}")
            print(f"Armor level: {armor}")
            print(f"Staff level: {staff}")
            print(f"Health Potions: {hp_potion}")
            print(f"Remaining Inventory Space: {self.inv_space - (sword + armor + staff + hp_potion)}")

class Enemy:
    def __init__(self):
        self.enemy_hp = 30
        self.enemy_atk = 10
        self.enemy_totalhp = 30
        self.enemyhit_chance = random.randint(1,100)
print("Welcome")
opt1 = "placeholder"
days = 0
i = 1
name = input("What is your name? ")
player = Player(name)
enemy = Enemy()
encounter = random.randint(1,100)
progress = 0
if player.name == "Beckett":
    while i in range(0, 1000000):
        print("Nope")
        i += 1
print(f"Hello, {player.name}")
input("Press enter to continue...")
print(f"{player.name}, you are a brave adventurer. You have embarked on a quest to kill the Dark Lord after he destroyed the kingdom.")
time.sleep(3)
print("You will have to fight many enemies and make your way through the ruined kingdom.")
time.sleep(3)
print("From killing enemies, you will gain gold to make trade with a shopkeeper at a shop.")
time.sleep(3)
print("After you make it to 100% progress, you will find the Dark Lord's lair.")
time.sleep(3)
print("You will have to defeat the Dark Lord to win the game.")
time.sleep(3)
print(f"Good luck, {player.name}!")
time.sleep(3)
while progress < 100:
    print(f"It is day {days}. Your health is at {player.hp}/{player.max_hp}. Your progress is at {progress * 2}%")
    time.sleep(3)
    if progress == 10 or progress == 20 or progress == 30 or progress == 40 or progress == 50 or progress == 60 or progress == 70 or progress == 80 or progress == 90:
        print("You are making good progress!")
        input("Press enter to continue...")
        print("There is a shop here. You may buy a wooden sword for 30 gold. You may buy a health potion for 15 gold. You may buy wooden armor for 50 gold. You may buy a staff for 80 gold. 1. sword | 2. health potion | 3. armor | 4. staff | 5. leave")
        player.Shop(player.gold, player.sword, player.armor, player.staff, player.hp_potion)
    if encounter > 30:
        print("You encounter an enemy!")
        time.sleep(2)
        player.Battle(enemy, player.hp, player.atk, player.defe, player.max_hp, player.hp_potion)
        # fight while both combatants have HP above 0
    if enemy.enemy_hp <= 0:
        print("You defeated the enemy!")
        player.gold += 10
        print("You gained 10 gold!")
        player.kills += 1
    while i in range(0, 1000):
        opt1 = input("Would you like to keep progressing, rest, or check stats?   1. progress | 2. rest | 3. check stats ")
        if opt1 == "1":
            progress += 1
            days += 1
            print("You make more progress.")
            break
        elif opt1 == "2":
            player.hp = player.max_hp
            days += 1
            print("You rested for 1 day. Health fully restored!")
            break
        elif opt1 == "3":
            player.check_stats(player.hp, player.max_hp, player.atk, player.defe, player.gold, player.progress, player.sword, player.armor, player.staff, player.hp_potion)
    enemy.enemy_hp = enemy.enemy_totalhp
    encounter = random.randint(1,100)

print("You have reached 100% progress! You have found the Dark Lord's lair!")
time.sleep(2)
print("You enter the lair and find the Dark Lord waiting for you.")
time.sleep(2)
print(f"'Hello, {player.name}. I have been waiting for you. It took you {days} to find me.'")
time.sleep(4)
while i in range(0, 1000):
    if days <= 100:
        print("'You made it here in the minimum amount of time. Somehow, you figured out how to get here without resting once.'")
        time.sleep(5)
        print("'Incredible.'")
        print("'Either way, draw your weapon. I will not go easy on you.'")
    if days > 100 and days <= 150:
        print("'You made it here quickly.'")
        time.sleep(2)
        print(f"'It only took you {days} days to find me.'")
        