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

