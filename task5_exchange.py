kurs = 4
kwota_pln = float(input("Podaj kwotę w PLN: "))
kwota_usd = kwota_pln / kurs
print(f"{kwota_pln} PLN to {kwota_usd:.2f} USD.")