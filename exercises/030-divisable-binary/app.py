# Your code here
def divisible_binary(binario):
    lista = binario.split(",")
    result = []
    for i in lista:
        num = int(i,2)
        if ((num % 5) == 0):
            result.append(i)
    return ",".join(result)
print(divisible_binary("0100,0011,1010,1001"))
