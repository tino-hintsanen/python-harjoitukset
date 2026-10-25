# tehtävä 6

arvot = []

while True:
    lista = int(input("anna joku arvo" ))
    
    if lista == 0:
        break
    
    arvot.append(lista)

print("Listausjärjestyksessä:", arvot)

lista2 = sorted(arvot)
print("Pienimmästä suurimpaan:", lista2)