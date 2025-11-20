__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

# Aufgabe 2, Handlungsvorschrift 1:

a = input("Gib die erste Zahl a ein: ")
b = input("Gib die zweite Zahl b ein: ")

a = int(a)
b = int(b)

while b != 0:
    h = a % b
    a = b
    b = h
print("Der größte gemeinsame Teiler ist: ", a)

