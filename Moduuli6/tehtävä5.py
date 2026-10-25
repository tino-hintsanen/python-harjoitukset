# tehtävä 5

tarina = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan?: (loppu sana lopettaa tarinan) ")

    if sana == "loppu":
        break

    tarina += sana + " "

print(tarina)

