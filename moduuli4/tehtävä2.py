
while True:
    tuuma = float(input("kirjoita tuumat (negatiivinen lopettaa ohjelman): "))

    if tuuma < 0:
        print("ohjelma päättyy")
        break


    senttimetri = tuuma * 2.54
    print(f"{tuuma} tuumaa on {senttimetri} cm")

