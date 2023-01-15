import random
MIN_VAL = 1
MAX_VAL = 9
EXPEC_VAL = 4

def mult_four():
    A = random.randint(MIN_VAL, MAX_VAL)
    B = random.randint(MIN_VAL, MAX_VAL)
    C = A*B
    if(C==EXPEC_VAL):
        print("\nSuccess!\nWith A=" + str(A) + " * B=" + str(B) + "\n C=" + str(C))
    else:
        print("A=" + str(A) + ", C=" + str(C))
        mult_four()



mult_four()