# summa_lasku.py

def laske_summa(numerot):
    summa = 0
    for numero in numerot:
        summa += numero
    return summa

# Tämä on virheellinen syöte, joka aiheuttaa ongelman
numerot = [1, 2, 'kolme', 4]  # Huomaa, että tässä on tekstinä 'kolme' eikä numerona

# Asetetaan murtopiste
#import pdb; pdb.set_trace()
#breakpoint()

tulos = laske_summa(numerot)
print(f"Listan summa on: {tulos}")
