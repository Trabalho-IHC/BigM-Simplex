lista = []
# matriz.append([[2],[1],[1],[0],[0],[5000]])
# matriz.append([[4],[5],[0],[-1],[1],[13000]])
# matriz.append([[3],[7],[0],[0],[999999],[0]])
lista.append([2,1,1,0,0,5000])
lista.append([[4],[5],[0],[-1],[1],[13000]])
lista.append([[3],[7],[0],[0],[999999],[0]])

def mostrar_matriz():
    for l in range(0, 3):
        print(lista[l], end='\n')

mostrar_matriz()
print(lista[0][4])
