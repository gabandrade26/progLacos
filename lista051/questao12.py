'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''

a = float(input("Me informe um número:"))
menor = a
maior = a
cont = -1
soma = 0
media = soma / cont
while (a != -1):
    a = float(input("Me informe um número:"))
    soma = soma + a
    cont = cont + 1
    if (maior < a):
        maior  = a
    if (menor > a):
        menor = a
    a = float(input("Me informe um número:"))
    if (maior == -1):
        print("Você inseriu -1 na primeira resposta.")
print(f"Esse é o menor desse é {menor} e esse é o maior {maior}, e a média desses números é {media}.")
