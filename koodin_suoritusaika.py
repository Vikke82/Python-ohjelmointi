import time

# Esimerkki 1: Koodin suoritusajan mittaaminen yksinkertaisella tavalla
def nopea_funktio():
    summa = 0
    for i in range(100000):
        summa += i
    return summa

def hidas_funktio():
    summa = 0
    for i in range(100000):
        summa += i ** 2
    return summa

# Mittaa nopea_funktion suoritusajan
start_time = time.time()
nopea_funktio()
end_time = time.time()
print(f"nopea_funktio suoritettiin ajassa: {end_time - start_time:.5f} sekuntia")

# Mittaa hidas_funktion suoritusajan
start_time = time.time()
hidas_funktio()
end_time = time.time()
print(f"hidas_funktio suoritettiin ajassa: {end_time - start_time:.5f} sekuntia")
