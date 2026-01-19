# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    dol = d * n
    cent = c * n
    if cent >= 100:
        dol += cent // 100
        cent = cent % 100
    return dol, cent


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(10,15,2))
