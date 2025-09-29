from GameMage import *
from GameDragon import *
import random

choice = [1,2,3,4,5]

Player = Mage(1000,100,100,100,100,9000,50,50,200,200)
Enemy = Dragon(10000,1000,100,90000,9000,100)

Play = True

SelfBurnTicks = 0
SelfBleedTicks = 0
BurnTicks = 0
BleedTicks = 0
PoisonTicks = 0
ShockTicks = 0 


EBurnTicks = 0
EBleedTicks = 0
EPoisonTicks = 0
EShockTicks = 0

BurnDmg = 0
BleedDmg = 0
PoisonDmg = 0
ShockShred = 0

SelfBurnDmg = 0
SelfBleedDmg = 0
SelfBleedShred = 0

EBurnDmg = 0
EBleedDmg = 0
EBleedShred = 0
EPoisonDmg = 0
EPoisonshred = 0
EShockShred = 0

while Play:
    if Player.Hp <= 0:
        print("The Dragon tosses you in the air and swallows you whole. You Loose...")
        break
    elif Enemy.Hp <= 0:
        print("You have slayed the dragon. You win!!!")
        break
    else:

        #Player Turn
        PlayerTurn = True
        while PlayerTurn:
            n = int(input("\nIt is your turn. \nPress 1 to view move list, Press 2 to view current stats, Press 3 to Attack: "))
            if n == 1:
                for i in range(1,11):
                    print(f"Move {i}")
                    for j in range(0,6):
                        print(Player.MoveList(i)[j])
                    print("\n")
            elif n == 2:
                Player.current_stats()
            elif n == 3: 
                m = int(input("\nEnter Move Number: "))
                if m > 0 and m < 11: 
                    for j in range(0 , 6):
                        print(Player.MoveList(m)[j])
                    confirm = input("\nEnter y to confirm and n to go back: ")
                    if confirm == "y":
                        PlayerMove = Player.MoveList(m)[6]
                        print(f"\nPlaying Move {m}")
                        print(Player.MoveList(m)[0])
                        print(Player.MoveList(m)[1])
                        PlayerTurn = False
                    elif confirm == "n":
                        print("\nGoing back...")
                    else:
                        print("\nEnter a value a argument.")
                else:
                    print("\nEnter a valid argument.")
            else:
                print("\nEnter a valid argument.")
            
        
        #Move effects
        print("Playing your Move.")
        Player.Mana = Player.Mana - PlayerMove["Cost"]
        #Enemy Damage and debuffs.
        Enemy.Hp = Enemy.Hp - (PlayerMove["dmg"]*(1 - (Enemy.Def/1000)))
        print(f"\nDamage dealt = {PlayerMove["dmg"]*(1 - (Enemy.Def/1000))}")
        Enemy.Atk = Enemy.Atk - (PlayerMove["Atk shred"])
        Enemy.Def = Enemy.Def - (PlayerMove["Def shred"])
        #Player Buffs
        Player.Hp = Player.Hp + PlayerMove["heal"]
        Player.Atk = Player.Atk + PlayerMove["Atk Buff"]
        Player.Def = Player.Def + PlayerMove["Def Buff"]
        Player.Int = Player.Int + PlayerMove["Int Buff"]
        Player.Mana = Player.Mana + PlayerMove["Mana Buff"]

        #Self Burns and Self Bleeds
        if PlayerMove["Self Burn"][0] == True:
            SelfBurnTicks += PlayerMove["Self Burn"][1]
            SelfBurnDmg = PlayerMove["Self Burn"][2]
            print("\nYou have been inflicted with self burn.")
        
        if PlayerMove["Self Bleed"][0] == True:
            SelfBleedTicks += PlayerMove["Self Bleed"][1]
            SelfBleedDmg = PlayerMove["Self Bleed"][2]
            SelfBleedShred = PlayerMove["Self Bleed"][3]
            print("\nYou have been inflicted with self bleed")

        #Enemy DoTs
        if PlayerMove["Burn"][0] == True:
            BurnTicks += PlayerMove["Burn"][1]
            BurnDmg = PlayerMove["Burn"][2]
            print("\nEnemy is burnt")

        if PlayerMove["Bleed"][0] == True:
            BleedTicks += PlayerMove["Bleed"][1]
            BleedDmg = PlayerMove["Bleed"][2]
            BleedShred = PlayerMove["Bleed"][3]
            print("\nEnemy bleeds")

        if PlayerMove["Poison"][0] == True:
            PoisonTicks += PlayerMove["Poison"][1]
            PoisonDmg = PlayerMove["Poison"][2]
            PoisonShred = PlayerMove["Poison"][3]
            print("\nEnemy is poisoned.")
        
        if PlayerMove["Shock"][0] == True:
            ShockTicks += PlayerMove["Shock"][1]
            ShockShred = PlayerMove["Shock"][2]
            print("\nEnemy is shocked")

        print("\n Your Stats Below")
        Player.current_stats()
        print("\nDragon's Stats Below")
        Enemy.current_stats()    

        if Enemy.Hp <= 0:
            print("You have slayed the Dragon. You win!!!") 
            break   

        #Dragon's Turn
        DragonAttack = random.choice(choice)
        DragMove = Enemy.MoveList(DragonAttack)[2]
        print(Enemy.MoveList(DragonAttack)[0])
        print(Enemy.MoveList(DragonAttack)[1])

        #Move Effects
        Player.Hp = Player.Hp - (DragMove["dmg"] * (1 - (Player.Def/1000)))
        print(f"Damage dealt = {DragMove["dmg"] * (1 - (Player.Def/1000))}")
        Player.Atk = Player.Atk - DragMove["Atk shred"]
        Player.Def = Player.Def - DragMove["Def shred"]
        Player.Int = Player.Int - DragMove["Int shred"]
        #DragonBuffs
        Enemy.Hp = Enemy.Hp + DragMove["heal"]
        Enemy.Atk = Enemy.Atk + DragMove["Atk Buff"]
        Enemy.Def = Enemy.Def + DragMove["Def Buff"]

        #Player Dots
        if DragMove["Burn"][0] == True:
            EBurnTicks += DragMove["Burn"][1]
            EBurnDmg = DragMove["Burn"][2]
            print("\nYou are burning")

        if DragMove["Bleed"][0] == True:
            EBleedTicks += DragMove["Bleed"][1]
            EBleedDmg = DragMove["Bleed"][2]
            EBleedShred = DragMove["Bleed"][3]
            print("\nYou are bleeding")

        if DragMove["Poison"][0] == True:
            EPoisonTicks += DragMove["Poison"][1]
            EPoisonDmg = DragMove["Poison"][2]
            EPoisonshred = DragMove["Poison"][3]
            print("\n You are poisoned")
        
        if DragMove["Shock"][0] == True:
            EShockTicks += DragMove["Shock"][1]
            EShockShred = DragMove["Shock"][2]
            print("You are shocked.")

        #Damage Over Time (DoT)

        #Burn

        if BurnTicks > 0:
            if BurnTicks > 5:
                BurnTicks = 5
            
            BurnTicks -= 1
            Enemy.Hp = Enemy.Hp - BurnDmg
            print(f"Enemy takes burn damage : {-BurnDmg}")

        if EBurnTicks > 0:
            if EBurnTicks > 5:
                EBurnTicks = 5
            
            EBurnTicks -= 1
            Player.Hp = Player.Hp - EBurnDmg
            print(f"You take burn damage : {-EBurnDmg}")

        if SelfBurnTicks > 0:
            if SelfBurnTicks > 3:
                SelfBurnTicks = 3
            
            SelfBurnTicks -= 1
            Player.Hp = Player.Hp - SelfBurnDmg
            print(f"You take self burn damage : {-SelfBurnDmg}")

        #Bleed

        if BleedTicks > 0:
            if BleedTicks > 5:
                BurnTicks = 5
            
            BleedTicks -= 1
            Enemy.Hp = Enemy.Hp - BleedDmg
            print(f"Enemy takes bleed damage : {-BleedDmg}")
            Enemy.Def = Enemy.Def - BleedShred
            print(f"Bleed causes defense shred : {-BleedShred}")

        if SelfBleedTicks > 0:
            if SelfBleedTicks > 3:
                BurnTicks = 3
            SelfBleedTicks -= 1
            Player.Hp = Player.Hp - SelfBleedDmg
            print(f"You take self bleed damage : {-SelfBleedDmg}")
            Player.Def = Player.Def - SelfBleedShred
            print(f"Self Bleed causes Defense Shred : {-SelfBleedShred}")

        if EBleedTicks > 0:
            if EBleedTicks > 5:
                EBurnTicks = 5
            
            EBleedTicks -= 1
            Player.Hp = Player.Hp - BleedDmg
            print(f"You take Bleed Damage : {-EBleedDmg}")
            Enemy.Def = Player.Def - EBleedShred
            print(f"Bleed causes your defense to shred : {-EBleedShred}")

        #Poison

        if PoisonTicks > 0:
            if PoisonTicks > 5:
                PoisonTicks = 5
            
            PoisonTicks -= 1
            Enemy.Hp = Enemy.Hp - PoisonDmg
            print(f"Enemy takes poison damage: {-PoisonDmg}")
            Enemy.Atk = Enemy.Atk - PoisonShred
            print(f"Poison causes Attack shred : {-PoisonShred}")

        if EPoisonTicks > 0:
            if EPoisonTicks > 5:
                EPoisonTicks = 5
            
            EPoisonTicks -= 1
            Player.Hp = Player.Hp - EPoisonDmg
            print(f"You take poison damage: {-EPoisonDmg}")
            Player.Atk = Player.Atk - EPoisonshred
            print(f"Poison causes your attack to be shredded : {-EPoisonshred}")
        
        #Shock

        if ShockTicks > 0:
            if ShockTicks > 5:
                ShockTicks = 5
            
            ShockTicks -= 1
            Enemy.Def = Enemy.Def - ShockShred
            print(f"Shock causes defense to be shred : {-ShockShred}")

        if EShockTicks > 0:
            if EShockTicks > 5:
                EShcokTicks = 5
            
            EShockTicks -= 1
            Player.Def = Player.Def - EShockShred
            print(f"You are shocked and your defense shreds by : {-EShockShred}")



        


        


                