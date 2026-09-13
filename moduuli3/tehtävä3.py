#tehtävä 3

sukupuoli = input("mikä on biologinen sukupuolesi? (nainen, mies) ")
arvo = int(input("mikä on hemoglobiiniarvosi "))
       

if sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif arvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")