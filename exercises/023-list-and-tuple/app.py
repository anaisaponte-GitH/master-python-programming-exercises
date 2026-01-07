# Your code here
def list_and_tuple(*args):
    lista = []
    tupla = ()
    for i in range(len(args)):
        lista.append(str(args[i]))
        tupla = tupla + (str(args[i]),)
    return lista, tupla
        
l,t = list_and_tuple(12,34,56,78,43)
print(l)
print(t)
