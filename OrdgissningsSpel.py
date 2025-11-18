import random
ordlista = ["Mask", "Kanin", "Julafton", "Pepparkakor", "Stenfisk"]
alfabetet = "abcdefghijklmnopqrstuvwxyzåäö"
fel_ihop = ""

while True:
    hemligt_ord = random.choice(ordlista).lower()

    gissning = ["_"] * len(hemligt_ord)
    gissade_bokstäver = set()
    felgissningar = []
    print("Välkommen till Ordgissningsspelet!")
    print(f"Du ska gissa ett ord som har {len(hemligt_ord)} bokstäver.\n")

    antal = 10
    while "_" in gissning and antal >= 1:
        print("Nuvarande ord:", " ".join(gissning))
        print(f"Du har {antal} gissningar kvar.")
        antal -= 1
        bokstav = input("Gissa en bokstav: ").lower()
        if len(bokstav)>1:
            print("Du ska bara använda en bokstav")
            antal += 1
        elif bokstav not in alfabetet:
            print("Du får bara skriva bokstäver")
            antal += 1
        elif bokstav in gissade_bokstäver:
            print("Du har redan använt denna bokstav, försök igen")
            antal += 1
        elif bokstav in hemligt_ord:
            print("Denna bokstav fanns i ordet")
            antal += 1
        else:
            print("Denna bokstav fanns inte i ordet")
            if bokstav in felgissningar:
                continue
            else:
                felgissningar.append(bokstav)
                fel_ihop=" ".join(felgissningar)

        print(f"\nDina felgissningar är: {fel_ihop}")
        gissade_bokstäver.add(bokstav)

        for i in range(len(hemligt_ord)):
            if hemligt_ord[i] == bokstav:
                gissning[i] = bokstav


    if "_" not in gissning:
        print(f"\nGrattis du gissade rätt ord\nDet korrekta ordet var {hemligt_ord}")
    else:
        print(f"\nDu har tyvär använt upp alla dina gissningar och därmed avslutat spelet, det korrekta ordet var {hemligt_ord}")

    while True:
        restart = input("Vill du starta om spelet, J/N: ").lower()
        if restart != "j" and restart != "n":
            print("Svara med J (Ja) eller N (Nej)")
        else:
            print()
            break
    if restart == "n":
        break

print("Tack för att du körde! :D")