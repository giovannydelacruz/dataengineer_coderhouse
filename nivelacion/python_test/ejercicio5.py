import numpy as np

def run():
    try:
        
        list_one = np.array([x for x in range(0,100) if x%2!=0])
        suma = list_one.sum()
        print(suma)
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()