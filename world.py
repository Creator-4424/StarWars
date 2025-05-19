import enemies
import random
from time import sleep
import npc
from printf import printb

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
      pass


class StartTile(MapTile):
    def intro_text(self):
        print ("""
\t\tYou are in the hangar where the rebellion covertly deployed you
""")
        sleep(1)
class DETERMINATION(MapTile):
  def intro_text(self):
        print("""
\t\tKeep going""")

class BIGSECRET(MapTile):
  def intro_text(self):
    creditcount = 0
    if creditcount == 0:
      sleep(3)
      print("""
      You made it :)""")
      sleep(1)
      printb("""You are brave to have come this far. A hero rises to right the wrongs of this world. since you have made this great journey, I shall reward you. """)
      sleep(9)
      print("""
      With the credits!
      """)
      sleep(2)
      printb ("""
      ------------------:STAR WARS TEXT ADVENTURE CREDITS:------------------
      """,0.01)
      sleep(1)
      printb ("""
      \n \n \nLEAD DEVELOPMENT: ------------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nMAIN GAME DESIGN: ------------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nENEMY DESIGN: ----------------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nWEAPONS DESIGN: --------------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nHEALING ITEM DESIGN: ---------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nSTORY DESIGN: ----------------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nPROGRAMMING LEAD: ------------------------------------------------LUCA
      """,0.01)
      printb ("""
      \nGRAPHIC DESIGN: -------------------------------------------Wait, what?
      """,0.01)
      printb ("""
      \nMUSIC COMPOSITION: -----------------------------------------------Huh?
      """,0.01)
      printb ("""
      \nLEAD LOCALIZATION EFFORTS: ----------------------------------------???
      """,0.01)
      printb ("""
      \nMAIN ARTWORK DESIGN: ------------ Ok I'm done.
      """,0.01)
      sleep(2)
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Stormtrooper()
            self.alive_text = "\t\tYou encounter a stormtrooper, who immediately draws their blaster."
            self.dead_text = "\t\tThe stormtrooper you killed lies idly on the ground."
        elif r < 0.80:
            self.enemy = enemies.TIE_Pilot()
            self.alive_text = "\t\tA TIE fighter pilot confronts you on their way to the hangar!"
            self.dead_text = "\t\tThe TIE fighter pilot will not be getting to the hangar."
        elif r < 0.95:
            self.enemy = enemies.Imp_Officer()
            self.alive_text = "\t\tAn imperial officer catches you sneaking around and draws his blaster."
            self.dead_text = "\t\tHidden in a loose panel, is the imperial officer you defeated."
        elif r < 0.99:
            self.enemy = enemies.Urmom()
            self.alive_text = "\t\tA wild UrMom.com appears!"
            self.dead_text = "\t\tYour mom died here."
        else:
            self.enemy = enemies.D_Star_Droid()
            self.alive_text = "\t\tA droid wandering through the hall finds you and prepares to attack!"
            self.dead_text = "\t\tBits and pieces of a destroyed droid lie on the ground."

        super().__init__(x, y)




    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        print(text)
        print()
        print()
        sleep(1)

    def modify_player(self, player):
        if self.enemy.is_alive():
            best_armor = player.most_powerful_armor()
            try:
              player.hp = player.hp - (self.enemy.damage - int((best_armor.defense * self.enemy.damage)))
            except AttributeError:
              player.hp = player.hp - self.enemy.damage
            try:
              if player.hp <= 0:
                  print(f"\t\tEnemy does {self.enemy.damage - int((best_armor.defense * self.enemy.damage))} damage. You have 0 HP remaining.")
              else:
                  print(f"\t\tEnemy does {self.enemy.damage - int((best_armor.defense * self.enemy.damage))} damage. You have {player.hp} HP remaining.")
              sleep(1)
            except AttributeError:
              if player.hp <= 0:
                  print(f"\t\tEnemy does {self.enemy.damage} damage. You have 0 HP remaining.")
              else:
                  print(f"\t\tEnemy does {self.enemy.damage} damage. You have {player.hp} HP remaining.")
              sleep(1)
  
