# tehtävä 1

import random


def noppa():
  return random.randint(1, 6)


print("nopan heitto alkaa")
heitot = 0

while True:
  silmaluku = noppa()
  heitot += 1
  print(f"Heitto {heitot}: {silmaluku}")

  if silmaluku == 6:
    break