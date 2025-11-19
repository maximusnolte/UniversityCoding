#! /venv/bin/python3.14

"""Ein einfaches Schatzsuchspiel in der Konsole.
    Der Spieler muss den Schatz auf einer 5x5 Karte finden,
    indem er sich bewegt und Hindernissen ausweicht.
    Der Spieler hat eine begrenzte Anzahl von Zügen, um den Schatz zu finden.
"""

__author__ = '8722674, Nolte'

import random
import sys


def create_map():
    """Erzeugt eine 5x5 Karte"""
    output = []
    for y in range(5):
        output.append([])
        for _ in range(5):
            output[y].append(".")
    return output


def place_element(game_map, element):
    """Platziert ein Element zufällig auf der Karte"""
    rnd_y = random.randint(0, len(game_map)-1)
    rnd_x = random.randint(1, len(game_map[0])-1)

    if game_map[rnd_y][rnd_x] == ".":
        return rnd_y, rnd_x
    return None


def fill_map(game_map, obstacle_count):
    """Füllt die Karte mit Hindernissen und einem Schatz"""
    obstacles = []
    for _ in range(obstacle_count):
        element_pos = list(place_element(game_map, ""))
        while element_pos is None or element_pos in obstacles:
            element_pos = list(place_element(game_map, ""))
        obstacles.append(element_pos)
    element_pos = place_element(game_map, "")
    while element_pos is None or element_pos in obstacles:
        element_pos = list(place_element(game_map, ""))
    obstacles.append(element_pos)
    return obstacles


def print_map(game_map):
    """Gibt die Karte in der Konsole aus"""
    for y in game_map:
        for x in y:
            print(x + " ", end=" ")
        print()


def manhattan_distance(point1, point2):
    """Berechnet die Manhattan-Distanz zwischen zwei Punkten"""
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def move_player(position, direction, game_map, obstacles):
    """Bewegt den Spieler in die angegebene Richtung, wenn möglich"""
    map_size_y = len(game_map)-1
    map_size_x = len(game_map[0])-1

    y = position[0]
    x = position[1]

    updated_position = []

    match direction:
        case "d":
            if y+1 <= map_size_y:
                if [y+1, x] not in obstacles:
                    updated_position = [y+1, x]
                else:
                    updated_position = [-(y+1), -x]
        case "u":
            if y-1 >= 0:
                if [y-1, x] not in obstacles:
                    updated_position = [y-1, x]
                else:
                    updated_position = [-(y-1), -x]
        case "r":
            if x + 1 <= map_size_x:
                if [y, x+1] not in obstacles:
                    updated_position = [y, x+1]
                else:
                    updated_position = [-y, -(x+1)]
        case "l":
            if x-1 >= 0:
                if [y, x-1] not in obstacles:
                    updated_position = [y, x-1]
                else:
                    updated_position = [-y, -(x-1)]
        case _:
            pass
            # raise Exception(f"Invalid direction '{direction}'")
    return updated_position


def treasure_hunter_game():
    """Hauptfunktion für das Schatzsuchspiel"""
    game_map = create_map()

    obstacle_count = 1
    max_try = 10

    position = [0, 0]
    try_counter = 0

    obstacles = fill_map(game_map, obstacle_count)
    treasure = list(obstacles[-1])
    obstacles.pop()

    # print("--------DEBUG--------")
    # print(f"{len(obstacles)} Obstacle/s at {obstacles}")
    # print(f"Treasure at {treasure}")

    print("-------ERKLÄRUNG--------")
    print("Du kannst dich mit 'u', 'o', 'l', 'r' Bewegen")
    print("Um das Spiel zu beenden gib 'q' ein")
    print(f"Du hast maximal {max_try} Versuche um den Schatz zu finden")

    print("--------GAME--------")
    game_map[position[0]][position[1]] = "P"
    print_map(game_map)
    distance = manhattan_distance(position, treasure)
    print(f"Distanz zum Schatz: {distance}")

    while True:
        command = input(">")
        if command != "q" and try_counter < max_try:
            old_position = position
            position = move_player(old_position,  command, game_map, obstacles)
            if position:
                if position[0] >= 0 and position[1] >= 0:
                    if position != old_position:
                        try_counter += 1
                    if position != treasure:
                        game_map[old_position[0]][old_position[1]] = "."
                        game_map[position[0]][position[1]] = "P"
                    else:
                        game_map[old_position[0]][old_position[1]] = "."
                        game_map[position[0]][position[1]] = "X"
                        print("\n-------GEWONNEN-------")
                        print_map(game_map)
                        print(f"Du hast den Schatz in {try_counter}"
                              f"-Versuchen gefunden!")
                        sys.exit()
                else:
                    game_map[-position[0]][-position[1]] = "O"
                    position = old_position
            else:
                position = old_position
            print_map(game_map)
            distance = manhattan_distance(position, treasure)
            print(f"Distanz zum Schatz: {distance}")
            print(f"Versuch: {try_counter}")
        else:
            print("Spiel beendet... :(")
            sys.exit()


if __name__ == '__main__':
    treasure_hunter_game()
