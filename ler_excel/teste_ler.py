lista = []
lista.append([[2],[1],[1],[0],[0],[5000]])
lista.append([[4],[5],[0],[-1],[1],[13000]])
lista.append([[3],[7],[0],[0],[999999],[0]])


# matriz = []
# L = int(input("Digite o número de linhas:"))
# C = int(input("Digite o número de colunas:"))
# for i in range(L):
#     matriz.append([])

# for l in range(0, L):
#     for c in range(0, C):
#         matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

def teste():
    for l in range(0, 3):
        print(lista[l], end='\n')

# def show_matriz():
#   print("\n")
#   for l in range(0, L):
#     for c in range(0, C):
#         print(f'[{matriz[l][c]:^5}]')
#     print()

# create a variable to store final integer
var = '' 
 
#iterate over the list elements
for element in lista[0][0]: ##ISSO AQUI FUNCIONOU
    # converting integer to string and adding into variable
    var += str(element)
 
# converting back into integer and printing the final result
b = var
print(var) 

# if a > 0:
#     print("eeeee")

teste()
# show_matriz()
#print(lista)
