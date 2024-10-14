def distributive_property(a, b, c):
    return a * (b + c), a * b + a * c

a, b, c = 2, 3, 4
result_dist = distributive_property(a, b, c)
print(f"Distributive property: {a} * ({b} + {c}) = {result_dist[0]}, {a} * {b} + {a} * {c} = {result_dist[1]}")
