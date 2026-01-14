def Parzysta(): #Zad 1
	p = int(input('Wprowadź liczbe: '))
	if p in range(2, 99999999999999, 2):
		print('Liczba jest parzysta')
	else:
		print('liczba jest nieparzysta')

def Wiek(): #zad 2
	w = int(input('Wprowadz swój wiek: '))
	if w in range(1, 10):
		print('Jesteś dzieckiem')
	elif w in range(11,17):
		print('Jesteś nastolatkiem')
	else:
		print('Jesteś dorosły')

def Licz(): #zad 3
	list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
	for a in list:
		if a > 10:
			print(a)


def Tabliczka(): #zad 4
	for z in range(1, 11):
		for x in range(1, 11):
			wynik = z * x
		print(f'{z} * {x} = {wynik }')


def palidro(): #zad 5
	print(nic)
	



print('> COS <')
print()
print('1.Sprawdź czy liczba jest parzysta')
print('2.Czy jesteś dorosły czy nastolatkiem od zależności od wieku')
print('3.Liczneie powyżej 10')
print('4.Tabliczka mnożenia dla liczb od 1 do 10')
xd = int(input('Wybierz opcie: '))

if xd == 1:
	print(Parzysta())

if xd == 2:
	print(Wiek())

if xd == 3:
	print(Licz())

if xd == 4:
	print(Tabliczka())

if xd == 5:
	print(palidro())
