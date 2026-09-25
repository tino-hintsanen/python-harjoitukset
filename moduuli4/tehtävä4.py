#tehtävä 4

import random

luku = random.randint(1, 10)

while True:
    arvaus =(int(input("arvaa luku 1-10")))

    if arvaus == luku:
        print("oikea vastaus")
        break

    elif arvaus < luku:
        print("lukusi on liian pieni")

    else:
        print("lukusi on liian iso")





