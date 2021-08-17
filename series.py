########### Inserir suas notas aqui ###########
AVS1 = 0
AVS2 = 0
NAVS = (AVS1 + AVS2) / 2

T1 = 0
T2 = 0
T3 = 0
NTarefa = (T1 + T2 + T3) / 3

S1 = 0
S2 = 0
S3 = 0
S4 = 0
S5 = 0
S6 = 0
S7 = 0
S8 = 0
S9 = 0
S10 = 0
S11 = 0
S12 = 0
###############################################

lista_simulado = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12]
lista_simulado_soma = 0
for k in range(len(lista_simulado)):
    for j in range(len(lista_simulado)):
        if lista_simulado[k] > lista_simulado[j]:
            lista_simulado[k], lista_simulado[j] = lista_simulado[j], lista_simulado[k]

for k in range(len(lista_simulado) - 1):
    lista_simulado_soma += lista_simulado[k]
NSimulado = lista_simulado_soma / 11



N = (NTarefa + NSimulado) / 2


MF = 0.8 * NAVS + 0.2 * N

print('Média: {:.2f}'.format(MF))
