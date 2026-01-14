a = 'XD'
b = 'LMAO'

print('> Jakies obliczeniowe cos <')
print()
print('1.Wydrukuj: XD')
print('2.Wydrukuj: XDLMAO')
print('3.Liczba liter w słownie: XDLMAO')
xd = int(input('Wybierz opcie: '))

if xd == 1:
	print(a)

if xd == 2:
	print(a + b)	

if xd == 3:
	print(len(a + b))