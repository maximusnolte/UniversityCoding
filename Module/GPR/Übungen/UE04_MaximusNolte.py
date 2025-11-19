"""Programm zum Lösen Quadratischer Funktionen der Form: ax^2 + bx + c """

__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

import math as m
import cmath as cm

def abc_solver(a,b,c):
    """
    Die Methode löst quadratische Funktionen der Form: ax^2 + bx + c
    und gibt dann alle möglichen Lösungen aus (auch imaginäre, falls notwendig)
    es wird zwischen Reellen und Komplexen Lösungen unterschieden, sowie die Anzahl der Lösungen.
    Bei Eingaben für a,b,c werden alle reellen Zahlen, sowie die Unendlichkeit unterstützt.
    """
    try:
        if a == "inf":
            print("Rechnen wir mit der Unendlichkeit!!!")
            a = float("inf")
        if b == "inf":
            b = float("inf")
        if c == "inf":
            c = float("inf")

        a = float(a)
        b = float(b)
        c = float(c)
    except TypeError, ValueError:
        print("Falsche Eingabe")
        return None
    if a != 0:
        print(f"Löse die Formel: {a}x^2+{b}x+{c}")
        try:
            positive_solution = ((-b + m.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            negative_solution = ((-b - m.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            if positive_solution == negative_solution:
                print(f"Eine Lösung gefunden: {positive_solution}")
            else:
                print(f"Zwei Lösungen gefunden:\n{positive_solution}\n{negative_solution}")

        except ValueError:
            print("Keine Reele Lösung gefunden, versuche nun mit Komplexen Zahlen")
            positive_solution = ((-b + cm.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            negative_solution = ((-b - cm.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
            if positive_solution == negative_solution:
                print(f"Eine Lösung gefunden: {positive_solution}")
            else:
                print(f"Zwei Lösungen gefunden:\n{positive_solution}\n{negative_solution}")
    else:
        print("Fehler: a == 0!")

if __name__ == '__main__':
    a = input("gib eine Zahl für A ein")
    b = input("gib eine Zahl für B ein")
    c = input("gib eine Zahl für C ein")
    abc_solver(a,b,c)

