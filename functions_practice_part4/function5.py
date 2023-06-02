#5 Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
    # The function accepts the number n, the number of rows to print
    # Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    triangle = []  # Initialize an empty list to store the Pascal's triangle
    
    for i in range(n):  # Iterate over each row (i) from 0 to n-1
        row = []  # Create an empty list for the current row
        
        for j in range(i+1):  # Iterate over each element in the current row (j) from 0 to i
            if j == 0 or j == i:  # First and last elements of each row are always 1
                row.append(1)
            else:  # Calculate other elements by summing up the corresponding elements from the previous row
                prev_row = triangle[i-1]
                element = prev_row[j-1] + prev_row[j]
                row.append(element)
        
        triangle.append(row)  # Append the current row to the triangle list
    
    # Print each row of the triangle
    for row in triangle:
        print(' '.join(str(num) for num in row))


#test
pascal(5)

