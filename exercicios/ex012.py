#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

#este foi o que eu fiz

prod = float(input('Qual o valor do produto?:'))
desc = prod - prod * 0.05
print ('O produto inserido tem o novo valor de {:.2f}'.format(desc))


#este é o codigo que o professor deu!

#preço = float(input('Qual é o preço do produto R$'))
#novo = preço - (preço * 5 / 100)
#print('O Produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R${.:2f}'.format(preço, novo))