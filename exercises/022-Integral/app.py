# Your code here
def squares_dictionary(num):
    resul = {}
    for i in range(1,num+1):
        resul[i] = i*i
    return resul

print(squares_dictionary(8))
