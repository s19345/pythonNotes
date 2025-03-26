# Pobierz od użytkownika listę liczb i wypisz tylko unikalne wartości (set)

user_list = input("Podaj liczby oddzielone spacjami: ")

user_list = user_list.split()

user_list = [int(number) for number in user_list]

unique_list = set(user_list)

print("Unikalne wartości: ", unique_list)


# Utwórz frozenset z kilku liczb i spróbuj dodać do niego nowy element – co się stanie?

frozen_values = [frozenset([1, 2, 3, 4, 5])]

try:
    frozen_values.add(6)
except AttributeError as e:
    print(e)

# ODP: kiedy próbujemy użyć metody .add(), Python zgłasza błąd AttributeError,
# ponieważ frozenset nie obsługuje modyfikacji (nie ma metody add() ani remove()).
# frozenset jest niemutowalny


# Stwórz dwa zbiory i sprawdź ich część wspólną oraz różnicę.

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}

common = set1 & set2

differece = set1 - set2

print(f"Część wspólna to: {common}")
print(f"Róznica to: {differece}")



