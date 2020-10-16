import random
import os,sys

def main(): 
    if len(sys.argv) == 1:
        num_sides = int(input("Enter number of sides for a dice: "))
        num_dices = int(input("Enter number of dices: "))
    else: 
        print(f"Arguments: {sys.argv}")
        num_sides = int(sys.argv[1])
        num_dices = int(sys.argv[2])
    for i in range(num_dices):
        roll = random.randint(1,num_sides)
        print("Dice [%d] roll is %d"%(i+1, roll))

if __name__ == "__main__":
    main()

