# Escreva um programa que leia um caractere e mostra o valor booleano True
# (verdadeiro) se for um dígito entre ‘0’ e ‘9’ ou o valor booleano False (falso) caso
# contrário

def car(v):
    if v in('0','1','2','3','4','5','6','7','8','9'):
        return 'True'
    else:
        return 'False'
    
val = input()
ch = car(val)

print(ch)