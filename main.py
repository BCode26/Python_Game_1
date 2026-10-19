import time
import pygame
import random
from pathlib import Path
import json
import transfer
import sys

"""
TO DO:
- FIX MAGIC (TOO STRONG)
- FINISH SAVE FILES
- CREATE FUNCTIONS FOR ALL AREAS (DARK LAIR, LAB, VOID)
- FINISH BOSSES
- GET MUSIC FOR ALL AREAS
- FIX SAVE FILE ERROR (IN AI)
- FINISH STORY
"""
i = 1
progress = 0
# Initialize pygame mixer
pygame.mixer.init()
def play_music_start():
    music_file = Path(__file__).parent / "music" / "Start Menu.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_enemy():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 127  - Enemy Retreating.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_boss1():
    music_file = Path(__file__).parent / "music" / "Hammer of New Kunlun (Kuafus Theme).mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_story():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 01 - Once Upon A Truthful Time.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_fields():
    music_file = Path(__file__).parent / "music" / "Seclusion - Undertale Yellow.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_caves():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 037 - Mining Co.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_shop():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 023 - Occupied Turf.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def play_music_approaching_death():
    music_file = Path(__file__).parent / "music" / "Undertale Yellow OST_ 042  - Apex.mp3"
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
def stop_music():
    pygame.mixer.music.stop()

def Fields():
    global progress, days, encounter
    while progress < 20:
        print(f"It is day {days}. Your health is at {player.hp}/{player.max_hp}. Your progress is at {progress * 5}%")
        time.sleep(3)
        if progress == 10 or progress == 20 or progress == 30 or progress == 40 or progress == 50 or progress == 60 or progress == 70 or progress == 80 or progress == 90 and not boss:
            print("You are making good progress!")
            input("Press enter to continue...")
            player.Shop()
        if encounter > 30:
            print("You encounter an enemy!")
            time.sleep(2)
            player.Battle(enemy)
        if enemy.enemy_hp <= 0:
            player.gold += 10
            print("You gained 10 gold!")
            player.kills += 1
            stop_music()
            play_music_fields()
        while i in range(0, 1000):
            opt1 = input("Would you like to keep progressing, rest, check stats, or save and quit? 1. progress | 2. rest | 3. check stats | 4. save and quit ")
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
            elif opt1 == "4":
                if not played:
                    while True:
                        save_slot = int(input("Which save slot would you like to save your game to? "))
                        if save_slot != 1 or save_slot != 2 or save_slot != 3:
                            print("Invalid input.")
                            continue
                print("Saving...")
                transfer.File_Change(save_slot)
                time.sleep(3)
                print("Saved!")
                sys.exit()
            else:
                print("Invalid input.")
                continue
        enemy.enemy_hp = enemy.enemy_totalhp
        encounter = random.randint(1,100)

def Caves():
    while progress < 40:
        print(f"It is day {days}. Your health is at {player.hp}/{player.max_hp}. Your progress is at {progress * 2.5}%")
        time.sleep(3)
        if progress == 10 or progress == 20 or progress == 30 or progress == 40 or progress == 50 or progress == 60 or progress == 70 or progress == 80 or progress == 90 and not boss:
            print("You are making good progress!")
            input("Press enter to continue...")
            player.Shop()
        if encounter > 30:
            print("You encounter an enemy!")
            time.sleep(2)
            player.Battle(enemy)
        if enemy.enemy_hp <= 0:
            player.gold += 10
            print("You gained 10 gold!")
            player.kills += 1
            stop_music()
            play_music_caves()
        while i in range(0, 1000):
            opt1 = input("Would you like to keep progressing, rest, or check stats? 1. progress | 2. rest | 3. check stats ")
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
            elif opt1 == "4":
                print("Saving...")
                transfer.File_Change()
                time.sleep(3)
                print("Saved!")
                sys.exit()
            else:
                print("Invalid input.")
                continue
        enemy.enemy_hp = enemy.enemy_totalhp
        encounter = random.randint(1,100)

