__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

# Aufgabe 2)
def schalt_jahr_checker():

    #Liest eine Jahreszahl ein und prüft, ob es sich um ein Schaltjahr handelt.
    #Nimmt nur gültige ganze Zahlen an.

    while True:
        jahr = input("Gib dein Jahr ein: ")
        if not jahr.isdigit():
            print("Ungültige Eingabe! Bitte gib eine ganze Zahl ein.")
            continue
        jahr = int(jahr)
        break

    if ((jahr % 4 == 0) and (jahr % 100 != 0)) or (jahr % 400 == 0):
        print(f"{jahr} ist ein Schaltjahr!")
    else:
        print(f"{jahr} ist KEIN Schaltjahr!")


# Aufgabe 3)
def katzen_futter_berater():

    #Liest das Alter und die Haltungsart einer Katze ein und gibt eine Futterempfehlung.
    #Akzeptiert nur gültige Eingaben und wiederholt bei Fehlern.

    gueltige_alter = ["jung", "erwachsen", "senior"]
    gueltige_haltungsarten = ["haus", "frei"]

    while True:
        alter = input("Gib das Alter (jung, erwachsen, senior) deiner Katze ein: ").lower().strip()
        if alter not in gueltige_alter:
            print("Ungültige Eingabe für Alter! Bitte gib 'jung', 'erwachsen' oder 'senior' ein.")
            continue
        break

    while True:
        haltungsart = input("Gib die Haltungsart (haus, frei) deiner Katze ein: ").lower().strip()
        if haltungsart not in gueltige_haltungsarten:
            print("Ungültige Eingabe für Haltungsart! Bitte gib 'haus' oder 'frei' ein.")
            continue
        break

    print("\nDein empfohlenes Futter ist:")

    match alter, haltungsart:
        case "jung", "haus":
            print("Kittenfutter für Wohnungskatzen")
        case "jung", "frei":
            print("Kittenfutter für Freigängerkatzen")
        case "erwachsen", ("haus" | "frei"):
            print("Nass- und Trockenfutter für erwachsene Katzen")
        case "senior", ("haus" | "frei"):
            print("Nassfutter für Senior-Katzen")
        case _:
            print("Keine Empfehlung verfügbar – Eingabe unbekannt.")


if __name__ == '__main__':
    # schalt_jahr_checker()
    katzen_futter_berater()