class BossTile(MapTile):
    def __init__(self, x, y):
        self.enemy = enemies.RoyalGuard()
        self.alive_text = "\t\tAn imperial royal gaurd stands in front of you, ready to attack"
        self.dead_text = "\t\tThe royal gaurd lies vanquished in front of you. The empires files must be close!"
        super().__init__(x, y)




    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        print(text)
        print()
        print()
        sleep(1)

    def modify_player(self, player):
        if self.enemy.is_alive():
            best_armor = player.most_powerful_armor()
            try:
              player.hp = player.hp - (self.enemy.damage - int((best_armor.defense * self.enemy.damage)))
            except AttributeError:
              player.hp = player.hp - self.enemy.damage
            try:
              if player.hp <= 0:
                  print(f"\t\tEnemy does {self.enemy.damage - int((best_armor.defense * self.enemy.damage))} damage. You have 0 HP remaining.")
              else:
                  print(f"\t\tEnemy does {self.enemy.damage - int((best_armor.defense * self.enemy.damage))} damage. You have {player.hp} HP remaining.")
              sleep(1)
            except AttributeError:
              if player.hp <= 0:
                  print(f"\t\tEnemy does {self.enemy.damage} damage. You have 0 HP remaining.")
              else:
                  print(f"\t\tEnemy does {self.enemy.damage} damage. You have {player.hp} HP remaining.")
              sleep(1)

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Credits".format(i, item.name,
item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")

            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError or IndexError:

                  print("Invalid choice!")
    def swap(self, seller, buyer, item):
        if item.value > buyer.credits:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.credits = seller.credits + item.value
        buyer.credits = buyer.credits - item.value
        print("Trade complete!")
    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")

            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")
    def intro_text(self):
        print("an imperial officer eyes you warily. You draw your blaster, but you find he is a spy. he has many materials that could be of use to you")


class VictoryTile(MapTile):
    def modify_player(self,player):
        player.victory = True
    def intro_text(self):
        print("""\t\tYou arrive in a vast room. at last! the empire's plans! you download all of their secret files and head to the hangar where the rebel ship awaits your arrival. you hop on, and fly off into the distance, never to be seen again""")
        print()
        sleep(1)
        print("""\t\tYou Win!
               """)
        
class HallTile(MapTile):
  def intro_text(self):
    print("\t\tYou are in a regular hallway. nothing to see here")
    sleep(1)

class FindCreditsTile(MapTile):
    def __init__(self, x, y):
        self.credits = random.randint(1, 50)
        self.credits_claimed = False
        super().__init__(x, y)
    
    def modify_player(self, player):
        if not self.credits_claimed:
            self.credits_claimed = True
            player.credits = player.credits + self.credits
            print("you find some dropped credits and run to pick them up\n")
            sleep(1)
            print("+{} credits added.".format(self.credits))
    
    def intro_text(self):
        if self.credits_claimed:
            print("\t\tYou are in a regular hallway. nothing to see here\n")
            sleep(1)

          
class SecretTile(MapTile):
    def __init__(self, x, y):
        self.seen_text = False
        super().__init__(x, y)
    def intro_text(self):
        if self.seen_text:
            print("\t\tYou are in a regular hallway. nothing to see here\n")
            sleep(1)
        if self.seen_text == False:
            self.seen_text = True
            print("\t\tYou are in a regular hallway. nothing to see here\n")
            sleep(1)
          

world_dsl = """
|  |  |  |  |VT|FC|FC|FC|  |  |
|  |  |  |  |BT|  |  |BT|XX|XX|
|TT|  |TT|BT|FC|  |  |BT|  |XX|
|EN|  |FC|  |  |  |  |SC|  |XX|
|FC|  |EN|  |  |  |  |EN|  |XX|
|EN|TT|FC|EN|EN|  |  |EN|  |XX|
|  |EN|  |  |EN|FC|  |TT|  |XX|
|EN|FC|EN|  |TT|  |  |EN|  |XX|
|TT|  |ST|FC|EN|  |  |EN|  |XX|
|FC|  |EN|  |FC|TT|FC|EN|  |BS|
"""
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    
    return True
tile_type_dict = {"VT": VictoryTile, 
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FC": FindCreditsTile,
                  "TT": TraderTile,
                  "SC": SecretTile,
                  "BT": BossTile,
                  "XX": DETERMINATION,
                  "BS": BIGSECRET,
                  "  ": None}

world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else
None)
        world_map.append(row)
      
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
