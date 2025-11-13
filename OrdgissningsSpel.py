import random

ordlista = ["Mask", "Kanin", "Julafton", "pepparkakor", "Stenfisk"]
hemligt_ord = random.choice(ordlista)

gissning = ["_"] * len(hemligt_ord)
gissade_bokstäver = set()

print("Välkommen till Ordgissningsspelet!\nDu ska få gissa ordet, det har", len(hemligt_ord), "bokstäver.")

antal = 10
while "_" in gissning:
    print("\nNuvarande ord:", " ".join(gissning))
    bokstav = input("Gissa en bokstav: ").lower()
    antal -= 1
    print(f"du har {antal} gissningar kvar")
#Kommer inte riktigt ihåg hur man commita så jag tar det nästa gång, här är koden från idag.





import random

ordlista = ["Mask", "Kanin", "Julafton", "Pepparkakor", "Stenfisk"]
hemligt_ord = random.choice(ordlista).lower()

gissning = ["_"] * len(hemligt_ord)
gissade_bokstäver = set()

print("Välkommen till Ordgissningsspelet!")
print(f"Du ska gissa ett ord som har {len(hemligt_ord)} bokstäver.\n")

antal = 10
while "_" in gissning and antal>=0:
    print("Nuvarande ord:", " ".join(gissning))
    print(f"Du har {antal} gissningar kvar.")
    bokstav = input("Gissa en bokstav: ").lower()
    if bokstav in gissade_bokstäver:
        print("Du har redan använt denna bokstav, försök igen")
        antal+=1
    gissade_bokstäver.add(bokstav)
    antal-=1
    for i in range(len(hemligt_ord)):
        if hemligt_ord[i] == bokstav:
            gissning[i] = bokstav

if "_" not in gissning:
    print(f"Grattis du gissade rätt ord\nDet korrekta ordet var {hemligt_ord}")
if antal<=1:
    print(f"Du har tyvär använt upp alla dina gissningar och därmed avslutat spelet, det korrekta ordet var {hemligt_ord}")


#Tredje tillfälle

import random
j = 1
while j == 1:
    ordlista = ["Mask", "Kanin", "Julafton", "Pepparkakor", "Stenfisk"]
    hemligt_ord = random.choice(ordlista).lower()

    gissning = ["_"] * len(hemligt_ord)
    gissade_bokstäver = set()
    felgissningar=[]
    print("Välkommen till Ordgissningsspelet!")
    print(f"Du ska gissa ett ord som har {len(hemligt_ord)} bokstäver.\n")

    antal = 10
    while "_" in gissning and antal>=0:
        print("Nuvarande ord:", " ".join(gissning))
        print(f"Du har {antal} gissningar kvar.")
        antal-=1
        bokstav = input("Gissa en bokstav: ").lower()
        if len(bokstav)>1:
             print("Du ska bara använda en bokstav")
             antal+=1
        if bokstav in gissade_bokstäver:
            print("Du har redan använt denna bokstav, försök igen")
            antal+=1
        if bokstav in hemligt_ord:
            print("Denna bokstav fanns i ordet")
        else:
            print("Denna bokstav fanns inte i ordet")
            if bokstav in felgissningar:
                continue
            else:
                felgissningar.append(bokstav)
                fel_ihop2=" ".join(felgissningar)
            print(f"Dina felgissningar är {fel_ihop2}")
        gissade_bokstäver.add(bokstav)

        for i in range(len(hemligt_ord)):
            if hemligt_ord[i] == bokstav:
                gissning[i] = bokstav
        continue


    if "_" not in gissning:
        print(f"Grattis du gissade rätt ord\nDet korrekta ordet var {hemligt_ord}")
    if antal<=1:
        print(f"Du har tyvär använt upp alla dina gissningar och därmed avslutat spelet, det korrekta ordet var {hemligt_ord}")

    Restart=input("Vill du starta om spelet, J/N").lower()
    if j:
        continue
    else:
        j += 1
print("Tack föratt du körde! :D")
