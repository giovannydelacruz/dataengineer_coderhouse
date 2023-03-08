import numpy as np

def run():
    try:
        list_one = [x for x in range(0,11)]
        list_two = [x for x in range(-10,1)]
        list_three = [x for x in range(0,21) if x%2==0]
        list_four = [x for x in range(-20,1) if x%2!=0]
        list_five = [x for x in range(0,51) if x%5==0]
        print(list_one)       
        print(list_two)
        print(list_three)
        print(list_four)
        print(list_five)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()