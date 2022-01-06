#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar!
# forma que eu fiz
#num = float(input ('digite um valor:'))
#dolar = (num / 3.27)

#print ('Você consegue comprar {:3} doláres.'.format( dolar))

#correto
real = float(input('quanto de dinehiro na carteria? R$'))
dolar = real / 3.27
print ('com R${:.2f} voce consegue comprar US${:.2f}'.format(real, dolar))
