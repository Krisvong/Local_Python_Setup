#1 name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    # Iterate over the key-value pairs in the kwargs dictionary
    for key, value in kwargs.items():
        # Print the key and value with the pattern "key: value"
        print(key, ":", value)



# The name_args function is defined, which uses the **kwargs syntax to accept any number of named arguments. The named arguments are treated as a dictionary.

# Within the function, we use a for loop to iterate over the key-value pairs in the kwargs dictionary.

# In each iteration, we assign the key to the variable key and the value to the variable value.

# We use the print() function to output the key and value with the desired pattern "key: value". The comma , is used to separate the values in the print statement.


#test
name_args(name="John", age=25, city="New York")