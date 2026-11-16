wzrost = float(input("Podaj swój wzrost w metrach: "))
czy_opiekun = input("Czy jesteś opiekunem? (tak/nie): ").strip().lower()
if wzrost >= 1.6 or (wzrost >= 1.2 and czy_opiekun == "tak"):
    decyzja = True
else:
    decyzja = False
print(decyzja)