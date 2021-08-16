def soma_e_peso_algelin(lista):
    P1sp = lista[0]  * 3.5
    P2sp = lista[1]  * 3.5
    P3sp = lista[2]  * 3.0
    lista_com_pesos = [P1sp, P2sp, P3sp]
    somatorio_das_notas = 0
    for item in lista_com_pesos:
        somatorio_das_notas += item
    return somatorio_das_notas


P1 = 0
P2 = 0
P3 = 0
lista_com_as_notas = [P1, P2, P3]

MF= soma_e_peso_algelin(lista_com_as_notas) / 10
print('Média: {:.2f}'.format(MF))