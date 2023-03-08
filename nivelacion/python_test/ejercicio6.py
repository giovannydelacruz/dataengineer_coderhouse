import numpy as np

def run(number, lista):
    try:
        quantity = 0
        for i in lista:
          if i == number:
            quantity+=1
        print(quantity)        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    number = int(input("Cual número deseas saber la cantidad de veces que aparece en la lista?: "))
    lista = [0,0,1,1,2,2,2,2,4,5,6,6,6,7,7,7,7,7,7,8]
    run(number,lista)