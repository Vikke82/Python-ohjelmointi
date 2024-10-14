def kertoma(n):
    if n == 0:
        return 1
    else:
        return n * kertoma(n - 1)

def laske_pinta_ala(leveys, korkeus=1):
    return leveys * korkeus

def tulosta_parilliset(luku):
    for i in range(luku + 1):
        if i % 2 == 0:
            print(i)