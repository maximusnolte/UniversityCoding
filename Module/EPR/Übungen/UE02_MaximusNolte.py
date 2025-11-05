__author__ = '8722674, Julian Maximus Nolte'
#! /venv/bin/python3.14

# Aufgabe 2)
#a)
def aufgabe_zwei_a(zahl1, zahl2):
    # Eine Funktion, welche zwei Ganzzahlen entgegennimmt und über beiden Zahlen und
    # den dazwischen liegenden Zahlen die Summe bildet
    ergebnis = 0
    if zahl1 > zahl2:
        temp = zahl1
        zahl1 = zahl2
        zahl2 = temp
    for i in range(zahl1, zahl2+1, 1):
        ergebnis += i
    return ergebnis
    #Tests:
        # aufgabe_zwei_a(-1, 5) ->14
        #aufgabe_zwei_a(5,-1) -> 14
        # aufgabe_zwei_a(5,5) -> 5

def aufgabe_zwei_b(zahl):
    #Eine Funktion, die eine Zahl (ungleich 0) so lange halbiert, bis sie nicht mehr darzustellen ist
    #und die Anzahl an benötigter schritte angibt
    if(zahl != 0):
        ergebnis = zahl
        while(zahl > 0):
            zahl = zahl / 2
            ergebnis += 1
    else: ergebnis = "Eingegebene Zahl war 0"
    return ergebnis
    #Tests:
        # aufgabe_zwei_b(2) -> 1078 Schritte
        # aufgabe_zwei_b(50) -> 1131 Schritte
        # aufgabe_zwei_b(100) -> 1182 Schritte

def aufgabe_zwei_c(n, m):
    n = abs(n)
    m = abs(m)
    #Eine Funktion, die durch Ausgabe auf der Konsole ein Schachfeld (n x m) erzeugt,
    #indem schwarz als 1 und weiß als 0 codiert ist (Schachfeld soll oben links mit 0 (als weiß) starten).
    for s in range(0, n):
        rout = ""
        for r in range(0, m):
            if r % 2 == 0:
                if s % 2 == 0:
                    rout +=  "0 "
                else:
                    rout += "1 "
            else:
                if s % 2 != 0:
                    rout +=  "0 "
                else:
                    rout += "1 "
        print(rout)
    # Tests:
        # aufgabe_zwei_c(1, 1) -> 0
        # aufgabe_zwei_c(2,2) -> 01
                                #10
        # aufgabe_zwei_c(-3,3) ->010
                                #101
                                #010


def aufgabe_zwei_d(limit):
    #Annäherung Catalansche Konstante, da keine infinite lopps in Python gut möglich sind,
    #muss ein Limit eingesetzt werden
    ergebnis = 0
    for n in range(0, limit):
        ergebnis += (((-1) ** n) / ((2 * n + 1) ** 2))
    return ergebnis

    #Tests:
        # aufgabe_zwei_d(1) ->  1
        # aufgabe_zwei_d(10) -> 0.914724781654844
        # aufgabe_zwei_d(100) -> 0.9159530951145242

def aufgabe_zwei_e(beginn, ende, schrittweite):
    #Die Funktion gibt die Differenz, der jeweiligen Schritte der Annäherung an die Catlansche Konstante
    #in selbst festgelegten Schritten aus
    ergebnis = 0
    last_ergebnis = 0
    for n in range (0, ende+1):
        ergebnis += (((-1)**n)/((2*n+1)**2))
        if n >= beginn-1:
            differenz = last_ergebnis - ergebnis
            last_ergebnis = ergebnis
            if n >= beginn and (n-beginn) % schrittweite == 0 or n== beginn:
                print("n" + str(n) + ": " + str(ergebnis)+ "\nDifferenz: " + str(differenz))
    #Tests:
        # aufgabe_zwei_e(4,10,3) -> n4: 0.9208264046359285
                                    # Differenz: -0.012345679012345734
                                    # n7: 0.9140346571448803
                                    # Differenz: 0.004444444444444473
                                    # n10: 0.9169923553509892
                                    # Differenz: -0.0022675736961451642
        # aufgabe_zwei_e(0,10,3) ->n0: 1.0
                                    # Differenz: -1.0
                                    # n3: 0.9084807256235827
                                    # Differenz: 0.020408163265306145
                                    # n6: 0.9184791015893248
                                    # Differenz: -0.00591715976331364
                                    # n9: 0.914724781654844
                                    # Differenz: 0.0027700831024930483

        # aufgabe_zwei_e(5,0,1) -> #
if __name__ == '__main__':
    #print(aufgabe_zwei_a(-1, 5) )
    #print(aufgabe_zwei_b(2))
    #aufgabe_zwei_c(3,3)
    #print(aufgabe_zwei_d(10))
    #aufgabe_zwei_e(4,10,3)
    pass