#tehtävä 3

pienin = None
isoin = None

while True:
    luku = input("anna luku")

    if luku == "":
        break


    luku = int(luku)

    if pienin is None or luku < pienin:
        pienin = luku

    if isoin is None or luku > isoin:
        isoin = luku

print("pienin luku", pienin)
print("isoin luku", isoin)


