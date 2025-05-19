# import player

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return "{} ({} damage)".format(self.name, self.damage)


class Blaster(Weapon):
    def __init__(self):
        self.name = "Blaster"
        self.description = "A decently powerful blaster. it can be helpful in a pinch"
        self.damage = 10
        self.value = 30


class EB(Weapon):
    def __init__(self):
        self.name = "Enhanced Blaster"
        self.description = "Stronger than a regular blaster, but still not incredibly powerful"
        self.damage = 18
        self.value = 50


class D_Sword(Weapon):
    def __init__(self):
        self.name = "Minecraft Diamond Sword"
        self.description = "IT'S THE DIAMOND SWORD FROM MINECRAFT@#^&^)#%^@&@^@#$%^&*(*&^%Rn^TFY&*UT%*Y(^^#$&*%"
        self.damage = 9999999999999999999999999999999999
        self.value = 9999999999999999999999999999999999

class B_Blade(Weapon):
    def __init__(self):
        self.name = "Bidoof Blade"
        self.description = "Doof"
        self.damage = 1
        self.value = 13

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class HealSpray(Consumable):
    def __init__(self):
        self.name = "Bacta Healing Spray"
        self.healing_value = 20
        self.value = 20
class Armor():
    def __init__(self):
        raise NotImplementedError("Do not create raw Armor objects.")
    def __str__(self):
        return "{} (+{}% defense)".format(self.name, self.str_def)

class Shield_Gen(Armor):
    def __init__(self):
        self.name = "Shield generator"
        self.Defense = 0.25
        self.str_def = 25
        self.value = 55

class Shield_Gen_Up(Armor):
    def __init__(self):
        self.name = "Upgraded shield generator"
        self.defense = 0.50
        self.str_def = 50
        self.value = 70
class M_Armor(Armor):
    def __init__(self):
        self.name = "Magic Armor"
        self.defense = 1
        self.str_def = 100
        self.value = 9999999999999999999999999999999999999999
class Misc():
    def __init__(self):
        raise NotImplementedError("Do not create raw Miscellaneous objects.")
    def __str__(self):
        return "{}".format(self.name)
  
# class Test(Misc):
#     def __init__(self):
#         self.name = "buy me :)"
#         self.value = 1 + player.credits()