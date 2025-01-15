#  Bazując na podanej poniżej liście, stwórz słownik zawierający słowo jako klucz i
# jego długość jako wartość. Słowa (wartości) w słowniku powinny być unikalne!
# source = [“Breaking”, “Bad”, “Prison”, “Break”, “Bad”, “Grandpa”,”Break” ,”Out”]

source = ["Breaking", "Bad", "Prison", "Break", "Bad", "Grandpa", "Break", "Out"]
source = set(source)

result = {}

[result.update({i: len(i)}) for i in source]
dict_comprehension = {i: len(i) for i in source}

print(result)
print(dict_comprehension)
