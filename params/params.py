import os,sys

def parse_params():
    if len(sys.argv) == 1:
        num_sides = int(input("Enter number of sides for a dice: "))
        num_dices = int(input("Enter number of dices: "))
    elif len(sys.argv) == 2:
        num_sides = int(sys.argv[1])
        num_dices = 1
    elif len(sys.argv) == 3: 
        print(f"Arguments: {sys.argv}")
        num_sides = int(sys.argv[1])
        num_dices = int(sys.argv[2])
    else:
        print("Wrong number of parameters!")
        exit(1)
    return [ num_sides, num_dices ]
