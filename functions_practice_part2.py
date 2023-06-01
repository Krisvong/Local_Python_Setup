#1 arb_args - Takes in any number of arguments and prints them one at a time
# * before the args parameter indicates that it will accept any number of arguments. Arguments are stored in the 'args' tuple.
def arb_args(*args):
    for arg in args:
        print(arg)

#test
arb_args(1,2,3)

#2 inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(num1, num2):
    def nested_func1(a,b):
        return a + b # Example math operation 1
    
    def nested_func2(x,y):
        return x * y # Example math operation 2
    
    result1 = nested_func1(num1, num2)
    result2 = nested_func2(num1, num2)
    total = result1+ result2
    print(total)

#test
inner_func(3,4)

#3 lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(student_name, lunch_preference=None):
    if lunch_preference is None:
        lunch_preference = "Mystery Meat"

    print("Student Nme:", student_name)
    print("Lunch Preference:", lunch_preference)

#test
lunch_lady("John", "Pizza")

#4 sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(num1, num2):
    sum_result = num1 + num2
    product_result = num1 * num2
    return sum_result, product_result

#test
result = sum_n_product(5,3)
print("Sum:", result[0])
print("Product:", result[1])

#5 alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
def arb_args(*args):
    for arg in args:
        print(arg)
    
# Assigning the alias
alias_arb_args = arb_args

#test
alias_arb_args(1,2,3)
arb_args("apple", "banana", "orange", "grape")

#6 arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    if len(args) == 0:
        print("No numbers provided.")
    else:
        average = sum(args) / len(args)
        print("Average:", average)  

#test
arb_mean(2,4,6,8,10)  

#7 arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    if len(args) == 0:
        return None # Return None if no strings provided
    
    longest_string = args[0]
    for string in args[1:]:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

#test
result = arb_longest_string("apple", "banana", "orange")
print("Longest string:", result)