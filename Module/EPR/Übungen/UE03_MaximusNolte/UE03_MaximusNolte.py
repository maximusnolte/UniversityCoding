__author__ = '8722674, Julian Maximus Nolte'
#! /venv/bin/python3.14

import UE03_A_MaximusNolte as aufgabe_a
import UE03_B_MaximusNolte as aufgabe_b
import UE03_C_MaximusNolte as aufgabe_c

def ue_03():
    """
    Steuert die Auswahl und Ausführung der drei Teilprogramme der Übungsaufgabe 03.

    Der Nutzer wird aufgefordert, eines der verfügbaren Unterprogramme auszuwählen:
    A, B oder C daraufhin wird das Unterprogramm gestartet und nach dem Abschluss des Programms wird die Abfrage neu gestartet.
    """
    eingabe = input(f'\nWähle dein Unterprogramm aus: \nZahlenraten (A)\nDreieck-Fraktal (B)\nBinärZuDezimal (C)\n')
    match eingabe:
        case 'A':
           while not aufgabe_a.zahlenRaten():
                pass
           print(f"\nFinished A")
        case 'B':
            eingabe = input("Wie viele Iterationen? ")
            eingabe = int(eingabe)
            while not aufgabe_b.dreieckFraktal(eingabe):
                pass
            print(f"\nFinished B")
        case 'C':
            eingabe = input("Gib eine ganzzahlige Dezimal Zahl ein: ")
            eingabe = int(eingabe)
            while not aufgabe_c.dezimal_zu_binär(eingabe):
                pass
            print(f"Finished C")

if __name__ == '__main__':
    while True:
        ue_03()