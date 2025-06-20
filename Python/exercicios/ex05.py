# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("Digite um número inteiro: "))
sucessor = num + 1
antecessor = num - 1
print(f"O sucessor de {num} é {sucessor} e o seu antecessor é {antecessor}.")