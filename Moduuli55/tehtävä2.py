# tehtävä 2

luvut = []

while True:
    annettuluku = input("anna luku (tyhjä lopettaa ohjelman: )")

    if annettuluku == "":
        break

    luku = float(annettuluku)
    luvut.append(luku)


luvut.sort(reverse = True)

viisisuurinta = luvut[:5]


print("\nviisi suurinta lukua isoimmasta lähtien")
for luku in viisisuurinta:
    print(luku)



