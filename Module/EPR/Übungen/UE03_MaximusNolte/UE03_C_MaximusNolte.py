__author__ = '8722674, Julian Maximus Nolte'
#! /venv/bin/python3.14

def dezimal_zu_binär(number):
    original = number
    out = ""
    p = 1

    print(f"Starte Umwandlung von Dezimal → Binär für: {original}")
    print("--------------------------------------------------------")
    print("1) Bestimme die höchste Zweierpotenz, die ≤ Zahl ist.\n")

    # Bit-Anzahl bestimmen
    while 2 ** (p + 1) <= number:
        print(f"Teste Potenz 2^{p+1} = {2**(p+1)} … passt noch.")
        p += 1

    print(f"\nGefunden: höchste benötigte Potenz = 2^{p}")
    print(f"Benötigte Bit-Länge: {p+1}\n")

    print("2) Subtrahiere von oben nach unten jede Zweierpotenz.\n")

    # Bitweise Konstruktion
    for i in range(p, -1, -1):
        digit = 2 ** i
        print(f"Teste Bit {i}: Prüfe 2^{i} = {digit}")

        if number >= digit:
            print(f" → {digit} passt in {number}, setze Bit = 1")
            number -= digit
            out += "1"
            print(f"   Neuer Rest: {number}\n")
        else:
            print(f" → {digit} passt NICHT, setze Bit = 0\n")
            out += "0"

    # führende Nullen entfernen
    out = out.lstrip("0")
    print("3) Entferne führende Nullen (falls vorhanden).")

    print("\n--------------------------------------------------------")
    print(f"Ergebnis: {original} in Binär = {out}")
    print("--------------------------------------------------------\n")

    return True
