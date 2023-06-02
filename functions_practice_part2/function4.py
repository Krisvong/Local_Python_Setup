#4 sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(num1, num2):
    sum_result = num1 + num2
    product_result = num1 * num2
    return sum_result, product_result

#test
result = sum_n_product(5,3)
print("Sum:", result[0])
print("Product:", result[1])