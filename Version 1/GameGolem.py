from GameBaseStats import TypeStat 

class Golem(TypeStat):
    def __init__(self, BaseHP, BaseATK, BaseDef, Hp, Atk, Def):
        self.Hp = BaseHP + Hp
        self.Atk = BaseATK + Atk
        self.Def = BaseDef + Def

    def Move_1(self):
        name = "Build Up"
        description = "\nThe golem picks up rocks and heals it self"
        MoveDict = {
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Int shred":0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0.01*self.Hp,
                "Atk Buff":0,
                "Def Buff": 0 ,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_2(self):
        name = "bulk up"
        description = "\nThe Golem strengthens its defenses"
        MoveDict = {
                "dmg":0,
                "Atk shred":0,
                "Def shred": 0,
                "Int shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 1000 + 0.001*self.Hp,
                "Atk Buff":0,
                "Def Buff": 0.1*self.Def ,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_3(self):
        name = "Hurl"
        description = "\nThe golem hurls a boulder at you."
        MoveDict = {
                "dmg":0.8*self.Atk,
                "Atk shred":0,
                "Def shred": 0,
                "Int shred": 0,
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

    def Move_4(self):
        name = "Growl"
        description = "\nThe Golem intimidates you with its deep but loud growl."
        MoveDict = {
                "dmg":0.08*self.Atk,
                "Atk shred":0,
                "Def shred": 300,
                "Int shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
                "Bleed" : [False , 0 , 0 , 0],
                "heal" : 0,
                "Atk Buff":100,
                "Def Buff": 200,
                "Self Burn" : [False , 0 , 0],
                "Self Bleed" : [False , 0 , 0 , 0],
            }
        List = [name , description ,MoveDict]
        return List

    def Move_5(self):
        name = "Roll"
        description = "This big golem is coming your way...."
        MoveDict = {
                "dmg":4*self.Atk,
                "Atk shred":0,
                "Def shred": 200,
                "Int shred": 0,
                "Burn" : [False , 0 , 0],
                "Poison" : [False , 0 , 0 , 0],
                "Shock" : [False , 0 , 0],
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
