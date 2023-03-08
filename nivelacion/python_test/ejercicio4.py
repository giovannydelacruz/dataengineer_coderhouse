import numpy as np

def run():
    try:
        list_one = [x for x in range(0,21)]
        list_two = [x for x in range(-10,15) if x%3==0]
        print(f"La primera lista es: {list_one}\n y la segunda lista es: {list_two}\n")
        list_ambas = set(list_one) & set(list_two)
        print(list_ambas)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()