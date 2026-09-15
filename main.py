# main.py
import time
import pygame
import random
from pathlib import Path
pygame.mixer.init()
def play_music_start():
    music_file = Path(__file__).parent / "music" / "Start Menu.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_enemy():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 127  - Enemy Retreating.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_story():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 001  - Once Upon A Truthful Time.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_dun1():
    music_file = Path(__file__).parent / "music" / "Seclusion - Undertale Yellow.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_dun2():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 037 - Mining Co.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_shop():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 0123  - Occupied Turf.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_approaching_death():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 042  - Apex.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def stop_music():
    pygame.mixer.music.stop()
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
        self.totalinv_space = 10
        self.remaininv_space = self.totalinv_space
        self.staff = 0
        self.kills = 0
        self.hp_potion = 0
        self.hit_chance = random.randint(1, 100)
        self.bighit_chance = random.randint(1, 100)
    def stat_up(self):
        if self.sword == 1:
            self.atk += 5
        elif self.sword == 2:
            self.atk += 10
        elif self.sword == 3:
            self.atk += 15
        elif self.sword == 4:
            self.atk += 20
        elif self.armor == 1:
            self.defe += 5
        elif self.armor == 2:
            self.defe += 10
        elif self.armor == 3:
            self.defe += 15
        elif self.armor == 4:  
            self.defe += 20
        elif self.staff == 1:
            self.magic += 10
        elif self.staff == 2:
            self.magic += 10
        elif self.staff == 3:
            self.magic += 20
        elif self.staff == 4:
            self.magic += 30
    def Battle(self, enemy):
        play_music_enemy()
        while enemy.enemy_hp > 0 and self.hp > 0:
            print(f"Your health is at {self.hp}/{self.max_hp}. The enemy's health is at {enemy.enemy_hp}/{enemy.enemy_totalhp}.")
            action = input("What would you like to do?  1. attack | 2. risk attack | 3. item | 4. run ")
            if action == "1":
                self.hit_chance = random.randint(1, 100)
                if self.hit_chance >= 20:
                    enemy.enemy_hp -= self.atk
                    print("You dealt", self.atk, "damage to the enemy!")
                    time.sleep(2)
                else:
                    print("The attack missed...")
                    time.sleep(1)
            elif action == "2":
                self.bighit_chance = random.randint(1, 100)
                if self.bighit_chance >= 50:
                    enemy.enemy_hp -= self.atk * 3
                    print(f"You dealt {self.atk * 3} damage to the enemy")
                    time.sleep(2)
                else:
                    print("The attack missed...")
                    time.sleep(1)
            elif action == "3":
                if self.hp_potion > 0:
                    heal = random.randint(30, 70)
                    self.hp_potion -= 1
                    self.hp += heal
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    print(f"You used a health potion and healed {heal} health!")
                    time.sleep(2)
                else:
                    print("You don't have any health potions!")
                    time.sleep(1)
            elif action == "4":
                if self.armor == -1:
                    print("You ran away, coward...")
                run_chance = random.randint(1,100)
                if run_chance >= enemy.enemy_hp * 2:
                    print("You successfully ran away!")
                    encounter = random.randint(1,100)
                    time.sleep(1)
                    stop_music()
                    break
                else:
                    print("You failed to run away...")
            enemyhit_chance = random.randint(1,100)
            if enemyhit_chance >= 50:
                self.hp -= (enemy.enemy_atk - self.defe)
                print("The enemy attacked you and..!")
                time.sleep(0.5)
                print(f"dealt {enemy.enemy_atk - self.defe} damage!")
                time.sleep(1)
            else:
                print("The enemy attacked and...!")
                time.sleep(0.5)
                print("missed...")
                time.sleep(1)
    def Shop(self):
            while i in range(0, 1000):
                print(f"You have {self.gold} gold.")
                play_music_shop()
                if self.sword == 0 and self.armor == 0 and self.staff == 0:
                    shop_choice = input("What would you like to buy?  1. sword | 2. health potion | 3. armor | 4. staff | 5. leave ")
                    if shop_choice == "1":
                        if self.gold <= 30:
                            print("You don't have enough gold!")
                        elif self.sword > 0:
                            print("You already have a wooden sword!")
                        elif self.sword == 0 and self.gold >= 30:
                            self.sword += 1
                            self.gold -= 30
                            print("You bought a wooden sword!")
                            self.stat_up()
                    elif shop_choice == "2":
                        if self.gold <= 15:
                            print("You don't have enough gold!")
                        elif self.remaininv_space == 0:
                            print("You don't have enough inventory space!")
                        elif self.gold >= 15 and self.remaininv_space > 0:
                            self.hp_potion += 1
                            self.remaininv_space -= 1
                            self.gold -= 15
                            print("You bought a health potion!")
                    elif shop_choice == "3":
                        if self.gold >= 50:
                            self.armor += 1
                            self.gold -= 50
                            print("You bought wooden armor!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "4":
                        if self.gold >= 80:
                            self.staff += 1
                            self.gold -= 80
                            print("You bought a staff!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "5":
                        print("You left the shop.")
                        break
                elif self.sword == 1 and self.armor == 0 and self.staff == 0:
                    shop_choice = input("What would you like to buy?  1. sword | 2. health potion | 3. armor | 4. staff | 5. leave ")
                
    def check_stats(self):
            print(f"Health: {self.hp}/{self.max_hp}")
            print(f"Attack: {self.atk}")
            print(f"Defense: {self.defe}")
            print(f"Gold: {self.gold}")
            print(f"Sword level: {self.sword}")
            print(f"Armor level: {self.armor}")
            print(f"Staff level: {self.staff}")
            print(f"Health Potions: {self.hp_potion}")
            print(f"Remaining Inventory Space: {self.remaininv_space}")

class Enemy:
    def __init__(self):
        self.enemy_hp = 30
        self.enemy_atk = 10
        self.enemy_totalhp = 30
        self.enemyhit_chance = random.randint(1,100)
play_music_start()
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
stop_music()
play_music_story()
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
    play_music_dun1()
    print(f"It is day {days}. Your health is at {player.hp}/{player.max_hp}. Your progress is at {progress * 2}%")
    time.sleep(3)
    if progress == 10 or progress == 20 or progress == 30 or progress == 40 or progress == 50 or progress == 60 or progress == 70 or progress == 80 or progress == 90:
        print("You are making good progress!")
        input("Press enter to continue...")
        print("There is a shop here. You may buy a wooden sword for 30 gold. You may buy a health potion for 15 gold. You may buy wooden armor for 50 gold. You may buy a staff for 80 gold. 1. sword | 2. health potion | 3. armor | 4. staff | 5. leave")
        player.Shop()
    if encounter > 30:
        print("You encounter an enemy!")
        time.sleep(2)
        player.Battle(enemy)
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
            player.check_stats()
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
        