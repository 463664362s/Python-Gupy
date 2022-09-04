#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

palavra = input(str("Digite a palavra que quer inverter:"))
palavra_invertida = "" 
for i in palavra: 
    palavra_invertida = i + palavra_invertida

print(palavra_invertida)
