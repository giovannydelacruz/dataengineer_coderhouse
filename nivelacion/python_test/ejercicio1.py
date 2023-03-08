def run():
    try:
        number = int(input("Introduce un número impar a continuación: "))

        while number%2!=1:
            number = int(input("Introduce un número impar a continuación: "))
        print("Es correcto, has ingresado un númeor impar!!")
    except:
        print("No se ha ingresado un número!")

if __name__ == "__main__":
    run()