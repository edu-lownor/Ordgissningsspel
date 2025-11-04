import random

ordlista = ["Mask", "Kanin", "Julafton", "pepparkakor", "Stenfisk"]

hemligt_ord = random.choice(ordlista)

print("Välkommen till Ordgissningsspelet!\nDu ska få gissa ordet, det har", len(hemligt_ord), "bokstäver.")