def Parzysta(): #Zad 1
	p = int(input('Wprowadź liczbe: '))
	if p in range(2, 99999999999999, 2):
		print('Liczba jest parzysta')
	else:
		print('liczba jest nieparzysta')

def Wiek():
	w = int(input('Wprowadz swój wiek: '))
	if w in range(1, 10):
		print('Jesteś dzieckiem')
	elif w in range(11,17):
		print('Jesteś nastolatkiem')
	else:
		print('Jesteś dorosły')

def 

print('> COS <')
print()
print('1.Sprawdź czy liczba jest parzysta')
print('2.Czy jesteś dorosły czy nastolatkiem od zależności od wieku')
print('3.')
xd = int(input('Wybierz opcie: '))

if xd == 1:
	print(Parzysta())

if xd == 2:
	print(Wiek())