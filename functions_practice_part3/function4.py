#4 recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    if n == 0:
        return 1 # Base case: factorial of 0 is 1
    else:
        return n * recursive_factorial(n - 1)
    
#test
result = recursive_factorial(5)
print(result)  # 120 (factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120)

result = recursive_factorial(0)
print(result)  # 1 (factorial of 0 is defined as 1)
