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