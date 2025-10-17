#Geschrieben für: Python3.14
from math import pi as pi #Nutzt math.pi für genauere Flächenberechnung
r = input("Gib den Radius als eine Zahl ein: ") #Programm erhält eine Zahl (auch komma) als Eingabe
try:
    r = float(r) #Eingabe wird zu FLoat convertiert
    A = r * r * pi #Formel der Kreis-Flächenberechnung wird angewandt
    print("Die Fläche ist: " + str(A)) #Fertiges Ergebnis wird ausgegeben
except ValueError: #Für Falscheingaben (Alles ausser eine normale Zahl)
    print("Falsche Eingabe!")

