# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
  print("INFO")

  return {
    "apiversion": "1",
    "author": "Josua Christyanton, Robert Chung",  # TODO: Your Battlesnake Username
    "color": "#006ee6",  # TODO: Choose color
    "head": "default",  # TODO: Choose head
    "tail": "default",  # TODO: Choose tail
  }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
  print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
  print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:
  is_move_safe = {"up": True, "down": True, "left": True, "right": True}

  # We've included code to prevent your Battlesnake from moving backwards
  my_head = game_state["you"]["body"][0]  # Coordinates of your head

  # my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"

  board_width = game_state['board']['width']
  board_height = game_state['board']['height']

  my_body = game_state['you']['body']
  my_body_nohead = my_body[1:]

  # Potential positions of head
  potential_coordinates = {
    "up": {
      "x": my_head["x"],
      "y": my_head["y"] + 1
    },
    "down": {
      "x": my_head["x"],
      "y": my_head["y"] - 1
    },
    "right": {
      "x": my_head["x"] + 1,
      "y": my_head["y"]
    },
    "left": {
      "x": my_head["x"] - 1,
      "y": my_head["y"]
    }
  }

  # getting direction of head as key values
  for key in potential_coordinates:
    potential_my_head = potential_coordinates[key]
    # compare the x and y values of potential positions of snake head with border
    if potential_my_head["x"] == -1 or potential_my_head[
        "x"] == board_width or potential_my_head[
          "y"] == -1 or potential_my_head["y"] == board_height:
      is_move_safe[key] = False
      # exit after this check if false
      continue
      # compare potential position of snake head with its own body
    if potential_coordinates[key] in my_body_nohead:
      is_move_safe[key] = False
      # exit after this check if false
      continue
      print(potential_my_head)

  print(my_body_nohead)
  print("==============================")

  # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
  # opponents = game_state['board']['snakes']

  # Are there any safe moves left?
  safe_moves = []
  for move, isSafe in is_move_safe.items():
    if isSafe:
      safe_moves.append(move)
  print(safe_moves)
  if len(safe_moves) == 0:
    print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
    return {"move": "down"}

  # Choose a random move from the safe ones
  next_move = random.choice(safe_moves)

  # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
  # food = game_state['board']['food']

  print(f"MOVE {game_state['turn']}: {next_move}")
  return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
  from server import run_server

  run_server({"info": info, "start": start, "move": move, "end": end})

