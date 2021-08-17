def soma_e_peso_intrinf(lista):
    P1sp = lista[0] * 0.15
    P2sp = lista[1] * 0.3
    P3sp = lista[2] * 0.3
    P4sp = lista[3] * 0.25
    lista_com_pesos = [P1sp, P2sp, P3sp, P4sp]

    somatorio_das_notas = 0
    for item in lista_com_pesos:
        somatorio_das_notas += item
    return somatorio_das_notas

########### Inserir suas notas aqui ###########
N_TRAB = 0
N_PROVA1 = 0
N_PROVA2 = 0
N_PROVA3 = 0
###############################################

lista_com_notas = [N_TRAB, N_PROVA1, N_PROVA2, N_PROVA3]

MF = soma_e_peso_intrinf(lista_com_notas)

print('Média: {:.2f}'.format(MF))
