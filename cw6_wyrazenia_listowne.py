liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

liczby_parzyste = []
for liczba in liczby:
    if liczba % 2 == 0:
        liczby_parzyste.append(liczba)

print(liczby_parzyste)

liczby_parzyste_wyrazenie = [liczba
                             for liczba in liczby
                             if liczba % 2 == 0]

potegi_dwojki = [element ** 2
                for element in range(100)]

print(potegi_dwojki)



