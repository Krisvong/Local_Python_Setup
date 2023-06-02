#2 Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num #multiply current 'num' with the current value of 'result' and update 'result' accordingly
    return result

#test
result = mult_list([1, 2, 3, 4, 5])
print(result)  # 120 (1 * 2 * 3 * 4 * 5 = 120)

result = mult_list([2, 3, 4, 5])
print(result)  # 120 (2 * 3 * 4 * 5 = 120)

result = mult_list([1, 1, 1, 1, 1])
print(result)  # 1 (1 * 1 * 1 * 1 * 1 = 1)
