from GameBaseStats import TypeStat 

class Mage(TypeStat):
    def __init__(self, BaseHP, BaseATK, BaseDef, BaseInt, BaseMana, Hp, Atk, Def, Int, Mana):
        super().__init__(BaseHP, BaseATK, BaseDef, BaseInt, BaseMana, Hp, Atk, Def, Int, Mana)

    def Move_1(self):
        name = "Mana Orb"
        description = "\nThe most basic of spells. You channel your mana into your hands.\nYou shape it into a ball and launch it towards your enemy.\n"
        IntelligenceRequired = "Intelligence Required : 20"
        ManaCost = "Mana Cost: 40"
        damage = f"damage = 1 x atk + 2 x int = {1*self.Atk + 2*self.Int}"
        effect = "Null"
        if self.Int < 20 or self.Mana < 40:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 40,
                "dmg":1*self.Atk + 2*self.Int,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        
    def Move_2(self):
        name = "Recover"
        description = "\nAs an ardent believer of gods, you invoke their bledding to heal yourself. The gods redaily bless you.\n"
        IntelligenceRequired = "Intelligence Required : 100"
        ManaCost = "Mana cost : 60"
        damage = f"Healing = 0.3 x Base HP +  10 x int = {0.3*self.BaseHP + 10*self.Int}"
        effect = "Null"
        if self.Int < 100 or self.Mana < 60:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 60,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0.3*self.BaseHP + 10*self.Int,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        
    def Move_3(self):
        name = "Inquisition"
        description = "\nMages are very inquisitive persons.\nYour thirst for knowledge interests the gods and they bless you.\n"
        IntelligenceRequired = "Intelligence Required : 50"
        ManaCost = "Mana Cost : 60"
        damage = f"Intelligence Buff = 0.5 x Base INT= {0.4*self.BaseINT}"
        effect = "Null"
        if self.Int < 50 or self.Mana < 60:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 60,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0.5*self.BaseINT ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List

    def Move_4(self):
        name = "Recharge"
        description = "\nYou meditate, absorbing nature's mana within you.\nThe calmness boosts your wisdom, stamina and recovers some strength as well.\n"
        IntelligenceRequired = "Intelligence Required : 50"
        ManaCost = "Mana Cost : 0"
        damage = f"Mana Buff = 0.3 x INT = {0.3*self.Int} , heal,Atk, Def and Int buff."
        effect = "Null"
        if self.Int < 50 or self.Mana < 0:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 1000,
                "Atk Buff":100,
                "Def Buff": 100 ,
                "Int Buff" : 50 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 50,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0,
                "Mana Buff" : 0.5*self.Int , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        
    def Move_5(self):
        name = "Mana Beam"
        description = "\nYou channel your dense mana through your hand, right at your enemy in the form of a continuous beam.\n"
        IntelligenceRequired = "Intelligence Required : 300"
        ManaCost = "Mana Cost : 200"
        damage = f"Damage = 3 x ATK + 10 x INT = {3*self.Atk + 10*self.Int}"
        effect = "Bleed, Duration = 2, damage per tick = 3 x Atk , def shred per tick = 0.3 x Int "
        if self.Int < 300 or self.Mana < 200:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 300,
                "dmg": 3*self.Atk + 10*self.Int,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [True , 2 , 5*self.Atk , 0.3*self.Int],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0,
                "Mana Buff" : 0, 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List

    def Move_6(self):
        name = "Blood Sacrifice"
        description = "\nThe dark one seeks life blood.\nYou feed it some of your own and in return gain immense power.\n"
        IntelligenceRequired = "Intelligence Required : 500"
        ManaCost = "Mana Cost : 25"
        damage = f"All stat boost by 0.5 x Int = {0.5*self.Int} and mana buff by 0.1 x Int = {0.15*self.Int}"
        effect = "Self damage: 0.30 x Hp \nSelf Bleed : Duration = 3, damage per tick = 400 , def shred per tick = 20 "
        if self.Int < 500 or self.Mana < 50:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 50,
                "dmg": 0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : -0.30*self.Hp,
                "Atk Buff":0.6*self.Int,
                "Def Buff": 0.6*self.Int ,
                "Int Buff" : 0.6*self.Int,
                "Mana Buff" : 0.3*self.Int, 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [True , 3 , 400 , 20],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List

    def Move_7(self):
        name = "Fire Bomb"
        description = "\nThis is what happens when playing with fire goes wrong...no, not for you. It goes well for you.\n"
        IntelligenceRequired = "Intelligence Required : 400"
        ManaCost = "Mana Cost : 400"
        damage = f"Damage = 10 x ATK + 12 x INT = {10*self.Atk + 12*self.Int}"
        effect = "Burn, Duration = 4, damage per tick = 8 x INT\nGods' Aid: +100 Atk, +100 Int"
        if self.Int < 300 or self.Mana < 400:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 400,
                "dmg": 10*self.Atk + 12*self.Int,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [True , 3 , 8*self.Int],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":100,
                "Def Buff": 0 ,
                "Int Buff" : 100,
                "Mana Buff" : 0, 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        
    def Move_8(self):
        name = "Thunder Clap"
        description = "\nThe clouds are consumed with bright lightning and roaring thunder.\nYou use this natural energy and rain it down on your enemy\n"
        IntelligenceRequired = "Intelligence Required : 500"
        ManaCost = "Mana Cost : 450"
        damage = f"Damage = 5 x (3 x ATK + 5 x INT) = {15*self.Atk + 25*self.Int}"
        effect = "Def Shred: 0.5 x INT\nShock, Duration = 2, def shred per tick = 100 + 1 x BaseINT"
        if self.Int < 500 or self.Mana < 450:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 450,
                "dmg": 15*self.Atk + 25*self.Int,
                "Atk shred":0,
                "Def shred": 0.5*self.Int,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [True , 2 , 100 + 0.01*self.BaseINT],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":100,
                "Def Buff": 0 ,
                "Int Buff" : 50,
                "Mana Buff" : 0, 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List

    def Move_9(self):
        name = "Plague"
        description = "\nYou once again turn to the dark one. This time he gifts you with a deadly disease...\n"
        IntelligenceRequired = "Intelligence Required : 600"
        ManaCost = "Mana Cost : 600"
        damage = f"Damage = 2 x INT = {2*self.Int}"
        effect = "Def Shred: 2 x INT\nPoison, Duration = 4, damage per tick = 6 x INT , ATK shred per tick 0.3 x INT\n"
        if self.Int < 600 or self.Mana < 600:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : 600,
                "dmg": 2*self.Int,
                "Atk shred":0,
                "Def shred": 0.75*self.Int,
                "Burn" : [False , 0 , 0],
                "Poison" : [True, 5 , 6*self.Int ,0.3*self.Int],
                "Shock" : [False, 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0,
                "Mana Buff" : 0, 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        
    def Move_10(self):
        name = "HEX"
        description = "\nYou invoke the dark one unleash a fraction of his power, draining you but bringing hell on your enemy.\n"
        IntelligenceRequired = "Intelligence Required : 1000"
        ManaCost = "Minimum Mana Cost : 1000"
        damage = f"Damage = 10 x INT = {10*self.Int}"
        effect = "Gain all stats buff. Loose all your mana. Apply all DoT effects for three turns."
        if self.Int < 1000 or self.Mana < 1000:
            MoveDict = {
                "Cost" : self.Mana,
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Int Buff" : 0 ,
                "Mana Buff" : 0 , 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
        else: 
            MoveDict = {
                "Cost" : self.Mana,
                "dmg": 10*self.Int,
                "Atk shred":0.5*self.Int,
                "Def shred": 0.5*self.Int,
                "Burn" : [True , 3 , 6*self.Int],
                "Poison" : [True, 3 , 5*self.Int ,0.6*self.Int],
                "Shock" : [True, 3 , 0.8*self.Int],
                "Bleed" : [True , 3 , 3*self.Int , 0.8*self.Int],
                "heal" : 2000,
                "Atk Buff":100,
                "Def Buff":100 ,
                "Int Buff" : 200,
                "Mana Buff" : 0, 
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
            List = [name , description , IntelligenceRequired , ManaCost , damage , effect , MoveDict]
            return List
    
    def MoveList(self, num):
        move_methods = {
            1: self.Move_1,
            2: self.Move_2,
            3: self.Move_3,
            4: self.Move_4,
            5: self.Move_5,
            6: self.Move_6,
            7: self.Move_7,
            8: self.Move_8,
            9: self.Move_9,
            10: self.Move_10
        }
        return move_methods[num]()
    
    def current_stats(self):
        print(f"Hp = {self.Hp}")
        print(f"Atk = {self.Atk}")
        print(f"Def = {self.Def}")
        print(f"Int = {self.Int}")
        print(f"Mana = {self.Mana}")


    