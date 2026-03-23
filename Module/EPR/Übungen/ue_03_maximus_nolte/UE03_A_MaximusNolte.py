"""Programm welches mit dem Nutzer zahlen-Raten zwischen -10 und 30 spielt"""

__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

import random

def zahlenRaten():
    """
    Die Funktion startet das Zahlen-Raten Spiel, wo ein Nutzer eine zufällig generierte Zahl zwischen -10 und 30
    erraten muss. Der Nutzer gibt eine zahl ein und es wird überprüft, ob diese größer, kleiner oder
    richtig geraten (gleich) ist und dementsprechend wird ein Hinweis ausgegeben.
    Das Spiel endet, sobald der Nutzer die richtige Zahl errät.
    Danach wird die Anzahl der benötigten Versuche ausgegeben.
    """
    print("Zahlen Raten einer Zahl zwischen -10 und 30")
    number = random.randint(-10, 30)
    guess = 0
    guess_count = 1
    while guess != number:
        guess = int(input("Guess My Number: "))
        if guess == number:
            print("You guessed my number in " + str(guess_count) + " guesses")
            break
        elif guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            print("An error occurred")
        guess_count += 1

    return True