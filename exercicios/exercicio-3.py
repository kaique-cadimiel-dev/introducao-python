# 🚀 Exercício 3: Faça um programa que, dado um valor n qualquer,
# tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n.

def create_square(num):
    count = 0
    while count < len(range(num)):
        count += 1
        print(num * '*')

create_square(5)
