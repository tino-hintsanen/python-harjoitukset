#tehtävä 5


tunnus = "tino"
salasana = "python"

yritys = 0
enimmäismäärä = 5

while yritys < enimmäismäärä:
    käyttäjä = input("kirjoita käyttäjätunnus, ")
    salis = input("kirjoita salasana ")

    if tunnus == käyttäjä and salasana == salis:
        print("tervetuloa! ")
        break

    else:
        yritys += 1

if enimmäismäärä == yritys:
    print("pääsy evätty")


    
