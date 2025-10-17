__author__ = '<s5486426> , <Julian Maximus Nolte>'
#! /venv/bin/python3.14

#Python Programm, welches eine Bankleitzahl
# und eine Kontonummer, sowie ein gültiges Länderkürzel entgegennimmt
# und daraus die IBAN mit Prüfsumme bestimmt.


land = input("Länderkürzel: ")
bankleitzahl = input("Bankleitzahl: ")
kontonummer = input("Kontonummer: ")
if len(bankleitzahl) == 8 or len(kontonummer) <= 10:
    try:
        ibankleitzahl = int(bankleitzahl)
        ikontonummer = int(kontonummer)
    except ValueError:
        print("Falsche Eingabe!")
        quit()
else:
    print("Bankleitzahl oder Kontonummer ist nicht korrekt")
    quit()

if len(land) != 2:
    print("Länderkürzel falsch! ")


l_code = []
for char in land:
    l_code.append(ord(char)-55)

pruefziffer = "00"

output = bankleitzahl + kontonummer + str(l_code[0]) + str(l_code[1]) + pruefziffer
#print(output)
if len(output) == 24:
    rest = int(output) % 97
    pruefziffer = rest-98
    pruefziffer = abs(pruefziffer)
    #print(pruefziffer)
else:
    print("Fehler")

output = land + str(pruefziffer) + " "+ bankleitzahl + " " + kontonummer
print("\nIBAN:")
print(output)

#35070024
#0388249600