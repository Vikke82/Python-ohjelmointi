import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='ohjelma.log', level=logging.DEBUG)

def laske_summa(numerot):
    summa = 0
    for numero in numerot:
        logging.debug(f"Lisätään {numero} summaan {summa}")
        
        summa += numero
    return summa

numerot = [1, 2, 3, 4]
tulos = laske_summa(numerot)
logging.info(f"Listan summa on: {tulos}")
