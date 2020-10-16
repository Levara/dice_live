import random
from params import *

def main(): 
    num_sides, num_dices = parse_params()

    for i in range(num_dices):
        roll = random.randint(1,num_sides)
        print("Dice [%d] roll is %d"%(i+1, roll))

if __name__ == "__main__":
    main()

