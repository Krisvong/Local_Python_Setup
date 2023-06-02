#2 all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def all_true(iterable):
    return all(iterable)

#test
result = all_true([True, True, True])
print(result)  # True

result = all_true([True, False, True])
print(result)  # False

result = all_true([])
print(result)  # True (Empty iterable is considered as all elements being true)