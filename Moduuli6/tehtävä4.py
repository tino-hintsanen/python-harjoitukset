#tehtävä 4



while True:
    luku = int(input("kerro joku kokonaisluku? "))

    if luku < 0:
        print("virheellinen numero")

    elif luku > 0:
        from math import sqrt
        print(sqrt(luku))

    elif luku == 0:
        break

