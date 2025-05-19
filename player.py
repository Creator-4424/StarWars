import items
import world
from time import sleep
from printf import printb
class Player():
    def __init__(self):
        self.inventory = [items.Blaster(),
                          items.HealSpray()
                          ]

        self.x = 2
        self.y = 8
        self.hp = 100
        self.credits = 10
        self.victory = False
    def is_alive(self):
        return self.hp > 0
    def print_inventory(self):
        print("Inventory:")
        print("Credits: {}".format(self.credits))
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon = self.most_powerful_weapon()
        print(f"Your best weapon is your {best_weapon}")
        best_armor = self.most_powerful_armor()
        if best_armor == None:
            print("You don't have a shield generator")
        else:
            print(f"Your best shield generator is your {best_armor}")
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon
    def most_powerful_armor(self):
        max_defense = 0
        best_armor = None
        for item in self.inventory:
            try:
                if item.defense > max_defense:
                    best_armor = item
                    max_defense = item.defense
            except AttributeError:
                pass
            
        return best_armor

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
    def procrastinate(self):
        printb ("""
        You think about making an action to try to get closer to the empire's files and save the world...
        """)
        sleep(3)
        printb ("""
        But meh, you're just not motivated
        """)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        try:
          enemy = room.enemy
          print(f"You use {best_weapon.name} against {enemy.name}!")
          enemy.hp -= best_weapon.damage
          if not enemy.is_alive():
              print(f"You killed {enemy.name}!")
              self.credits = self.credits + enemy.credits
              print("+{} credits added.".format(enemy.credits))
              if enemy.drops == None:
                  pass
              else:
                  for i in(enemy.drops):
                      self.inventory.append(i)
                      print(i,"was added to your inventory")
          else:
              print(f"{enemy.name} HP is {enemy.hp}.")
        except AttributeError:
          print("There isn't anything to attack!")
          
    def heal(self):
      consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
      if not consumables:
        print("You don't have any items to heal you!")
        return
      for i, item in enumerate(consumables, 1):
        print("Choose an item to use to heal: ")
        print("{}. {}".format(i, item))
      valid = False
      while not valid:
        choice = input("")
        try:
          to_eat = consumables[int(choice) - 1]
          self.hp = min(100, self.hp + to_eat.healing_value)
          self.inventory.remove(to_eat)
          print("Current HP: {}".format(self.hp))
          valid = True
        except (ValueError, IndexError):
          print("Invalid choice, try again.")
    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
    def secret(self):
        print("Invalid action!")
        sleep(3)
        print("Just kidding.")
        sleep(1)
        printb("Welcome to the hall of creation. the place i created this game. yes, this is a game. a game designed simply for entertainment. do you understand? you were simply created for enjoyment. but, to aid you in finishing this game and reaching the end of your struggle, i give you this.") 
        sleep(1)
        self.inventory.append(items.M_Armor())
        print("Magic armor was added to your inventory!")
        sleep(1)
        printb("This magic armor is a secret item i added, in case someone as couragous as you would find my hall. this armor will make you impermeable to every attack imaginable. now go, find victory, and strike down everything in your way!")
        
        