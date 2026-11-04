# tehtävä 2

import random

def noppa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))

print("nopan heitto alkaa")
heitot = 0

while True:
    silmaluku = noppa(tahkot)
    heitot += 1
    print(f"Heitto {heitot}: {silmaluku}")
    
 
    if silmaluku == tahkot:
        break