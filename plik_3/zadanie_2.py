#  Napisz funkcję is_even, która sprawdza, czy podana liczba jest parzysta.

def is_even(x):
    if x %2 == 0:
        return True
    else:
        return False

print(is_even(5))