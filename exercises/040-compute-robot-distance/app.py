# Your code here
def compute_robot_distance(mov_list):
    pasos = [0,0]
    for i in range(len(mov_list)):
        lista = mov_list[i].split(" ")
        if  lista[0] == 'UP':
            pasos[1] += int(lista[1])
        elif lista[0] == 'DOWN':
            pasos[1] -= int(lista[1])
        elif lista[0] == 'LEFT':
            pasos[0] -= int(lista[1])
        else:
            pasos[0] += int(lista[1])
    resultado = ((pasos[0]**2)+(pasos[1]**2))**0.5 
    return(round(resultado))

print(compute_robot_distance(["DOWN 20", "UP 5", "LEFT 5", "RIGHT 2"])) 


    
    