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