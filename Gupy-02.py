# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

numeroAnterior = -1 
numeroAtual = 1

numero = int(input("Digite um número para verificar se ele está na sequência de Fibonacci: "))

while(1):
    fibonacci = numeroAnterior + numeroAtual
    numeroAnterior = numeroAtual
    numeroAtual = fibonacci
    if fibonacci == numero:
        print("O número",numero,"está na sequência de Fibonacci")
        break
    if fibonacci > numero:
        print("O número",numero,"não está na sequência de Fibonacci")
        break

  
