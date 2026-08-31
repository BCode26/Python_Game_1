# main.py
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.atk = 10
        self.defe = 5
        self.gold = 0
        self.progress = 0
        self.sword = 0
        self.armor = 0
        self.magic = 0
        self.inv_space = 10
        self.staff = 0
        self.kills = 0
        self.hp_potion = 0
        def Battle(self, enemy_hp, enemy_atk, hp, atk, defe, max_hp, hp_potion):
            while enemy_hp > 0 and hp > 0:
                action = input("What would you like to do?  1. attack | 2. risk attack | 3. item | 4. run ")
                if action == "1":
                    hit_chance = random.randint(1,100)
                    if hit_chance >= 20:
                        enemy_hp -= atk
                        print("You dealt", atk, "damage to the enemy!")
                    else:
                        print("The attack missed...")
                elif action == "2":
                    bighit_chance = random.randint(1,100)
                    if bighit_chance >= 50:
                        enemy_hp -= atk * 3
                        print(f"You dealt {atk * 3} damage to the enemy")
                    else:
                        print("The attack missed...")
                elif action == "3":
                    if hp_potion > 0:
                        hp = max_hp
                        hp_potion = 0
                        print("You used a health potion and fully restored your health!")
                    else:
                        print("You don't have any health potions!")
                elif action == "4":
                    run_chance = random.randint(1,100)
                    if run_chance >= enemy_hp * 2:
                        print("You successfully ran away!")
                        break
                    else:
                        print("You failed to run away...")
                # enemy attack
                enemyhit_chance = random.randint(1,100)
                if enemyhit_chance >= 50:
                    hp -= (enemy_atk - defe)
                    print("The enemy attacked you and..!")
                    print(f"dealt {enemy_atk - defe} damage!")
                else:
                    print("The enemy attacked and...!")
                    print("missed...")
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
print("Welcome")
days = 0
i = 1
name = input("What is your name? ")
player = Player(name)
encounter = random.randint(1,100)
hit_chance = random.randint(1, 100)
bighit_chance = random.randint(1,100)
progress = 0
enemy_hp = 30
enemyhit_chance = random.randint(1,100)
enemy_atk = 10
enemy_totalhp = 30
if player.name == "Beckett":
    while i in range(0, 1000):
        print("Nope")
print(f"Hello, {player.name}")
print(player.name, ", There is an evil guy. You should, like, stop him.")
while progress < 100:
    print(f"It is day {days}. Your health is at {player.hp}/{player.max_hp}. Your progress is at {player.progress * 2}%")
    if progress == 10 or progress == 20 or progress == 30 or progress == 40 or progress == 50 or progress == 60 or progress == 70 or progress == 80 or progress == 90:
        print("You are making good progress!")
        print("There is a shop here. You may buy a wooden sword for 30 gold. You may buy a health potion for 15 gold. You may buy wooden armor for 50 gold. You may buy a staff for 80 gold. 1. sword | 2. health potion | 3. armor | 4. staff | 5. leave")
        player.Shop(player, player.gold, player.sword, player.armor, player.staff, player.hp_potion)
    if encounter > 30:
        print("You encounter an enemy!")
        player.Battle(player, enemy_hp, enemy_atk, player.hp, player.atk, player.defe, player.max_hp, hp_potion)
        # fight while both combatants have HP above 0
    if enemy_hp <= 0:
        print("You defeated the enemy!")
        gold += 10
        print("You gained 10 gold!")
        enemy_hp = enemy_totalhp
        kills += 1
        opt1 = input("Would you like to keep progressing, rest, or check stats?   1. progress | 2. rest | 3. check stats ")
    while i in range(0, 1000):
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
            player.check_stats(player, player.hp, player.max_hp, player.atk, player.defe, player.gold, player.progress, player.sword, player.armor, player.staff, player.hp_potion)
    enemy_hp = enemy_totalhp
    encounter = random.randint(1,100)
