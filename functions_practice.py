# a function named hello() that prints a greeting to the user. No arguments returns nothing
def hello():
    print("Hello! Welcome!")

# Testing the function
hello()

#A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

# Testing the function
result = pack("apple", "banana", "orange")
print(result)

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(food_list):
    if len(food_list) == 0:
        print("my lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

# Testing the function
eat_lunch(['sandwich', 'chips', 'apple'])