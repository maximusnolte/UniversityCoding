"""Schatzsuchspiel Modul
    dieses Modul enthält die Hauptfunktion für das Schatzsuchspiel.
    Der Spieler kann sich auf einer Karte bewegen, Hindernissen ausweichen
    und versucht, einen versteckten Schatz zu finden.
    Als hilfe werden die Manhattan-Distanz zum Schatz und die Anzahl der Versuche angezeigt.
    Er hat 10 Versuche, um den Schatz zu finden.
"""

import sys
from ue_o4_maximus_nolte_functions import (create_map, fill_map, print_map,
                                            manhattan_distance, move_player)
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
