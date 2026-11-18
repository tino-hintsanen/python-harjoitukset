# tehtävä 1

talvi = (12, 1, 2)   
kevät = (3, 4, 5)    
kesä = (6, 7, 8)     
syksy = (9, 10, 11)  


kknumero = int(input("Anna kuukauden numero (1 - 12): "))


if kknumero in talvi:
    print(f"Kuukausi {kknumero} on talvikuukausi.")
elif kknumero in kevät:
    print(f"Kuukausi {kknumero} on kevätkuukausi.")
elif kknumero in kesä:
    print(f"Kuukausi {kknumero} on kesäkuukausi.")
elif kknumero in syksy:
    print(f"Kuukausi {kknumero} on syyskuukausi.")
else:
    print("Virheellinen numero! Anna luku väliltä 1-12.")