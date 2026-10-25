#tehtävä 3

while True:
    tuotanto = (input("jatketaanko tuotantoa? kyllä, ei (ei vastauksella tuotanto päättyy)"))
    if tuotanto == "kyllä":
       print("tuotanto jatkuu")
    
    if tuotanto == "ei":
        print("tuotanto lopetettu")
        break

