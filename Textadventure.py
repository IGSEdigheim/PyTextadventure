def start():
    print("Willkommen zu deinem Abenteuer!")
    print("Du stehst vor einem dunklen Wald. Möchtest du hineingehen?")
    print("1: Ja")
    print("2: Nein")
    choice = input("Was tust du? ")
    if choice == "1":
        forest()
    elif choice == "2":
        print("Du entscheidest dich umzukehren. Ende des Spiels.")
    else:
        print("Ungültige Eingabe. Versuche es erneut.")
        start()

def forest():
    print("Du betrittst den Wald. Es ist unheimlich still.")
    print("Vor dir liegt ein alter Brunnen.")
    print("1: Schau in den Brunnen")
    print("2: Gehe weiter")
    choice = input("Was tust du? ")
    if choice == "1":
        well()
    elif choice == "2":
        print("Du gehst tiefer in den Wald, aber verlierst die Orientierung. Ende des Spiels.")
    else:
        print("Ungültige Eingabe. Versuche es erneut.")
        forest()

def well():
    print("Du schaust in den Brunnen und siehst eine schimmernde Münze.")
    print("1: Nimm die Münze")
    print("2: Lasse die Münze liegen")
    choice = input("Was tust du? ")
    if choice == "1":
        inventar.append("Münze")
        print("Die Münze ist verflucht! Du wirst in einen Frosch verwandelt. Ende des Spiels.")
    elif choice == "2":
        print("Du lässt die Münze liegen und gehst sicher aus dem Wald. Du hast überlebt!")
    else:
        print("Ungültige Eingabe. Versuche es erneut.")
        well()

inventar = []
# Spiel starten
start()
