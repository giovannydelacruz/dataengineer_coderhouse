import numpy as np

def run():
    try:
        quantity = int(input("Cuantos números quieres introducir?: "))
        list = np.array(0)

        for i in range(quantity):
            number = int(input("Ingresa un número: "))
            list = np.append(list, number)
        mean = list.mean()

        print(f"La media aritmética de los números ingresado es: {mean}")            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()