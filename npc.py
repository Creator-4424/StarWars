import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("DO not create raw NPC objects.")

    def __str__(self):
      return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.credits = 500
        self.inventory = [items.EB(), items.Shield_Gen(), items.Shield_Gen_Up(), items.HealSpray(), items.HealSpray(), items.HealSpray(), items.B_Blade()]