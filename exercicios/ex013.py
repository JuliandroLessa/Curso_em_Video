#Faça um Algoritmo que leia salário de um funcionario e mostre seu novo salario com 15% de aumento.

#este foi o que eu fiz
sal = float(input('Digite seu salário atual:'))
novo = sal + (sal * 15/100)
print('Salario atualizado de {:.2f}'.format(novo))

#este foi o dado pelo professor
#salário = float(input('Qual é o salrio do funcionário? R$'))
#novo = salário + (salário * 15/100)
#print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))