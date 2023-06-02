#1 Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

# Within the function, we utilize the max() built-in function, which returns the maximum value among the provided arguments. By passing num1, num2, and num3 as arguments to max(), we can directly obtain the maximum of the three numbers.

#test
result = max_num(10, 5, 8)
print (result) #10

result = max_num(2, 7, 3)
print(result)  # 7

result = max_num(1, 1, 1)
print(result)  # 1