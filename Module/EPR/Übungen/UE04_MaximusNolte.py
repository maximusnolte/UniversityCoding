import numpy as np
import random as rnd

def create_map():
    output = []
    for j in range(0, 5):
        output.append([])
        for i in range(0, 5):
            output[j].append(".")
    return output

def place_element(game_map, element):
    rnd_x = rnd.randint(0, len(game_map))
    rnd_y = rnd.randint(0, len(game_map[0]))

    if game_map[rnd_x][rnd_y] == ".":
        return rnd_x, rnd_y
    else:
        return None

def print_map(game_map):
    for i in game_map:
        for j in i:
            print(j + " ", end=" ")
        print()

def move_player(position, direction, game_map, obstacles):
    map_size_x = len(game_map)
    map_size_y = len(game_map[0])

    if position[0] > map_size_x or position[0] < 0 or position[1] > map_size_y or position[1] < 0:
        raise Exception("Position out of bounds")



if __name__ == '__main__':
    map = create_map()
    move_player([0,0],"l", map, None)