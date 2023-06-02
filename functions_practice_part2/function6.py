#6 arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    if len(args) == 0:
        print("No numbers provided.")
    else:
        average = sum(args) / len(args)
        print("Average:", average)  

#test
arb_mean(2,4,6,8,10)  