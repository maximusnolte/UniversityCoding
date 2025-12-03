
from random import randint

def words_to_dezimal(words):
    """
        Convert words representing a number in base 10 
        from 0-9 to its decimal integer value.
    """

    decimals = ""
    words = words.lower()
    words = words.replace(" ", "")
    words = words.split(",")
    for word in words:
        match word:
            case "null":
                decimals += "0"
            case "eins":
                decimals += "1"
            case "zwei":
                decimals += "2"
            case "drei":
                decimals += "3"
            case "vier":
                decimals += "4"
            case "fünf":
                decimals += "5"
            case "sechs":
                decimals += "6"
            case "sieben":
                decimals += "7"
            case "acht":
                decimals += "8"
            case "neun":
                decimals += "9"

    return decimals

def aufgabe_1_a():
    """
        Aufgabe 1 a)
        Schreiben Sie ein Programm, das eine Zahl in Worten (0-9)
        einliest (z.B. "eins, drei, sieben") und die entsprechende
        Dezimalzahl (z.B. "137") ausgibt.
    """
    while True:
        input_words = input("Geben Sie eine/mehrere Zahl/en in Worten (0-9) ein, getrennt durch Kommas: ")
        print(words_to_dezimal(input_words))

def insert_number_into_list(number, lst):
    """
        Insert a number into a sorted list while maintaining the order.
    """
    for i in range(len(lst)):
        if number < lst[i]:
            lst.insert(i, number)
            return lst, i
    lst.append(number)
    return lst, len(lst)

def aufgabe_1_b():
    """
        Aufgabe 1 b)
        Schreiben Sie ein Programm, das eine sortierte Liste von Zahlen
        und eine weitere Zahl einliest und die Zahl an der richtigen
        Position in die Liste einfügt.
    """
    input_list = input("Geben Sie eine sortierte Liste von Zahlen ein, getrennt durch Kommas: ")
    input_number = int(input("Geben Sie eine Zahl ein, die in die Liste eingefügt werden soll: "))

    lst = [int(x) for x in input_list.replace(" ", "").split(",")]
    new_list, position = insert_number_into_list(input_number, lst)

    print(f"Die neue Liste lautet: {new_list}")
    print(f"Die Zahl wurde an der Position {position} eingefügt.")

def fake_dictionary(tuple_list, key):
    """
    Simuliert ein Python-Dictionary mithilfe einer Liste von Tupeln.
    Gibt den Wert zurück, der dem angegebenen Schlüssel zugeordnet ist,
    oder None, wenn der Schlüssel nicht gefunden wird.
    """
    for tup in tuple_list:
        if tup[0] == key:
            return tup[1]
    return None

def aufgabe_1_c():
    """
        Aufgabe 1 c)
        Schreiben Sie ein Programm, das eine Liste von Tupeln
        (Schlüssel, Wert) einliest und einen Schlüssel abfragt.
        Das Programm soll den entsprechenden Wert zurückgeben
        oder None, wenn der Schlüssel nicht gefunden wird.
    """
    input_tuples = input("Geben Sie eine Liste von Tupeln (Schlüssel,Wert) ein")
    input_key = int(input("Geben Sie einen Schlüssel ein, dessen Wert abgefragt werden soll: "))

    tuples = []
    input_tuples = input_tuples.split("),")
    for tupl in input_tuples:
        tupl = tupl.replace("(", "").replace(")", "").replace(" ", "")
        key, value = tupl.split(",")
        tuples.append((int(key), int(value)))
    print(fake_dictionary(tuples, input_key))

def ackermann_funktion(n,m):
    """
        Implementierung der Ackermann-Funktion.
        Aus Aufgabe 2 a)
    """
    if n == 0:
        return m + 1
    if m == 0 and n != 0 :
        return ackermann_funktion(n - 1, 1)

    return ackermann_funktion(n - 1, ackermann_funktion(n, m - 1))

def create_matrix(n,m):
    """
        Erstellung einer n x m Matrix mit zufälligen Zahlen
    """
    if n < 2 or m < 2:
        return "Fehler: n und m müssen größer oder gleich 2 sein."
    matrix = {}
    for row in range(n):
        for col in range(m):
            random_number = randint(-200, 4000)
            matrix.update({(row, col): random_number})
    return matrix

def format_matrix(mtrx, n, m):
    """
        Formatiert eine n x m Matrix für die Ausgabe
    """
    for row in range(n):
        row_string = "("
        for col in range(m):
            row_string += f"{mtrx[(row, col)]:>5}"
        row_string += ")"
        row_string = row_string.replace(" )", ")")
        print(row_string)

def output_matrix():
    """
        Ausgabe einer n x m Matrix mit zufälligen Zahlen
    """
    print("Gib Zahlen für n>2 und m > 2 ein, um eine n x m Matrix zu erstellen.")
    n = int(input("Number of Rows:"))
    m = int(input("Number of Columns:"))

    matrix = create_matrix(n,m)
    print()
    for row in range(n):
        row_string = "("
        for col in range(m):
            row_string += f"{matrix[(row, col)]} "
        row_string += ")"
        row_string = row_string.replace(" )", ")")
        print(row_string)
    print()
    format_matrix(matrix,n,m)


if __name__ == '__main__':
    #aufgabe_1_a()
    #aufgabe_1_b()
    #aufgabe_1_c()
    output_matrix()

