from player import Player
import world
from printf import printb
from collections import OrderedDict
from time import sleep

def play():
    print("Find the empire's plans!")
    sleep(1)
    world.parse_world_dsl()
    player = Player()


  
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("The empire has defeated you!")
          
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room,player)
        
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
          action()
        else:
          print("Invalid action!")
          
        


def get_available_actions(room, player):
  actions = OrderedDict()
  print("Choose an action: ")
  
  if isinstance(room, world.TraderTile):
      action_adder(actions, 'T', player.trade, "Trade")
          
      
  if player.inventory:
      action_adder(actions, 'I', player.print_inventory, "View inventory")
  if (isinstance(room, world.EnemyTile) and room.enemy.is_alive()) or (isinstance(room, world.BossTile) and room.enemy.is_alive()):
  
      action_adder(actions, 'A', player.attack, "Attack")
  else:
      if world.tile_at(room.x, room.y - 1):
          action_adder(actions, 'N', player.move_north, "Move north")

      if world.tile_at(room.x, room.y + 1):
          action_adder(actions, 'S', player.move_south, "Move south")

      if world.tile_at(room.x + 1, room.y):
          action_adder(actions, 'E', player.move_east, "Move east")
        
      if world.tile_at(room.x - 1, room.y):
          action_adder(actions, 'W', player.move_west, "Move west")
  if player.hp < 100:
      action_adder(actions, 'H', player.heal, "Use healing item")
 
  if isinstance(room, world.SecretTile) and room.seen_text:
      action_adder(actions, "?", player.secret, "???")
  if player.inventory:
    action_adder(actions, 'P', player.procrastinate, "Procrastinate")
  return actions
  



def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
