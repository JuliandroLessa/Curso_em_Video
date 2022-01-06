# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

#resposta certa.
num = int(input('Digita um número para ver sua tabuada:'))
print ('-' * 12)
print ('{} x {:2} = {:02}'.format(num, 1, num*1))
print ('{} x {:2} = {}'.format(num, 2, num*2))
print ('{} x {:2} = {}'.format(num, 3, num*3))
print ('{} x {:2} = {}'.format(num, 4, num*4))
print ('{} x {:2} = {}'.format(num, 5, num*5))
print ('{} X {:2} = {}'.format(num, 6, num*6))
print ('{} x {:2} = {}'.format(num, 7, num*7))
print ('{} x {:2} = {}'.format(num, 8, num*8))
print ('{} x {:2} = {}'.format(num, 9, num*9))
print ('{} x {:2} = {}'.format(num, 10, num*10))
print ('-' * 12)  # {:-^12}, este é o exemplo que eu tinha imaginado.


#num = int(input('Insira um numero:'))

# foi o que pensei na hora de fazer! tive que colar para conseguir fazer.



#('Sua tabuada é: {}*1 \n {}*2 \n {}*3 \n {}*4 \n {}*5 \n {}*6 \n {}*7 \n {}*8 \n {}*9 \n {}*10'.format(n))
