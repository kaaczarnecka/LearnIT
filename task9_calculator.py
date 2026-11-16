a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
znak = input("Podaj znak działania (+, -, *, /): ")

if znak == "+":
    wynik = a + b
elif znak == "-":
    wynik = a - b
elif znak == "*":
    wynik = a * b
elif znak == "/":
    if b == 0:
        print("Błąd: dzielenie przez zero!")
        exit()
    wynik = a / b
else:
    print("Błąd: niepoprawny znak działania!")
    exit()

print(f"Wynik: {a} {znak} {b} = {wynik}")