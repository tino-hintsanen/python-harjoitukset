# tehtävä 4

def laskesumma(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa


testilista = [14, 5, 9, 25, 3]

tulos = laskesumma(testilista)


print(f"Listan {testilista} lukujen summa on: {tulos}")