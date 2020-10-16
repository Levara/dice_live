import random

def main(): 
    num_sides = int(input("Enter number of sides for a dice:"))
    roll = random.randint(1,num_sides)
    print("Dice roll is %d"%(roll))

if __name__ == "__main__":
    main()

