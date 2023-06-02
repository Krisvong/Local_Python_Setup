# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD
def recursive_deduplicate(string):
    if len(string) < 2:
        return string # Base case: if the string has 1 or fewer characters, it is already deduplicated
    
    if string[0] == string[1]:
        #If the first two characters are duplicates, recursively call the function with the remaining substring
        return recursive_deduplicate(string[1:])
    else:
        #If the first two characters are not duplicates, concatenate the first character with the deduplicated substring
        return string[0] + recursive_deduplicate(string[1:])
    
#test
result = recursive_deduplicate("AABBCCDD")
print(result)  # "ABCD"

result = recursive_deduplicate("ABBA")
print(result)  # "ABA"

result = recursive_deduplicate("AAABBBCCC")
print(result)  # "ABC"
