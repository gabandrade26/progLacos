'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();
'''

b = int(input("Me informe um número para ser base:"))
e = int(input("Me informe um número para ser expoente:"))
cont = 1
acum = 1
while (cont <= e):
    acum = acum * b
    cont = cont + 1
print(f"A {b} elevado à {e} = {acum}.")