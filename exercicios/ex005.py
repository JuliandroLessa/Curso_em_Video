#Faça um programa que leia um numero inteiro e mostre na tela seu antecessor e o seu sucessor

n =int(input('Qual o numero?:'))


print ('Analisando o valor', n, end=" ")
print('seu antecessor', n-1, end=" ")
print ('seu sucessor', n+1) 


# esta é a resolução que ele mostrou na aula
# n = int(input('digite um numero))
# a = n-1
# s = n+1
# print ('Analisando o valor {}, seu antecessor é {}, seu sucessor é {}'. format(n, a, s))