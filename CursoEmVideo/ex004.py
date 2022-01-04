#n = input('Digite algo:')
#print('Segue abaixo as informações:')
#print('Tipo primitivo:', type(n))
#print('Alfanúmerico:', n.isalnum())
#print('Alfabético:', n.isalpha())
#print('Numérico:', n.isnumeric())
#feito antes de 2019


#novo formato que vi no youtube curso em video em 2022.

a = input('Digite algo:')
print (f'so tem espacos?:{a.isspace()}')
print (f'É numérico?:{a.isnumeric()}')
print (f'É alfabético?:{a.isalpha()}')
print (f'É alfanumerico?;{a.isalnum()}')
print (f'Está em letras maiúsculas?:{a.isupper()}')
print (f'Está em letras minúsculas?:{a.islower()}')
print (f'Está capitalizada?: {a.istitle()}')

 
 