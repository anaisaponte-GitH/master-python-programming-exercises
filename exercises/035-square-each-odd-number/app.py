# Your code here
def square_odd_numbers(numeros):
    list_str = numeros.split(",")
    list_nros = list(map(int,list_str))
    list_resul = []
    for i in list_nros:
        if (i % 2 != 0):
            list_resul.append(i ** 2)
    return(list_resul)

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))


