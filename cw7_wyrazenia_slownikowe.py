imiona = ["Ania", "Kasia", "Marek", "Kleopatra"]

imiona2 = {
    imie: len(imie)
    for imie in imiona}

print(imiona2)

celciusz = {'t1': -2, 't2': 0, 't3': 5, 't4': 4}

faherheit = {key: celciusz * 9/5 + 32 for key, celciusz in celciusz.items() if celciusz > 0}

print(faherheit)