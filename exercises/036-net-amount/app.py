# Your code here
def net_amount(reg_trans):
    dic = {"D": 0, "W": 0}
    lista = reg_trans.split(" ")
    for x in range(len(lista)-1):
        if (lista[x] == 'D'):
            dic["D"] += int(lista[x+1])
        elif (lista[x] == 'W'):
            dic["W"] += int(lista[x+1])
        
    return (dic["D"] - dic["W"])

print(net_amount("D 300 D 300 W 200 D 100"))