# Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno.
#Apresente a média das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar
#mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de
#10 ela deve ser ajustada para 10.

def nota_media(a,b,c):
    nota_media = (a+b+c)/3
    if c > 8:
        nota_media = nota_media + 1
    if nota_media > 10:
        nota_media = 10
    return f'{nota_media:.2f}'
    
p = int(input().strip())
s = int(input().strip())
t = int(input().strip())

ch = nota_media(p,s,t)
print(ch)
