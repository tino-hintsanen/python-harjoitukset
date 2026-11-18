# tehtävä 2

nimet = []

print("Syötä nimiä. Tyhjä merkkijono lopettaa.")

while True:
    nimi = input("Anna nimi: ").strip()
    
   
    if nimi == "":
        break
        
    
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        
        nimet.append(nimi)

print("\nSyötetyt nimet:")

for nimi in nimet:
    print(nimi)