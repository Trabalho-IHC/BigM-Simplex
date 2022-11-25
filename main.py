# matriz possui 56 colunas e 36 linhas
# 10 variaveis de folga
# 20 variaveis

import functions
import matriz as mtrz

matriz = []
matriz = mtrz.export_matriz()

linhas = 0
colunas = 0

for c in range(len(matriz[-1])):
    colunas += 1

linhas = len(matriz)

def verifica_escalonamento():
    for a in range(0, colunas):
        if functions.verifica_valor_negativo_linha_z(matriz):
            functions.escalonamento(linhas, colunas, matriz)
    return functions.retorna_z(colunas, matriz)        
        

for a in range(10):
    functions.zera_var_artific_linha_z(linhas, colunas, matriz)

verifica_escalonamento()
#functions.show_matriz(linhas, matriz)
