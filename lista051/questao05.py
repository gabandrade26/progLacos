'''
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:
Considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
'''

cont = int(input("Me informe um número:"))
mult = 1
while (mult <= 10):
    print(f"{cont} . {mult} = {cont * mult}")
    mult = mult + 1
