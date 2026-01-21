
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
	
		for x in range(1, 11):
			wynik = z * x
		print(f'{z} * {x} = {wynik}')


def palidro(): #zad 5
    slowo = input("Podaj słowo: ").lower()
    
    if slowo == slowo[::-1]:
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")

def CelnaFah():
	c = int(input('Wprowadź stopień Celciusza: '))
	f = c * 9/5 + 32
	print(f'Po obliczeniach wychodzi = {f}')

def FahnaCel():
	f = int(input('Wprowadź stopień Farenheita: '))
	c = f * 9/5 + 32
	print(f'Po obliczeniach wychodzi = {c}')

def Ocena():
    m = int(input('Podaj maksymalną ilość punktów: '))
    pro = int(input('Podaj liczbe punktów: '))
        
    procenty = pro / m * 100  
    
    print(f"{procenty}", "%")
    
def BMI():
    waga = float(input("Podaj wagę w kg: "))
    wzrost = float(input("Podaj wzrost w m: "))
    
    bmi = waga / (wzrost ** 2)
    
    print(f"Twoje BMI wynosi: {bmi}")
    
    if bmi < 18.5:
        print("Masz niedowagę")
    elif bmi < 25:
        print("Twoja waga jest w normie")
    else:
        print("Masz nadwagę")
        
def Trojkat():
    a = float(input("Podaj długość pierwszego boku: "))
    b = float(input("Podaj długość drugiego boku: "))
    c = float(input("Podaj długość trzeciego boku: "))
    
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            print("Z podanych boków można zbudować trójkąt")
        else:
            print("Z podanych boków NIE można zbudować trójkąta")
    else:
        print("Długości boków muszą być większe od 0")
        
def najliczba():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    c = float(input("Podaj trzecią liczbę: "))
    
    if a >= b and a >= c:
        print("Największa liczba to:", a)
    elif b >= a and b >= c:
        print("Największa liczba to:", b)
    else:
        print("Największa liczba to:", c)

print('> COS <')
print()
print('1.Sprawdź czy liczba jest parzysta')
print('2.Czy jesteś dorosły czy nastolatkiem od zależności od wieku')
print('3.Liczneie powyżej 10')
print('4.Tabliczka mnożenia dla liczb od 1 do 10')
print('5.Sprawdz czy słowo jest palindromem')
print('6.Celciusz na Fahrenheit')
print('7.Fahrenheit na Celciusz')
print('8.Ile ci wychodzi procent z punktów ze sprawdzianu')
print('9.Sprawdź swoje BMI')
print('10.Sprawdź czy wybrane liczby staną się trójkątem')
xd = int(input('Wybierz opcie: '))

if xd == 1:
	print(Parzysta())

elif xd == 2:
	print(Wiek())

elif xd == 3:
	print(Licz())

elif xd == 4:
	print(Tabliczka())

elif xd == 5:
	print(palidro())

elif xd == 6:
	print(CelnaFah())

elif xd == 7:
	print(FahnaCel())

elif xd == 8:
	print(Ocena())

elif xd == 9:
    print(BMI())
    
elif xd == 10:
    print(Trojkat())
    
elif xd == 11:
    print(najliczba())
	

else:
	print('NIE MA TAKIEJ OPCJI')