class Player:
    def __init__(self, name, character):
        self.name = name
        self.max_hp = character["max_hp"]
        self.hp = self.max_hp
        self.atk = character["atk"]
        self.defe = character["defe"]
        self.gold = 0
        self.sword = 0
        self.armor = 0
        self.magic = character["magic"]
        self.totalinv_space = 10
        self.remaininv_space = self.totalinv_space
        self.staff = 0
        self.kills = 0
        self.hp_potion = 0
        self.hit_chance = random.randint(1, 100)
        self.bighit_chance = random.randint(1, 100)
    # Changes the player's stats based on their equipment
    def stat_up(self):
        if self.sword == 1:
            self.atk = 15
        if self.sword == 2:
            self.atk = 25
        if self.sword == 3:
            self.atk = 40
        if self.sword == 4:
            self.atk = 60
        if self.armor == 1:
            self.defe = 10
        if self.armor == 2:
            self.defe = 20
        if self.armor == 3:
            self.defe = 35
        if self.armor == 4:  
            self.defe = 55
        if self.staff == 1:
            self.magic = 10
        if self.staff == 2:
            self.magic = 20
        if self.staff == 3:
            self.magic = 40
        if self.staff == 4:
            self.magic = 70
    # The battle system for the boss
    def Boss_Battle(self, boss):
        while boss.boss_hp > 0 and self.hp > 0:
            if progress == 20:
                play_music_boss1()
                print(f"Your health is at {self.hp}/{self.max_hp}. The Craftsman's health is at {boss.boss_hp}/{boss.boss_totalhp}.")
            if progress == 40:
                pass
            action = input("What would you like to do?  1. attack | 2. risk attack | 3. item | 4. magic ")
            if action == "1":
                self.hit_chance = random.randint(1, 100)
                if self.hit_chance >= 20:
                    boss.boss_hp -= self.atk
                    print("You dealt", self.atk, "damage to the Craftsman!")
                    time.sleep(2)
                else:
                    print("The attack missed...")
                    time.sleep(1)
            elif action == "2":
                self.bighit_chance = random.randint(1, 100)
                if self.bighit_chance >= 50:
                    boss.boss_hp -= self.atk * 3
                    print(f"You dealt {self.atk * 3} damage to the Craftsman")
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
                    continue
            elif action == "4":
                if self.magic > 0:
                    magic_damage = random.randint(10, 30)
                    boss.boss_hp -= (magic_damage + self.magic)
                    print(f"You casted a spell to deal {magic_damage + self.magic} damage to the Craftsman!")
                    time.sleep(2)
                else:
                    print("You don't have any magic!")
                    time.sleep(1)
                    continue
            else:
                print("Invalid action. Please choose a valid option.")
                continue
            enemyhit_chance = random.randint(1,100)
            if boss.boss_hp <= 0:
                print(f"The Craftsman has been defeated!")
                break
            if enemyhit_chance >= 50:
                self.hp -= (boss.boss_atk - self.defe)
                print("The Craftsman attacked you and..!")
                time.sleep(0.5)
                print(f"dealt {boss.boss_atk - self.defe} damage!")
                time.sleep(1)
            else:
                print("The Craftsman attacked and...!")
                time.sleep(0.5)
                print("missed...")
                time.sleep(1)

    # The battle system for a normal enemy
    def Battle(self, enemy):
        play_music_enemy()
        while enemy.enemy_hp > 0 and self.hp > 0:
            print(f"Your health is at {self.hp}/{self.max_hp}. The enemy's health is at {enemy.enemy_hp}/{enemy.enemy_totalhp}.")
            action = input("What would you like to do?  1. attack | 2. risk attack | 3. item | 4. run | 5. magic ")
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
                    continue
            elif action == "4":
                if self.armor == -1:
                    print("You ran away, coward...")
                    break
                run_chance = random.randint(1,100)
                if run_chance >= enemy.enemy_hp * 2:
                    print("You successfully ran away!")
                    encounter = random.randint(1,100)
                    time.sleep(1)
                    stop_music()
                    break
                else:
                    print("You failed to run away...")
            elif action == "5":
                if self.magic > 0:
                    magic_damage = random.randint(10, 30)
                    enemy.enemy_hp -= (magic_damage + self.magic)
                    print(f"You casted a spell to deal {magic_damage + self.magic} damage to the enemy!")
                    time.sleep(2)
                else:
                    print("You don't have any magic!")
                    time.sleep(1)
                    continue
            else:
                print("Invalid action. Please choose a valid option.")
                continue
            enemyhit_chance = random.randint(1,100)
            if enemy.enemy_hp <= 0:
                print("The enemy has been defeated!")
                break
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
    # Shop system for the player to buy items and equipment
    def Shop(self):
            play_music_shop()
            while i in range(0, 1000) and progress == 10:
                print(f"You have {self.gold} gold.")
                if self.sword == 0 and self.armor == 0 and self.staff == 0:
                    shop_choice = input("What would you like to buy?  1.  wooden sword | 2. health potion | 3. wooden armor | 4. woodenstaff | 5. leave ")
                    if shop_choice == "1":
                        if self.gold <= 30:
                            print("You don't have enough gold!")
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
                    else:
                        print("Invalid choice. Please choose a valid option.")
                        continue
                elif self.sword == 1 and self.armor == 0 and self.staff == 0:
                    shop_choice = input("What would you like to buy?  1. health potion | 2. wooden armor | 3. wooden staff | 4. leave ")
                    if shop_choice == "1":
                        if self.gold <= 15:
                            print("You don't have enough gold!")
                        elif self.remaininv_space == 0:
                            print("You don't have enough inventory space!")
                        elif self.gold >= 15 and self.remaininv_space > 0:
                            self.hp_potion += 1
                            self.remaininv_space -= 1
                            self.gold -= 15
                            print("You bought a health potion!")
                    elif shop_choice == "2":
                        if self.gold >= 50:
                            self.armor += 1
                            self.gold -= 50
                            print("You bought wooden armor!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "3":
                        if self.gold >= 80:
                            self.staff += 1
                            self.gold -= 80
                            print("You bought a staff!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "4":
                        print("You left the shop.")
                        break
                elif self.sword == 0 and self.armor == 1 and self.staff == 0:
                    shop_choice = input("What would you like to buy?  1. wooden sword | 2. health potion | 3. wooden staff | 4. leave ")
                    if shop_choice == "1":
                        if self.gold >= 30:
                            self.sword += 1
                            self.gold -= 30
                            print("You bought a wooden sword!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                        
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
                        if self.gold >= 80:
                            self.staff += 1
                            self.gold -= 80
                            print("You bought a staff!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "4":
                        print("You left the shop.")
                        break

                elif self.sword == 0 and self.armor == 0 and self.staff == 1:
                    shop_choice = input("What would you like to buy?  1. wooden sword | 2. health potion | 3. wooden armor | 4. leave ")
                    if shop_choice == "1":
                        if self.gold >= 30:
                            self.sword += 1
                            self.gold -= 30
                            print("You bought a wooden sword!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
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
                        print("You left the shop.")
                        break

                elif self.sword == 1 and self.armor == 1 and self.staff == 0:
                    shop_choice = input("What would you like to buy?  1. health potion | 2. wooden staff | 3. leave ")
                    if shop_choice == "1":
                        if self.gold <= 15:
                            print("You don't have enough gold!")
                        elif self.remaininv_space == 0:
                            print("You don't have enough inventory space!")
                        elif self.gold >= 15 and self.remaininv_space > 0:
                            self.hp_potion += 1
                            self.remaininv_space -= 1
                            self.gold -= 15
                            print("You bought a health potion!")
                    elif shop_choice == "2":
                        if self.gold >= 80:
                            self.staff += 1
                            self.gold -= 80
                            print("You bought a staff!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "3":
                        print("You left the shop.")
                        break

                elif self.sword == 1 and self.armor == 0 and self.staff == 1:
                    shop_choice = input("What would you like to buy?  1. health potion | 2. wooden armor | 3. leave ")
                    if shop_choice == "1":
                        if self.gold <= 15:
                            print("You don't have enough gold!")
                        elif self.remaininv_space == 0:
                            print("You don't have enough inventory space!")
                        elif self.gold >= 15 and self.remaininv_space > 0:
                            self.hp_potion += 1
                            self.remaininv_space -= 1
                            self.gold -= 15
                            print("You bought a health potion!")
                    elif shop_choice == "2":
                        if self.gold >= 50:
                            self.armor += 1
                            self.gold -= 50
                            print("You bought wooden armor!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "3":
                        print("You left the shop.")
                        break

                elif self.sword == 0 and self.armor == 1 and self.staff == 1:
                    shop_choice = input("What would you like to buy?  1. health potion | 2. wooden sword | 3. leave ")
                    if shop_choice == "1":
                        if self.gold <= 15:
                            print("You don't have enough gold!")
                        elif self.remaininv_space == 0:
                            print("You don't have enough inventory space!")
                        elif self.gold >= 15 and self.remaininv_space > 0:
                            self.hp_potion += 1
                            self.remaininv_space -= 1
                            self.gold -= 15
                            print("You bought a health potion!")
                    elif shop_choice == "2":
                        if self.gold >= 30:
                            self.sword += 1
                            self.gold -= 30
                            print("You bought a wooden sword!")
                            self.stat_up()
                        else:
                            print("You don't have enough gold!")
                    elif shop_choice == "3":
                        print("You left the shop.")
                        break

                elif self.sword == 1 and self.armor == 1 and self.staff == 1:
                    shop_choice = input("What would you like to buy?  1. health potion | 2. leave ")
                    if shop_choice == "1":
                        if self.gold <= 15:
                            print("You don't have enough gold!")
                        elif self.remaininv_space == 0:
                            print("You don't have enough inventory space!")
                        elif self.gold >= 15 and self.remaininv_space > 0:
                            self.hp_potion += 1
                            self.remaininv_space -= 1
                            self.gold -= 15
                            print("You bought a health potion!")
                    elif shop_choice == "2":
                        print("You left the shop.")
                        break
    # Allows the player to check their stats at any time
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

# Loads character data from the .json file
play_music_start()
name = input("What is your name? ")
played = input("Have you played before? ") == "yes"
if played:
    with (Path(__file__).parent / "game_data.json").open(encoding="utf-8") as file:
        save_file = json.load(file)["save_data"]
    for number, slot in enumerate(save_file, start=1):
        area = slot["area"]
        progress = slot["progress"]
        print(f"{number} {slot['number']}")
        print(f"You are in the {area}")
        if area == "Fields":
            print(f"Your progress is at {progress * 5}%")
        if area == "Caves":
            print(f"Your progress is at {progress * 2.5}%")
        if area == "Dark Lair":
            print(f"Your progress is at {progress * 2}%")
        if area == "Lab":
            print(f"Your progress is at {progress * 1.25}%")
        if area == "Void":
            print(f"Your progress is at {progress}")
        if slot['wins_1'] == 0:
            print("          kills: 0 (see name after defeating this boss!)")
        else:
            print(f"Craftsman kills: {slot['wins_1']}")
        if slot['wins_2'] == 0:
            print("        kills: 0 (see name after defeating this boss!)")
        else:
            print(f"Arachne kills: {slot['wins_2']}")
        if slot['wins_3'] == 0:
            print("              kills: 0 (see name after defeating this boss!)")
        else:
            print(f"The Dark Lord kills: {slot['wins_3']}")
        if slot['wins_4'] == 0:
                pass
        else:
            print(f"Scyen kills: {slot['wins_4']}")
        if slot['wins_final'] == 0:
                pass
        else:
            print(f"Neverending Dark banishments: {slot['wins_final']}")
        time.sleep(7)
    while True:
        load = int(input("Load which save file? "))
        break

if not played:
    with (Path(__file__).parent / "character.json").open(encoding="utf-8") as file:
        characters = json.load(file)["characters"]
    for number, character in enumerate(characters, start=1):
        print(f"{number}. {character['type']}")

    while True:
        choice = int(input("Choose a character: "))
        if choice == 1:
            character = "warrior"
            break
        elif choice == 2:
            character = "mage"
            break
        elif choice == 3:
            character = "tank"
            break
        elif choice == 4:
            character = "barbarian"
            break

player = Player(name, characters[choice - 1])
# The enemy
class Enemy:
    def __init__(self):
        self.enemy_hp = 30
        self.enemy_atk = 15
        self.enemy_totalhp = 30
        self.enemyhit_chance = random.randint(1,100)
# The Boss
class Boss(Enemy):
    def __init__(self, bosses):
        super().__init__()
        self.boss_atk = enemy.enemy_atk * 3
        self.boss_totalhp = enemy.enemy_totalhp * 5
        self.boss_hp = self.boss_totalhp
        self.bosshit_chance = random.randint(1,100)
        self.boss_name = bosses["name"]
print("Welcome")
opt1 = "placeholder"
days = 0
boss = False
enemy = Enemy()
encounter = random.randint(1,100)
if player.name == "Beckett":
    while i in range(0, 1000000):
        time.sleep(0.01)
        print("Nope")
        i += 1
print(f"Hello, {player.name}")
input("Press enter to continue...")
player.stat_up()
stop_music()
play_music_story()
time.sleep(1)
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
play_music_fields()
Fields()
if progress == 20:
    print(f"You have made your way around the ruined fields and have found a small cave.")
    time.sleep(2)
    print("You enter the cave and find a craftsman.")
    time.sleep(1)
    print("'Hail, Craftsman.' you say.")
    time.sleep(1)
    print("However, the craftsman turns around and glares at you.")
    time.sleep(1)
    print(f"'I have been waiting for you, {player.name}. I have been watching your progress and I have seen your strength.'")
    time.sleep(2)
    print("'Too bad it will all end here!'")
    time.sleep(1)
    player.Boss_Battle(player, boss)
Caves()
if progress == 40:
    pass

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