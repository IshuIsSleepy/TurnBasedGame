from GameBaseStats import TypeStat 

class Dragon(TypeStat):
    def __init__(self, BaseHP, BaseATK, BaseDef, Hp, Atk, Def):
        self.Hp = BaseHP + Hp
        self.Atk = BaseATK + Atk
        self.Def = BaseDef + Def

    def Move_1(self):
        name = "Dragon Slash"
        description = "\nThe Dragon has been sharpening its claws using the volcanic rocks.\nIt now slashes at you with them!!!\n"
        MoveDict = {
                "dmg":1*self.Atk,
                "Atk shred":0,
                "Def shred": 0,
                "Int shred":0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_2(self):
        name = "Dragon Roar"
        description = "\nThe Dragon channels its energy volcanic energy and roars loudly, shaking the earth it self!!!!\nnIt buffs it self and de buffs you.\n"
        MoveDict = {
                "dmg":0.5*self.Atk,
                "Atk shred":0,
                "Def shred": 300,
                "Int shred": 200,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 1000 + 0.01*self.Hp,
                "Atk Buff":0.1*self.Atk,
                "Def Buff": 100 ,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_3(self):
        name = "Fire ball"
        description = "\nThe Mighty Dragon hurls a fireball at you, which explodes into flames.\nThe fires buffs it as well.\n"
        MoveDict = {
                "dmg":0.6*self.Atk,
                "Atk shred":0,
                "Def shred": 0,
                "Int shred": 0,
                "Burn" : [True , 3 , 200],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0.1*self.Atk,
                "Def Buff": 100 ,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_4(self):
        name = "Dragon Breath"
        description = "\nThe Dragon channels its volcanic powers and breaths bright and hot flames at you!!!!\nIt even converts nearby sand into glass!!!!\n"
        MoveDict = {
                "dmg":0.5*self.Atk,
                "Atk shred":0,
                "Def shred": 100,
                "Int shred": 0,
                "Burn" : [True , 5 , 600],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":0,
                "Def Buff": 0,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_5(self):
        name = "Dragon Ascent"
        description = "The Dragon now uses its wings...It flies high above the clouds, stealing their thunder.\nIt then comes crashing down at you."
        MoveDict = {
                "dmg":4*self.Atk,
                "Atk shred":0,
                "Def shred": 200,
                "Int shred": 100,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [True , 3 , 30],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : -1000,
                "Atk Buff":200,
                "Def Buff": 100 ,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List
    
    def MoveList(self, num):
        move_methods = {
            1: self.Move_1,
            2: self.Move_2,
            3: self.Move_3,
            4: self.Move_4,
            5: self.Move_5
        }
        return move_methods[num]()
    
    def current_stats(self):
        print(f"Hp = {self.Hp}")
        print(f"Atk = {self.Atk}")
        print(f"Def = {self.Def}")

    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                



