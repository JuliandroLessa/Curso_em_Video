#Faça um programa que leia a largura e a altura da parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la sabendo que cada litro pinta uma area de 2 metros quadrados.

altura = float(input('Qual a altura da sua parede?:'))
largura = float(input('Qual a largura da sua parede?:'))

area = altura * largura 

tinta = area / 2
print ('Sua parede tem {} m², Você vai precisar de {} litros de tinta para pintar esta parede'.format(area, tinta))

#este aqui em cima foi eu que fiz, abaixo vou escrever o que o professor fez.

#larg = float(input('largura da parede'))
#alt = float(input('Altura da parede'))
#área = larg * alt
#print('Sua parede tema dimesão de {}x{} e a sua área é de {}m²',format(larg, alt, area))
#tinta = área / 2
#print('Para pintar esta parede, você vai precisar de {}l de tinta'.format(tinta))