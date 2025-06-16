a = 'a'
b = 3
c = 5.5

# przewidywania dla dodawania
# a + b -> błąd, nie da się dodać string + int
# a + c -> błąd, nie da się dodać string + float
# b + c -> ok, wynik to float

try:
    print(a + b)
except TypeError as e:
    print(f'Błąd dla a + b: {e}')

try:
    print(a + c)
except TypeError as e:
    print(f'Błąd dla a + c: {e}')

try:
    print(b + c)
except TypeError as e:
    print(f'Błąd dla b + c: {e}')




