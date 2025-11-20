__author__ = '8722674, Nolte'
#! /venv/bin/python3.14

#Python Programm, welches eine Bankleitzahl
# und eine Kontonummer, sowie ein gültiges Länderkürzel entgegennimmt
# und daraus die IBAN mit Prüfsumme bestimmt.

def IBAN():
    print("Das Programm erhält ein Länderkürzel, eine Bankleitzahl \n"
          "mit maximal 8 Stellen und eine Kontonummer mit maximal 10 Stellen \n"
          "und bestimmt daraus die IBAN mit der Prüfsumme")
    land = input("Länderkürzel: ")
    if len(land) != 2:
        print("Länderkürzel falsch!, maximal 2 Buchstaben")
        quit()
    bankleitzahl = input("Bankleitzahl: ")
    kontonummer = input("Kontonummer: ")
    if len(bankleitzahl) == 8 or len(kontonummer) == 10:
        try:
            ibankleitzahl = int(bankleitzahl)
            ikontonummer = int(kontonummer)
        except ValueError:
            print("Falsche Eingabe!, die Bankleitzahl und Kontonummer dürfen nur Zahlen sein!")
            quit()
    else:
        print("Bankleitzahl oder Kontonummer ist nicht korrekt")
        quit()




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
        print("Fehler, falsche Bankleitzahl oder Kontonummer")
        quit()

    output = land + str(pruefziffer) + " "+ bankleitzahl + " " + kontonummer
    print("\nIBAN:")
    print(output)

#Errors aus Aufgabe 2:

def Name_Error(): #Variable existiert nicht und es wird versucht zuzugreifen
    print(x)

def Type_Error(): #Man versucht z.B. einen String mit einem Int zu addieren
    x = "1"
    y = 2
    z = x+y
    print(z)

def ZeroDivision_Error(): #Man darf nicht durch $0$ Teilen
    x = 0
    y = 2
    z = y/x
    print(z)

def Syntax_Error(): #Code nicht nach Syntax geschrieben
    #if x gleich y:
        print("z")

if __name__ == '__main__':
    #IBAN()
    #Name_Error()
    #TypeError()
    #ZeroDivision_Error()
    quit()