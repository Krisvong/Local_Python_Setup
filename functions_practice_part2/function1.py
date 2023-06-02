#1 arb_args - Takes in any number of arguments and prints them one at a time
# * before the args parameter indicates that it will accept any number of arguments. Arguments are stored in the 'args' tuple.
def arb_args(*args):
    for arg in args:
        print(arg)

#test
arb_args(1,2,3)