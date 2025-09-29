class BaseStats:
    def __init__(self,BaseHP,BaseATK,BaseDef,BaseInt,BaseMana):
        self.BaseHP = BaseHP
        self.BaseATK = BaseATK
        self.BaseDEF = BaseDef
        self.BaseINT = BaseInt
        self.BaseMANA = BaseMana

class TypeStat(BaseStats):
    def __init__(self, BaseHP, BaseATK, BaseDef, BaseInt, BaseMana , Hp , Atk , Def , Int , Mana):
        super().__init__(BaseHP, BaseATK, BaseDef, BaseInt, BaseMana)
        self.Hp = BaseHP + Hp 
        self.Atk = BaseATK + Atk
        self.Def = BaseDef + Def
        self.Int = BaseInt + Int
        self.Mana = BaseMana + Mana

