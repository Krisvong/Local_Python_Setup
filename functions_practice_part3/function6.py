# recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(string):
    if len(string) <= 1:
        return string # Base case: if the string has 1 or fewer characters, it is already reversed
    
    return recursive_reverse(string[1:]) + string[0]

#test
result = recursive_reverse("Hello")
print(result)  # "olleH"

result = recursive_reverse("Python")
print(result)  # "nohtyP"

result = recursive_reverse("12345")
print(result)  # "54321"
