# Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da
# mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o
# sexo feminino. Use o número inteiro para identificar masculino e 2 para identificar feminino.



nome = input()
sexo = int(input())

if sexo == 1:
    print('Ilmo Sr. ' + nome)
else:
    print('Ilma Sra. ' + nome)

    


