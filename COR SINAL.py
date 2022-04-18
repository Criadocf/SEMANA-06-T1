# Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é
# vermelho) e retorne  a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.

def cor(x):
    if x == 'V':
        return 'Siga'
    elif x == 'A':
        return 'Atenção'
    elif x == 'E':
        return 'Pare'
    else:
        return 'INSIRA UMA ENTRADA VÁLIDA'

y = input().upper()

ch = cor(y)

print(ch)
        
        