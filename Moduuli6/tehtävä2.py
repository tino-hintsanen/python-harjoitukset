#tehtävä 2

luku = int(input("anna kokonaisluku"))

if  luku % 3 == 0 and luku % 5 == 0:
    print("jaollinen molemmilla luvuilla")
elif luku % 3 == 0:
    print("kolmella jaollinen")
elif luku % 5 == 0:
    print("viidellä jaollinen")
else:
    print("ei jaollinen luvuilla")