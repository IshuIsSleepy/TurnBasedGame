class Character:
    def __init__(self, level, name=""):
        self.name = name
        self.level = level
        self.BaseHP = 10000 + 10000 * level/100
        self.BaseAtk = 1000 + 1000 * level/100
        self.BaseDef = 1000 + 1000 * level/100 
        self.BaseSpeed = 50
        self.BaseAlignment = 50
        self.CritRate = 0.10
        self.CritDmg = 0.50
        self.Allegiance = None
        self.Current_Vitality = 0 
        self.MaxVitality = 100 
        self.Affinities = {
            "Neutral": 0.0, "Light": 0.0, "Dark": 0.0, "Chaos": 0.0, "Serenity": 0.0, "Abyssal": 0.0, "Heavenly": 0.0, "Void": 0.0
        }
        self.Aversions = {
            "Neutral": 0.0, "Light": 0.1, "Dark": 0.1, "Chaos": 0.1,"Serenity": 0.1, "Abyssal": 0.1, "Heavenly": 0.1, "Void": 0.15
        }
        self.MovePool = [] 
        self.Passive1 = None
        self.Passive2 = None #Only for Neutral characters 
        self.NeutralizationAbility = None
        self.NeutralizeActive = False #whether character is capable of neutralizing 
        self.ConsumptionStacks = None 

class Tank(Character):
    def __init__(self, level, name=""):
        super().__init__(level, name)
        self.BaseHP *= 1.5
        self.BaseAtk *= 0.8
        self.BaseDef *= 1.5
        self.BaseSpeed *= 0.8
        for Allegiance in self.Aversions:
            self.Aversions[Allegiance] += 0.05

class DPS(Character):
    def __init__(self, level, name=""):
        super().__init__(level, name)
        self.BaseHP *= 1.0
        self.BaseAtk *= 1.2
        self.BaseDef *= 0.9
        self.BaseSpeed *= 1.1
        for Allegiance in self.Affinities:
            self.Affinities[Allegiance] += 0.10
        for Allegiance in self.Aversions:
            self.Aversions[Allegiance] -= 0.05

class SubDps(Character): 
    def __init__(self,level,name=""):
        super().__init__(level , name) 
        self.BaseHP *= 0.9 
        self.BaseAtk *= 1.1 
        self.BaseDef *= 0.9 
        self.BaseSpeed *= 1.2 
        self.BaseAlignment += 15
        for Allegiance in self.Affinities:
            self.Affinities[Allegiance] += 0.10
        for Allegiance in self.Aversions:
            self.Aversions[Allegiance] -= 0.05

class Support(Character):
    def __init__(self,level,name=""):
        super().__init__(level , name)
        self.BaseHP *= 0.9 
        self.BaseAtk *= 0.85 
        self.BaseDef *= 0.85 
        self.BaseAlignment += 25 
        for Allegiance in self.Aversions:
            self.Aversions[Allegiance] -= 0.1 

class Boss(Character):
    def __init__(self, level, name=""):
        super().__init__(level, name)
        self.BaseHP = 100000 + 10000 * level
        self.BaseAtk *= 3
        self.BaseDef *= 2
        self.CritRate = 0.0
        self.CritDmg = 0.0
        for Allegiance in self.Aversions:
            self.Aversions[Allegiance] += 0.15
        self.NeutralizeWho = None #who all are applicable for neutralizing 