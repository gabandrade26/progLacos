'''
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200
'''
import math

cont = 15
while (cont <= 200):
    print(f"O {cont} elevado ao quadrado {math.pow(cont,2):.0f}")
    cont = cont + 1
