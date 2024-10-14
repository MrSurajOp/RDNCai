def associative_addition(a, b, c):
    return (a + b) + c, a + (b + c)

def associative_multiplication(a, b, c):
    return (a * b) * c, a * (b * c)

a, b, c = 2, 3, 4
result_add = associative_addition(a, b, c)
print(f"Associative property for addition: ({a} + {b}) + {c} = {result_add[0]}, {a} + ({b} + {c}) = {result_add[1]}")

result_mul = associative_multiplication(a, b, c)
print(f"Associative property for multiplication: ({a} * {b}) * {c} = {result_mul[0]}, {a} * ({b} * {c}) = {result_mul[1]}")
