#3 Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1] #slicing allows us to create a new string that starts from the end and goes towards the beginning of the original string.

#test
result = rev_string("Hello")
print(result)  # "olleH"

result = rev_string("Python")
print(result)  # "nohtyP"

result = rev_string("12345")
print(result)  # "54321"
