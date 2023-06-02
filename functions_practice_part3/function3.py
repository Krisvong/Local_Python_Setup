#3 one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
def one_true(iterable):
    return any(iterable)

#test
result = one_true([False, False, True])
print(result)  # True

result = one_true([False, False, False])
print(result)  # False

result = one_true([])
print(result)  # False (Empty iterable has no elements, so no element is true)