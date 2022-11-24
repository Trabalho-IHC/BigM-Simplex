#matriz possui 56 colunas e 36 linhas
#10 variaveis de folga
#20 variaveis

import arquivos_real_oficial.funcoes as funcoes
import arquivos_real_oficial.matriz as matriz

L = 36
C = 56

for a in range(10):
  funcoes.zera_var_artific_linha_z(L, C, matriz)

#opcoes: 1. fazer for pra n escalonamentos
#2. fazer manual, colocando um por um
#3. chamar funcao verifica_z num loop até atingir c = 20, se nao atingir rodar escalonamento
#3 aparentemente mais promissora (tentar primeiro)
funcoes.escalonamento(L, C, matriz)
