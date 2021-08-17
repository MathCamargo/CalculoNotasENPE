def soma_prog2(lista):
    SomatorioDeNotas = 0
    for item in lista:
        SomatorioDeNotas += item
    return SomatorioDeNotas

########### Inserir suas notas aqui ###########
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
###############################################

lista_com_as_notas = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11]

MF = soma_prog2(lista_com_as_notas)/len(lista_com_as_notas)
print('Média: {:.2f}'.format(MF))
