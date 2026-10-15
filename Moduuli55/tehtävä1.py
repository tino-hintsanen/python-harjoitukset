#tehtävä 1 
import random

noppa = input("kerro noppien määrä")
luku = int(noppa)
summa = 0

for n in range(luku):
    nopanheitto = random.randint(1,6)
    summa += nopanheitto

print("noppien silmälukujen summa on", summa)




