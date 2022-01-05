# escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

medida = float(input('Qual a metragem?:'))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('Analisando a metragem inserida de {} metros, temos {} kilometros, {} hectometro, {} decâmetro, {} decimetro, {} centimetros e {} milimetros'.format( medida, km, hm, dam, dm, cm, mm) )



#resposta que vi de um aluno nos comentarios do Youtube, fiquei confuso, porque não me parece que a variavel metros seja a variavel principal 
#d = float(input('Digite um valor: '))
#print(f'A medida de {d:.0f} corresponde a: ')
#print(f'{d/1000}km\n{d/100}hm\n{d/10}dam\n{d*1000:.0f}m\n{d*10:.0f}dm\n{d*100:.0f}cm\n{d*1000:.0f}mm')
