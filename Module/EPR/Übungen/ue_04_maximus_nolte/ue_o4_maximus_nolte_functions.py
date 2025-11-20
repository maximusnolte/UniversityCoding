#! /venv/bin/python3.14

"""Dieses Modul enthält Funktionen für das schatzsuchspiel.
    Funktionen zum Erstellen und Verwalten der Spielkarte,
    Bewegen des Spielers und Berechnen der Manhattan-Distanz.
"""

__author__ = '8722674, Nolte'

import random

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
