import items

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0
class Imp_Officer(Enemy):
    def __init__(self):
        self.name = "Imperial Officer"
        self.hp = 32
        self.damage = 12
        self.drops = [items.HealSpray(), items.Blaster()]
        self.credits = 35

class TIE_Pilot(Enemy):
    def __init__(self):
        self.name = "TIE Fighter Pilot"
        self.hp = 36
        self.damage = 8
        self.drops = [items.HealSpray()]
        self.credits = 15


class D_Star_Droid(Enemy):
    def __init__(self):
        self.name = "Death Star Droid"
        self.hp = 45
        self.damage = 6
        self.drops = None
        self.credits = 25


class Stormtrooper(Enemy):
    def __init__(self):
        self.name = "StormTrooper"
        self.hp = 25
        self.damage = 10
        self.drops = None
        self.credits = 15
class Urmom(Enemy):
    def __init__(self):
        self.name = "UrMom.com"
        self.hp = 1
        self.damage = 0
        self.drops = [items.D_Sword()]
        self.credits = 50
class RoyalGuard(Enemy):
    def __init__(self):
        self.name = "Royal guard"
        self.hp = 60
        self.damage = 20
        self.drops = None
        self.credits = 55