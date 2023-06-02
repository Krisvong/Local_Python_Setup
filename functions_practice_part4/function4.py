#4 Write a Python function called num_within() to check whether a number falls in a given range.
    # The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
    # Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(number, start, end):
    return start <= number <= end

#test
result = num_within(3, 2, 4)
print(result)  # True

result = num_within(3, 1, 3)
print(result)  # True

result = num_within(10, 2, 5)
print(result)  # False
