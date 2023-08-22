'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''

a = int(input("Me informe um número:"))
b = int(input("Me informe um número:"))
c = int(input("Me informe um número:"))
d = int(input("Me informe um número:"))
while (a and b and c and d != 1):
    menor = a
    if (menor > b):
        b = menor
    if (menor > c):
        c = menor
    if (menor > d):
        d = menor
    maior = a
    if (maior < b):
        a = maior
    if (maior < c):
        a = maior
    if (maior < d):
        d = maior
    media = (a + b + c + d) / 4
print(f"Esse é o {menor} e esse é o {maior}, e a {media} desses números.")