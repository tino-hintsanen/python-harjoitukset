#tehtävä 1

pituus = float(input("anna kuhan pituus senttimetreinä"))

if pituus < 37:
    puuttuu = 37 - pituus
    print("kuha on alamittainen ja voit laskea sen takaisin järveen")
    print(f"pyyntipituudesta {puuttuu} cm ")

