my_list = [7, 8, 9, 'a', 'b', 'c']
print(my_list)

# Print all elements except the last one
print(my_list[:-1])

# Print every second element
print(my_list[::2])

# Print every second element up to the middle of the list
mid_len = len(my_list) // 2
print(my_list[:mid_len:2])

# Check if a variable x (with any value) is in the list
x = 7
if x in my_list:
    print(f'x is in my_list')
else:
    print('x is not in my_list')

# Show the difference between a tuple and a list
# 1. Mutowalność
# Lista jest mutowalna - możemy ją modyfikować, czyli zmieniać/dodawać/usuwać jej elementy
# Krotka (tuple) jest niemutowalna - nie można ich zmieniać po utworzeniu (nie można dodawać, usuwać ani modyfikować elementów w krotce)

# Lista (mutowalna)
my_list = [7, 8, 9, 'a', 'b', 'c']
my_list[1] = 7
my_list.append('d')
print(my_list)

# Krotka (tuple) niemutowalna
my_tuple = (7, 8, 9, 'a', 'b', 'c')
# my_tuple[1] = 7 spowoduje błąd
print(my_tuple)

# 2. Składnia
# Lista - tworzymy używając nawiasów kwadratowych
# Krotka - tworzymy używając nawiasów okrągłych

list1 = [7, 8, 9, 'a', 'b', 'c']
tuple1 = (7, 8, 9, 'a', 'b', 'c')

# 3. Wydajność
# Lista - listy są bardziej elastyczne niż krotki, ponieważ pozwalają na modyfikacje.
# Z tego względu dla listy przyznawana jest nadwyżka pamięci, aby te modyfikacje były mozliwe,
# ale przez to listy są mniej wydaje niż krotki

# Krotka (tuple) - jest bardziej wydajna, nie trzeba dla niej lokoważ aż tyle pamięci jak dla listy. Operacje na krotkach są szybsze
# ponieważ nie muszą zarządzać zmiennością (krotki są niemutowalne)


# 4. Metody
# Lista - listy posiadają wiele metod, np. append(), remove(), pop(), sort(), które modyfikują listę
# Krotka - krotki mają tylko dwie metody: count() i index(), ponieważ nie można ich modyfikować


# 5. Możliwość używania jako klucze w słowniku
# Lista - listy nie mogą być używane jako klucze w słowniku, ponieważ są mutowalne i nie są hashowalne
# Krotka - krotki są niemutowalne, więc mogą być używane jako klucze w słowniku, są hashowalne



# Add a new value after creating the list: At the end
list1.append('d')
print(list1)

# In the second position
list1.insert(1, 7.5)
print(list1)

# Remove the last value
list1.pop()
print(list1)

# Remove the value at the third position
# 1. Używając pop() z indeksem
list1.pop(2)
print(list1)

# 2. Albo używając del
del list1[2]
print(list1)

# Add a new list so that all elements are added to the existing list, resulting in a one-dimensional list
my_list1 = ['X', 'Y', 'Z']
my_list2 = ['A', 'X', 'C']

# 1. Używając extend()
my_list1.extend(my_list2)
print(my_list1)

# 2. Używając +=
my_list1 += my_list2
print(my_list1)

# Display how many times "X" appears in the list
count_X = my_list1.count('X')
print(f"Element X występuje {count_X} w liście my_list1")


