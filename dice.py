import random
import os,sys

def main(): 
    if len(sys.argv) == 1:
        num_sides = int(input("Enter number of sides for a dice:"))
    else: 
        print(f"Arguments: {sys.argv}")
        num_sides = int(sys.argv[1])
    roll = random.randint(1,num_sides)
    print("Dice roll is %d"%(roll))

if __name__ == "__main__":
    main()

