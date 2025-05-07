# Comprehension lists:
# 1. Zawierającą liczby od 1 do 100.

lista = [x for x in range(1, 101)]
print(lista)


# 2. Zawierającą tylko liczby parzyste od 1 do 100.

parzyste = [x for x in range(1, 101) if x % 2 == 0]
print(parzyste)


# 3. Zawierającą liczby od 1 do 100 które NIE znajdują się w liście c ([5,44,13,25]).

c = [5, 44, 13, 25]
lista_1 = [x for x in range(1, 101) if x not in c]
print(lista_1)


# 4. Dwuwymiarową, zawierającą 100 list, posiadających 1,2,3,4,5… elementów:
# [ [1], [1,2], [1,2,3]…]

two_dimension = [[x for x in range(1, i+1)] for i in range(1, 101)]
print(two_dimension)


# 5. Zawierającą potęgi liczb od 1 do 10.

potega = [x**2 for x in range(1, 11)]
print(potega)


# 6. Zawierającą liczby od 1 do 100 NIE podzielnych przez 6 i 4.

list_2 = [x for x in range(1, 101) if x % 6 != 0 and x % 4 != 0]
print(list_2)

# 7. Zawierającą 10 list pustych

puste_listy = [[] for _ in range(10)]
print(puste_listy)

# 8. Zawierającą wszystkie litery oprócz „e” oraz „c” ze zmiennej
# s = „Python jest językiem posiadającym różne cechy.”.

s = "Python jest językiem posiadającym różne cechy."
litery = [char for char in s if char not in 'ec']
print(litery)


# 9. Zawiera tylko liczby z podanej zmiennej tekstowej: zM7U0AS1J3jj09Afj!

zmienna = "zM7U0AS1J3jj09Afj!"
liczby = [char for char in zmienna if char.isdigit()]
print(liczby)


# 10. Wypisz wszystkie liczby pierwsze z zakresu 1 do 100. ZADANIE Z GWIAZDKĄ

def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# list comprehension do zebrania liczb pierwszych
liczby_pierwsze = [x for x in range(1, 101) if czy_pierwsza(x)]
print(liczby_pierwsze)


# 11.Używając comprehension list, stwórz słownik zawierający liczby (od i do 10) jako
# klucze i dziesięciokrotność tych liczb jako wartość. Przykładowy wynik:
# {1:10,2:20,3:30...10:100}

slownik = {x: x*10 for x in range(1, 11)}
print(slownik)


# 14.Używając comprehension list ( i innych składni ) wypisz w jednej linii sumę
# wszystkich kluczy i wartości z poniższej listy. Para klucz-wartość powinna być
# dodawana tylko w przypadku gdy wartość jest podzielna przez klucz lub odwrotnie.
# source = {5:20,10:4,18:9,2:11}
# oczekiwany wynik to: 5+20 + 18+9 = 52

source = {5: 20, 10: 4, 18: 9, 2: 11}

suma = sum([key + value for key, value in source.items() if value % key == 0 or key % value == 0])

print(suma)







