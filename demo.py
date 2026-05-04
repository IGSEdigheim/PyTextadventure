# held_name = input("Wie heißt du? ")
# print("Willkommen,", held_name, "! Dein Abenteuer beginnt." )
# waffe = "Pistole"
# leben = 100

# print("Du bist ein mutiger Held.")
# print("Vor dir liegt ein dunkler Wald.")
# print("Was tust du?")

# print(held_name, "kämpft mit", waffe, ". Leben: ", leben)

# wahl = "0"
# while wahl not in ["1","2"]:
#     wahl = input("Gehst du in den Wald? (1=Ja / 2=Nein) ")

#     if wahl == "1" or wahl == "Ja":
#         print("Du betrittst mutig den dunklen Wald.")
#     elif wahl == "2" or wahl == "Nein":
#         print("Du kehrst um. Das Abenteuer ist vorbei.")
#     else:
#         print("Ungültige Eingabe!")


# Demo
import random

print("=== Würfelkampf ===")
held_wurf = random.randint(1, 6)
drache_wurf = random.randint(1, 6)

print("Du würfelst:", held_wurf)
print("Der Drache würfelt:", drache_wurf)

if held_wurf > drache_wurf:
    print("Du gewinnst den Kampf!")
elif held_wurf < drache_wurf:
    print("Der Drache besiegt dich!")
else:
    print("Unentschieden! Beide stehen noch.")