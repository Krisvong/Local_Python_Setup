#5 alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
def arb_args(*args):
    for arg in args:
        print(arg)
    
# Assigning the alias
alias_arb_args = arb_args

#test
alias_arb_args(1,2,3)
arb_args("apple", "banana", "orange", "grape")