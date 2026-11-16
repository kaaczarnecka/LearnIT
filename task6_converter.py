dec = int(input("Podaj liczbę dziesiętną: "))
bin = bin(dec)
hex = hex(dec)
print(f"Liczba dziesiętna {dec} w systemie binarnym to {bin[2:]}, a w systemie szesnastkowym to {hex[2:]}.")