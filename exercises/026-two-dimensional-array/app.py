# Your code here
def two_dimensional_list(f, c):
    filas = []
    for x in range(f):
        columnas = []
        for y in range(c):
            columnas.append(x*y)
        filas.append(columnas)
    return filas

print(two_dimensional_list(3,5))

            

