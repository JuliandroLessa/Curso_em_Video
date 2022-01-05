n1 = int(input('Um valor:'))
n2 = int(input('outrovalor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

# para não quebrar uma linha para outra no final você acrescentar [,end=""]
# você coloca \n onde voce quer a quebra da linha.


print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end='')
print('Divisão inteira {} e Potência {}'.format(di, e))


#print('A soma vale {}'.format(n1+n2)) caso queria fazer algo mais simples se não
#
