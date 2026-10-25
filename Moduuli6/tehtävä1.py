#tehtävä 1

import math
tuntipalkka = float(input("anna tuntipalkkasi"))
tunnit = float(input("anna tehdyt tunnit"))
vkopv = (input("anna viikonpäivä? (maanantai, tiistai, keskiviikko, torstai, perjantai, lauantai, sunnuntai"))

if vkopv != "sunnuntai":
    liksa = tuntipalkka * tunnit
    print("päiväsi palkka on ", liksa )

elif vkopv == "sunnuntai":
    tuplaliksa = tuntipalkka * tunnit * 2
    print("päiväsi palkka on ", tuplaliksa)

else:
    vkopv != "maanantai","tiistai", "keskiviikko", "torstai", "perjantai","lauantai","sunnuntai"
    print("virheellinen viikonpäivä")


